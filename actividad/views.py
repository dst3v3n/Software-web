from django.shortcuts import render , redirect
from django.views.generic import View , ListView
from .forms import Form_actividad , Form_archivo
from usuario.models import Perfil
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Actividades
from django.utils import timezone
from django.db.models import Case, When
import sweetify
import openpyxl

# Create your views here.

class registro_actividad (LoginRequiredMixin , View):
    template_name = 'from_registro_activity.html'

    def get (self, request):
        if Perfil.objects.filter(myuser_id = self.request.user.id).exists():
            context = {
                'form_activity' : Form_actividad
            }
            return render(request , self.template_name, context)
        else:
            return redirect ('perfil_user')

    def post (self, request):
        form = Form_actividad(request.POST)
        if form.is_valid():
            info = form.save(commit = False)
            info.myuser_id = self.request.user.id
            info.save()
            sweetify.toast(self.request, 'La actividad ha sido creada' , timer=4000)
            return redirect ('registro_actividad')

class visualizar_actividad (LoginRequiredMixin , ListView):
    model = Actividades
    template_name = 'visualizar_actividades.html'
    paginate_by = 12

    def get(self, request, *args, **kwargs):
        if not Perfil.objects.filter(myuser_id=self.request.user.id).exists():
            return redirect('perfil_user')
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(myuser_id =  self.request.user.id).order_by(
            Case(
                When(proceso='Sin iniciar', then=0),
                When(proceso='En proceso', then=1),
                When(proceso='Terminado', then=2),
                default=3
            ),
            'id'
        )
        return qs

    def post(self , request):
        if request.POST.get('_method') == 'PUT':
            return self.put(request)
        else:
            dateInicio = timezone.now()
            Actividades.objects.filter(pk=request.POST.get('id')).update(
                dateInicio=dateInicio,
                proceso="En proceso",
            )
            sweetify.toast(self.request, 'La actividad ha sido iniciada' , timer=4000)
            return redirect('visualizar_actividad')

    def put (self, request):
        dateFin = timezone.now()
        boolean = True
        actividad = Actividades.objects.get(pk = request.POST.get('id'))
        diferencia = dateFin - actividad.dateInicio
        Actividades.objects.filter(pk=request.POST.get('id')).update(
            dateFin=dateFin,
            proceso='Terminado',
            tiempo = diferencia
        )
        sweetify.toast(self.request, 'La actividad ha sido terminada' , timer=4000)
        return redirect('visualizar_actividad')

class Archivo(LoginRequiredMixin , View):
    template_name = 'subir_archivo.html'
    form_class = Form_archivo

    def get (self , request):
        if Perfil.objects.filter(myuser_id = self.request.user.id).exists():
            context = {'form' : self.form_class}
            return render (request , self.template_name , context)
        else:
            return redirect ('perfil_user')

    def post (self , request):
        form = Form_archivo(request.POST, request.FILES)
        if form.is_valid():
            archivo_excel = request.FILES['archivo']
            wb = openpyxl.load_workbook(archivo_excel)
            sheet = wb.active
            for row in sheet.iter_rows(values_only=True):
                if isinstance(row[0] , int) == True and not row[0] == None:
                    actividad = Actividades(
                        myuser_id =  row[0],
                        actividad = row[1],
                        descripcion = row[2],
                        dateInicio = row[3],
                        dateFin = row[4],
                        proceso = row[5],
                    )
                    if row[3] and row[4] != None:
                        resultado = row[4] - row[3]
                        actividad.tiempo = resultado
                    sweetify.toast(self.request, 'Los archivos fueron subidos' , timer=4000)
                    actividad.save()
            return redirect('archivo')
        else:
            sweetify.toast(self.request, 'Los archivos no pudieron ser subidos', icon = 'error' , timer=4000)
            form = Form_archivo()
            return render(request, 'upload_excel.html', {'form': form})

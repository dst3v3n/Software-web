def nucleo ():
    return {
        ('' , 'selecciona tu nucleo familiar'),
        ("Pareja con hijos dependientes" , "Pareja con hijos dependientes"),
        ("Pareja sin hijos dependientes" , "Pareja sin hijos dependientes"),
        ("Hogar grupal" , "Hogar grupal"),
        ("Hogar multifamiliar" , "Hogar multifamiliar"),
        ("Familia monoparental con hijos dependientes" , "Familia monoparental con hijos dependientes"),
        ("Otro hogar unifamiliar" , "Otro hogar unifamiliar"),
        ("Persona soltera" , "Persona soltera"),
    }

def respuesta ():
    return {
        ('' , 'selecciona tu respuesta'),
        ("Ni poco probable ni probable" , "Ni poco probable ni probable"),
        ("Algo probable" , "Algo probable"),
        ("Algo improbable" , "Algo improbable"),
        ("Muy probable" , "Muy probable"),
        ("Muy improbable" , "Muy improbable"),
    }

def sector():
    return {
        ("", "Selecciona su cargo"),
        ('Trabajadores de oficina y administrativos - Apoyo clerical y de oficina' , 'Trabajadores de oficina y administrativos - Apoyo clerical y de oficina'),
        ('Trabajadores de oficina y administrativos - Trabajadores clericales generales' , 'Trabajadores de oficina y administrativos - Trabajadores clericales generales'),
        ('Trabajadores de oficina y administrativos - Oficinistas de consulta y recepcionistas' , 'Trabajadores de oficina y administrativos - Oficinistas de consulta y recepcionistas'),
        ('Trabajadores de oficina y administrativos - Oficinistas numéricos' , 'Trabajadores de oficina y administrativos - Oficinistas numéricos'),
        ('Trabajadores de oficina y administrativos - Gerentes de oficina y administradores de programas' , 'Trabajadores de oficina y administrativos - Gerentes de oficina y administradores de programas'),
        ('Trabajadores de oficina y administrativos - Otros trabajadores clericales y administrativos' , 'Trabajadores de oficina y administrativos - Otros trabajadores clericales y administrativos'),
        ('Trabajadores de oficina y administrativos - Asistentes personales y secretarias' , 'Trabajadores de oficina y administrativos - Asistentes personales y secretarias'),
        ('Trabajadores de servicios comunitarios y personales - Cuidadores y asistentes' , 'Trabajadores de servicios comunitarios y personales - Cuidadores y asistentes'),
        ('Trabajadores de servicios comunitarios y personales - Trabajadores de apoyo en salud y bienestar' , 'Trabajadores de servicios comunitarios y personales - Trabajadores de apoyo en salud y bienestar'),
        ('Trabajadores de servicios comunitarios y personales - Trabajadores de hostelería' , 'Trabajadores de servicios comunitarios y personales - Trabajadores de hostelería'),
        ('Trabajadores de servicios comunitarios y personales - Trabajadores de servicios de protección' , 'Trabajadores de servicios comunitarios y personales - Trabajadores de servicios de protección'),
        ('Obreros - Limpiadores y trabajadores de lavandería' , 'Obreros - Limpiadores y trabajadores de lavandería'),
        ('Obreros - Obreros de construcción y minería' , 'Obreros - Obreros de construcción y minería'),
        ('Obreros - Trabajadores de procesos en fábricas' , 'Obreros - Trabajadores de procesos en fábricas'),
        ('Obreros - Trabajadores de granjas, silvicultura y jardines' , 'Obreros - Trabajadores de granjas, silvicultura y jardines'),
        ('Obreros - Asistentes de preparación de alimentos' , 'Obreros - Asistentes de preparación de alimentos'),
        ('Obreros - Otros obreros' , 'Obreros - Otros obreros'),
        ('Operadores de maquinaria y conductores - Operadores de máquinas y plantas estacionarias' , 'Operadores de maquinaria y conductores - Operadores de máquinas y plantas estacionarias'),
        ('Operadores de maquinaria y conductores - Operadores de plantas móviles' , 'Operadores de maquinaria y conductores - Operadores de plantas móviles'),
        ('Operadores de maquinaria y conductores - Conductores de carretera y ferrocarril' , 'Operadores de maquinaria y conductores - Conductores de carretera y ferrocarril'),
        ('Operadores de maquinaria y conductores - Almacenistas' , 'Operadores de maquinaria y conductores - Almacenistas'),
        ('Gerentes - Directores ejecutivos, gerentes generales y legisladores' , 'Gerentes - Directores ejecutivos, gerentes generales y legisladores'),
        ('Gerentes - Agricultores y gerentes de granjas' , 'Gerentes - Agricultores y gerentes de granjas'),
        ('Gerentes - Gerentes de hostelería, retail y servicios' , 'Gerentes - Gerentes de hostelería, retail y servicios'),
        ('Gerentes - Gerentes especializados' , 'Gerentes - Gerentes especializados'),
        ('Profesionales - Profesionales de las artes y los medios' , 'Profesionales - Profesionales de las artes y los medios'),
        ('Profesionales - Profesionales en negocios, recursos humanos y mercadeo' , 'Profesionales - Profesionales en negocios, recursos humanos y mercadeo'),
        ('Profesionales - Profesionales en diseño, ingeniería, ciencia y transporte' , 'Profesionales - Profesionales en diseño, ingeniería, ciencia y transporte'),
        ('Profesionales - Profesionales en educación' , 'Profesionales - Profesionales en educación'),
        ('Profesionales - Profesionales de la salud' , 'Profesionales - Profesionales de la salud'),
        ('Profesionales - Profesionales de TIC' , 'Profesionales - Profesionales de TIC'),
        ('Profesionales - Profesionales en derecho, social y bienestar' , 'Profesionales - Profesionales en derecho, social y bienestar'),
        ('Trabajadores de ventas - Asistentes de ventas y vendedores' , 'Trabajadores de ventas - Asistentes de ventas y vendedores'),
        ('Trabajadores de ventas - Representantes y agentes de ventas' , 'Trabajadores de ventas - Representantes y agentes de ventas'),
        ('Trabajadores de ventas - Apoyo a las ventas' , 'Trabajadores de ventas - Apoyo a las ventas'),
        ('Técnicos y trabajadores calificados - Trabajadores calificados en automoción e ingeniería' , 'Técnicos y trabajadores calificados - Trabajadores calificados en automoción e ingeniería'),
        ('Técnicos y trabajadores calificados - Trabajadores calificados en construcción' , 'Técnicos y trabajadores calificados - Trabajadores calificados en construcción'),
        ('Técnicos y trabajadores calificados - Trabajadores calificados en electrotecnología y telecomunicaciones' , 'Técnicos y trabajadores calificados - Trabajadores calificados en electrotecnología y telecomunicaciones'),
        ('Técnicos y trabajadores calificados - Técnicos en ingeniería, TIC y ciencia' , 'Técnicos y trabajadores calificados - Técnicos en ingeniería, TIC y ciencia'),
        ('Técnicos y trabajadores calificados - Trabajadores calificados en alimentos' , 'Técnicos y trabajadores calificados - Trabajadores calificados en alimentos'),
        ('Técnicos y trabajadores calificados - Otros técnicos y trabajadores calificados' , 'Técnicos y trabajadores calificados - Otros técnicos y trabajadores calificados'),
        ('Técnicos y trabajadores calificados - Trabajadores calificados en animales y horticultura' , 'Técnicos y trabajadores calificados - Trabajadores calificados en animales y horticultura')
    }

def cargo():
    return {
        ("", "Selecciona su sector"),
        ("Alojamiento y alimentos", "Alojamiento y alimentos"),
        ("Administración y apoyo", "Administración y apoyo"),
        ("Agricultura, silvicultura y pesca", "Agricultura, silvicultura y pesca"),
        ("Artes y recreación", "Artes y recreación"),
        ("Salud", "Salud"),
        ("Construcción", "Construcción"),
        ("Educación y formación", "Educación y formación"),
        ("Electricidad, gas, agua y desechos", "Electricidad, gas, agua y desechos"),
        ("Finanzas y seguros", "Finanzas y seguros"),
        ("Atención de la salud y asistencia social", "Atención de la salud y asistencia social"),
        ("Medios de información y telecomunicaciones", "Medios de información y telecomunicaciones"),
        ("Manufactura", "Manufactura"),
        ("Minería", "Minería"),
        ("Otros servicios", "Otros servicios"),
        ("Profesionales, científicos y técnicos", "Profesionales, científicos y técnicos"),
        ("Administración pública y seguridad", "Administración pública y seguridad"),
        ("Alquiler, arrendamiento y bienes raíces", "Alquiler, arrendamiento y bienes raíces"),
        ("Comercio minorista", "Comercio minorista"),
        ("Transporte, postal y almacenamiento", "Transporte, postal y almacenamiento"),
        ("Comercio mayorista", "Comercio mayorista"),
    }

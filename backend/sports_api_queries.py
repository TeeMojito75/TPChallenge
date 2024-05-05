import requests
from datetime import datetime, timedelta

def obtener_ligas_por_pais_y_deporte(pais, deporte):
    # Construir la URL para obtener todas las ligas por país y deporte
    url_ligas = "https://www.thesportsdb.com/api/v1/json/60130162/search_all_leagues.php?"
    parametros = {'c': pais, 's': deporte}

    # Hacer la solicitud GET a la API
    response = requests.get(url_ligas, params=parametros)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Obtener los datos de las ligas en formato JSON
        datos_ligas = response.json()
        return datos_ligas.get('countries', [])
    else:
        # Si la solicitud falla, imprimir el mensaje de error
        print("Error al obtener las ligas:", response.text)
        return None

def obtener_eventos_por_liga_y_dia(liga_id, dia):
    # Construir la URL para obtener los eventos por liga y día
    url_eventos = f"https://www.thesportsdb.com/api/v1/json/60130162/eventsday.php?"
    parametros = {'l': liga_id, 'd': dia}

    # Hacer la solicitud GET a la API
    response = requests.get(url_eventos, params=parametros)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Obtener los datos de los eventos en formato JSON
        datos_eventos = response.json()
        return datos_eventos['events']
    else:
        # Si la solicitud falla, imprimir el mensaje de error
        print("Error al obtener los eventos:", response.text)
        return None

def obtener_personas_y_eventos(pais, deporte, fecha_inicio, fecha_fin, personas):
    resultado = {}
    
    # Obtener todas las ligas por país y deporte
    ligas = obtener_ligas_por_pais_y_deporte(pais, deporte)
    """
    if ligas:
        # Generar un rango de fechas entre la fecha de inicio y la fecha de fin
        delta = fecha_fin - fecha_inicio
        for i in range(delta.days + 1):
            fecha = fecha_inicio + timedelta(days=i)
            eventos_del_dia = []
            personas_del_dia = []
            
            # Iterar sobre cada liga para obtener los eventos en un día específico
            for liga in ligas:
                liga_id = liga['idLeague']
                liga_name = liga['strLeague']
                eventos = obtener_eventos_por_liga_y_dia(liga_id, fecha.strftime("%Y-%m-%d"))
                if eventos:
                    for evento in eventos:
                        eventos_del_dia.append({
                            'liga':liga_name,
                            'nombre_evento': evento['strEvent'],
                            'lugar_evento': evento['strVenue']
                        })
                        # Agregar más datos del evento si es necesario
                        
            # Obtener personas que tienen actividades ese día
            for nombre_persona, fechas_persona in personas.items():
                print(fecha)
                print("-----")
                for f in fechas_persona: print(f)
                print("aaaaaaa")
                if fecha in fechas_persona:
                    personas_del_dia.append(nombre_persona)
            
            resultado[fecha.strftime("%Y-%m-%d")] = {
                'eventos': eventos_del_dia,
                'personas': personas_del_dia
            }
    """

    # Generar un rango de fechas entre la fecha de inicio y la fecha de fin
    delta = fecha_fin - fecha_inicio
    for i in range(delta.days + 1):
        fecha = fecha_inicio + timedelta(days=i)
        eventos_del_dia = []
        personas_del_dia = []
        
        if ligas:
            # Iterar sobre cada liga para obtener los eventos en un día específico
            for liga in ligas:
                liga_id = liga['idLeague']
                liga_name = liga['strLeague']
                eventos = obtener_eventos_por_liga_y_dia(liga_id, fecha.strftime("%Y-%m-%d"))
                if eventos:
                    for evento in eventos:
                        eventos_del_dia.append({
                            'liga':liga_name,
                            'nombre_evento': evento['strEvent'],
                            'lugar_evento': evento['strVenue']
                        })
                        # Agregar más datos del evento si es necesario
                        
        # Obtener personas que tienen actividades ese día
        for nombre_persona, fechas_persona in personas.items():
            print(fecha)
            print("-----")
            for f in fechas_persona: print(f)
            print("aaaaaaa")
            if fecha in fechas_persona:
                personas_del_dia.append(nombre_persona)
        
        resultado[fecha.strftime("%Y-%m-%d")] = {
            'eventos': eventos_del_dia,
            'personas': personas_del_dia
        }




    print("#####################")
    
    return resultado


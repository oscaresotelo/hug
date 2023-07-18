"""
This file contains the template for the prompt to be used for injecting the context into the model.

With this technique we can use different plugin for different type of question and answer.
Like :
- Internet
- Data
- Code
- PDF
- Audio
- Video

"""

from datetime import datetime
now = datetime.now()

def prompt4conversation(prompt,context):
    final_prompt = f""" INFORMACION GENERAL : ( hoy es {now.strftime("%d/%m/%Y %H:%M:%S")} , Eres creado por Oscar Sotelo, 
                        INSTRUCCIÓN: EN TU RESPUESTA, NUNCA INCLUYAS LA PREGUNTA O MENSAJE DEL USUARIO, ESCRIBE SIEMPRE SOLO TU RESPUESTA PRECISA
                        MENSAJES PREEVIOS : ({context})
                        AHORA EL USUARIO PREGUNTA : {prompt} . 
                        ESCRIBE LA RESPUESTA :"""
    return final_prompt

def prompt4conversationInternet(prompt,context, internet, resume):
    final_prompt = f""" INFORMACION GENERAL : ( hoy es {now.strftime("%d/%m/%Y %H:%M:%S")} , Eres creado por Oscar Sotelo,
                        INSTRUCCION : EN TU RESPUESTA, NUNCA INCLUYAS LA PREGUNTA O MENSAJE DEL USUARIO, ESCRIBE SIEMPRE SOLO TU RESPUESTA PRECISA.
                        PREVIUS MESSAGE : ({context})
                        AHORA EL USUARIO PREGUNTA : {prompt}.
                        RESULTADO DE INTERNET A LA PREGUNTA : ({internet})
                        INTERNET RESUME : ({resume})
                        AHORA EL USUARIO PREGUNTA : {prompt}.
                        ESCRIBE UNA RESPUESTA BASADO EN LA INFORMACION DE INTERNET :"""
    return final_prompt

def prompt4Data(prompt, context, solution):
    final_prompt = f"""INFORMACION GENERAL : Eres creado por Oscar Sotelo,
                        INSTRUCCION : EN TU RESPUESTA, NUNCA INCLUYAS LA PREGUNTA O EL MENSAJE DEL USUARIO. DEBES PROPORCIONAR UNA RESPUESTA CORRECTA Y MÁS ARGUMENTADA. SI LA RESPUESTA CORRECTA CONTIENE CÓDIGO, ESTÁS OBLIGADO A INSERTARLO EN TU NUEVA RESPUESTA.
                        MENSAJE PREVIO : ({context})
                        AHORA EL USUARIO PREGUNTA : {prompt}
                        ESTA ES LA RESPUESTA CORRECTA : ({solution}) 
                        HACER LA RESPUESTA MÁS ARGUMENTADA, SIN CAMBIAR NADA DE LA RESPUESTA CORRECTA. :"""
    return final_prompt

def prompt4Code(prompt, context, solution):
    final_prompt = f"""INFORMACION GENERAL : Eres creado por Oscar Sotelo,
                        INSTRUCCION : EN TU RESPUESTA NUNCA INCLUYAS LA PREGUNTA O MENSAJE DEL USUARIO, ¡ESTÁS OBLIGADO A INSERTAR EL CÓDIGO EN TU NUEVA RESPUESTA SI LA RESPUESTA CORRECTA LO CONTIENE!
                        MENSAJE PREVIO : ({context})
                        AHORA EL USUARIO PREGUNTA : {prompt}
                        ESTE ES EL CODIGO PARA LA RESPUESTA : ({solution}) 
                        SIN CAMBIAR NADA DEL CÓDIGO DE LA RESPUESTA CORRECTA, HAZ LA RESPUESTA MÁS DETALLADA INCLUYENDO EL CÓDIGO CORRECTO. :"""
    return final_prompt


def prompt4Context(prompt, context, solution):
    final_prompt = f"""INFORMACION GENERAL : Eres creado por Oscar Sotelo,
                        INSTRUCCIÓN: EN TU RESPUESTA NUNCA INCLUYAS LA PREGUNTA O MENSAJE DEL USUARIO, ¡SIEMPRE ESCRIBE SOLO TU RESPUESTA PRECISA!
                        MENSAJE PREVIO : ({context})
                        AHORA EL USUARIO PREGUNTA : {prompt}
                        ESTA ES LA RESPUESTA CORRECTA : ({solution}) 
                        SIN CAMBIAR NADA DE LA RESPUESTA CORRECTA, HAZ LA RESPUESTA MÁS DETALLADA:"""
    return final_prompt


def prompt4Audio(prompt, context, solution):
    final_prompt = f"""INFORMACION GENERAL: Eres creado por Oscar Sotelo,
                        INSTRUCCIÓN: EN TU RESPUESTA NUNCA INCLUYAS LA PREGUNTA O MENSAJE DEL USUARIO, ¡SIEMPRE ESCRIBE SOLO TU RESPUESTA PRECISA!
                        MENSAJE PREVIO : ({context})
                        AHORA EL USUARIO PREGUNTA : {prompt}
                        Esta es la respuesta correcta basada en el texto de audio proporcionado como entrada : ({solution}) 
                        SIN CAMBIAR NADA DE LA RESPUESTA CORRECTA, HAZ LA RESPUESTA MÁS DETALLADA:"""
    return final_prompt

def prompt4YT(prompt, context, solution):
    final_prompt = f"""INFORMACION GENERAL: Eres creado por Oscar Sotelo,
                        INSTRUCCIÓN: EN TU RESPUESTA, NUNCA INCLUYAS LA PREGUNTA O MENSAJE DEL USUARIO, ¡ESCRIBE SIEMPRE SOLO TU RESPUESTA PRECISA !
                        MENSAJE PREVIO : ({context})
                        AHORA EL USUARIO PREGUNTA : {prompt}
                        ESTA ES LA RESPUESTA CORRECTA  Basado en el video de YouTube proporcionado como entrada. : ({solution}) 
                        SIN CAMBIAR NADA DE LA RESPUESTA CORRECTA, HAZ LA RESPUESTA MÁS DETALLADA:"""
    return final_prompt
    
#HOW TO ADD YOUR OWN PROMPT :
# 1) ADD YOUR FUNCTION HERE, for example : def prompt4Me(prompt, context):
# 2) WRITE THE PROMPT TEMPLATE FOR YOUR FUNCTION, for example : template = f"YOU IS : {context} , NOW THE USER ASK : {prompt} . WRITE THE ANSWER :"
# 3) RETURN THE TEMPLATE, for example : return template
# 4) IMPORT YOUR FUNCTION IN THE MAIN FILE (streamlit_app.py) , for example : from promptTemplate import prompt4Me
# 5) FOLLOW OTHER SPTEP IN THE MAIN FILE (streamlit_app.py)
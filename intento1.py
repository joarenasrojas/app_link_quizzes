import streamlit as st
import unidecode

# Define aquí la lista de nombres de tus estudiantes
nombres = [
'Arenas Rojas, José Rafael Felipe', 
'Acevedo Pino, Felipe Ignacio', 
'Acosta Martínez, Marcelo Pablo', 
'Acuña Calderón, Alberto Sebastián', 
'Aguilar Muñoz, Matías Sebastian', 
'Ahumada Palma, Martina Isidora', 
'Álvarez Pezoa, Lucas Alonso', 
'Andrade Zúñiga, Yeraldi Estefanía', 
'Aránguiz Candia, Paulina Andrea', 
'Aravena Moraga, Cristian Luis', 
'Arce Rosales, Amaro Jesús', 
'Arena Sáez, Ignacio Alonso', 
'Arévalo Díaz, Javiera Constanza', 
'Ariztía Valdivia, María José', 
'Auth Rojas, Sofía', 
'Baez Quiroz, Tomás Ignacio', 
'Baeza Jofré, Alejandro Javier', 
'Banda Zúñiga, Daniela Constanza', 
'Banha Pires, Isabel', 
'Baro Riquelme, Gerardo Alonso', 
'Barría Toledo, Agustín Javier', 
'Becerra Gómez, Fernanda Paz', 
'Belmar Zúñiga, Diego Orlando', 
'Bettocchi Cortés, Benjamín Eduardo', 
'Bravo Parada, Rebeca', 
'Carranza Fredes, Romina Danae', 
'Carrasco Henríquez, Javiera Ignacia', 
'Carter Saavedra, Ailyn Dannae Carolina', 
'Castro Díaz, Ariel Miguel Angel', 
'Cerda Araya, Cristóbal Adolfo', 
'Cerda Werches, Javiera Andrea', 
'Chávez Vega, Diego de Jesús', 
'Chicao Sandoval, Rodrigo Arturo', 
'Codorniú Fornes, Arturo Francisco', 
'Concha Padilla, Diego Alberto', 
'Curiqueo Velásquez, Patricio Alfonso', 
'De Goyeneche Yacometti, Miranda Antonia', 
'Díaz Cares, Ignacio Antonio', 
'Díaz Silva, Antonia Paz', 
'Donat Jofré, Constanza Alejandra', 
'Escamilla Durán, María Camila', 
'Escobar Llanquilef, Jorge Andrés', 
'Escobar Rivera, Bernardita Antonia', 
'Fahrenkrog Mamani, Werner Whyatt', 
'Farías Venegas, Rocío Rayen', 
'Farren Avaria, Maximiliano Raúl', 
'Ferrada Torres, Fabiana José', 
'Fierro Araya, Ricardo Esteban', 
'Fierro Gómez, Claudio Felipe', 
'Franco Botro, Alan Santiago', 
'Gajardo Barrientos, José Antonio', 
'García Gallardo, Valeria Alejandra', 
'García Rojas, Josué Nahum', 
'Gaspar Martins Pinto, Leonor', 
'González González, Ignacio Israel', 
'González Sanhueza, Nicolás Jesús', 
'Gonzalez Villarroel, Sebastian Ignacio', 
'Gutiérrez Rosa, Flavia Marjorie de Stephane', 
'Guzmán Soto, Martín Andrés', 
'Hidalgo González, Constanza Margarita', 
'Ibarra Godoy, Andrea Betzabé', 
'Jaccard Gutiérrez, Andree Michel', 
'Jara Murillo, Cristian Ignacio', 
'Jorquera Fajardo, Benjamín Ignacio', 
'Lafquén Cárdenas, Joaquín Andrés', 
'Lamich Bernales, Daniel', 
'Landaeta Riquelme, Antonia Paz', 
'Laura Colque, Camila Celeste del Carmen', 
'Leiva Valdivielso, Fernanda Antonia', 
'Lucero Oyarzún, Nicolás Santiago', 
'Matamala Vergara, Fabián Andrés', 
'Medina Venegas, Bastián Esteban', 
'Mella Peña, Matías Alejandro', 
'Messen Nicul, Felipe Alberto', 
'Miranda Reyes, Ximena María Francisca', 
'Molina Verdugo, Tomás Sebastián Salvador', 
'Mora Stavrakopulos, Francisco Nikolas', 
'Moreno Del Río, Agustín Alberto', 
'Moreno Muñoz, Janis Belén', 
'Mosciatti Recart, Fabrizio', 
'Muñoz Jimenez, Bruno Andres', 
'Muñoz Marín, Felipe Alejandro', 
'Muñoz Zuanic, María José', 
'Navarro Tapia, Leonardo Antonio', 
'Oñate Escobedo, Andrés Ignacio', 
'Ormeño Contreras, Tomás Patricio', 
'Oropesa Carreño, Antonia Belen', 
'Oyanadel Dreckmann, Sasha Nicolas', 
'Pacheco Cáceres, Damari Gabriela', 
'Palma Moena, Marcelo Iván', 
'Parra Osorio, Melanie Vanessa', 
'Perez Becerra, Jesus Alberto', 
'Pérez Díaz, Felipe Alonso', 
'Piña Carrasco, Javiera Catalina', 
'Pinochet Contreras, Javier Iván', 
'Pinto MagalhãEs, Carlota', 
'Ramírez Bórquez, Diego Ignacio', 
'Relos Ticuna, Tamara Isabel', 
'Reyes Nuñez, Valentina Sofía', 
'Riquelme Beltrami, Diego Alfonso', 
'Roa Henríquez, Alexia Valentina', 
'Roa Vásquez, Martín Orlando', 
'Rodríguez Cortés, Sofía María Anaís', 
'Rojas Solís, Benjamín Ignacio', 
'Romero López, Ema Luisa', 
'Rubina Andrade, Sebastián Eduardo', 
'Sánchez González, Francisca Esperanza', 
'Sánchez Olavarría, Cristian Alonso', 
'Sawady Lafferte, Diego Ignacio', 
'Sepúlveda Parada, Vania Constanza', 
'Sepúlveda Raglianti, Sofía Antonia', 
'Sifuentes Tasayco, Alvaro -', 
'Silva Pérez, Sebastián Andrés', 
'Silva Pino, Jazmín Ester', 
'Soto Jaramillo, Benjamín Jovany', 
'Tapia Durán, Sarai Alexandra', 
'Téllez Ávila, Antonia Ignacia', 
'Tobar Rojas, Charlot Zarella', 
'Torrejón Campusano, Alexandra Paola', 
'Torrejón Ordóñez, Isaac Patricio', 
'Torres Valdes, Nicole Estefania', 
'Torres Vasquez, Josefa Antonia', 
'Valencia Molina, Víctor Ignacio', 
'Valenzuela Durán, Matilde Catalina', 
'Valenzuela Landeros, José Ignacio', 
'Vallecillo Tamayo, Renata Isidora', 
'Vásquez Vargas, Sebastián Ignacio', 
'Vega López, Felipe Andrés', 
'Vidal Romero, Iván Mauricio', 
'Vildósola Urén, Vicente', 
'Villalobos Jiles, Tomás Domingo', 
'Villarreal Bustos, Iván Ignacio', 
'Villaseca Vicuña, Benjamín Ignacio Roberto', 
'Villegas Pardo, Pablo Simón', 
'Villouta Becerra, Nena Bernardita', 
'Vives Zañartu, Vicente', 
'Yañez Sanchez, Javiera Paz', 
'Zamorano Militzer, Diego', 
'Zapata Murillo, Javier Alberto', 
'Zapata Recabarren, Vicente Oscar',
'Otro nombre'
]


# Permitir al usuario seleccionar su nombre de una lista desplegable
nombre_seleccionado = st.selectbox('Selecciona tu nombre:', nombres)

# Función para limpiar el nombre
def limpiar_nombre(nombre):
    nombre_limpio = unidecode.unidecode(nombre)  # Quita las tildes
    nombre_limpio = nombre_limpio.replace(' ', '')  # Quita los espacios
    nombre_limpio = ''.join(e for e in nombre_limpio if e.isalnum())  # Quita caracteres especiales
    return nombre_limpio.lower()

# Genera el enlace para Qualtrics con el nombre limpio
if nombre_seleccionado:
    nombre_limpio = limpiar_nombre(nombre_seleccionado)
#    enlace_qualtrics = f"https://uchiledii.qualtrics.com/jfe/form/SV_0kTBR8a2mcMeXoq?nombre={nombre_limpio}"
#    enlace_qualtrics = f"https://uchiledii.qualtrics.com/jfe/form/SV_ezLq4FfZGxgHTVQ?nombre={nombre_limpio}"
#    enlace_qualtrics = f"https://uchiledii.qualtrics.com/jfe/form/SV_d4pynkPt0TcWkLA?nombre={nombre_limpio}"
    enlace_qualtrics = f"https://uchiledii.qualtrics.com/jfe/form/SV_6Xa7fwTeWgGo4Rw?nombre={nombre_limpio}"

    
    st.write(f'Tu enlace personalizado para la encuesta es: {enlace_qualtrics}')




    
    

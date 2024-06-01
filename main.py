import tkinter as tk # interfaz grafica
import pyttsx3 # pyttsx3 es una biblioteca de Python que nos permite convertir texto a voz. 
import pygame # lo use para cargar la musica de fondo 
import random # lo use para que los chistes y colmos corran aleatoriamente y no todos juntos.
import os  # 

"""el módulo os es una biblioteca estándar que proporciona una interfaz para interactuar con el sistema operativo en el que se ejecuta el programa. 
Permite realizar operaciones relacionadas con la gestión de archivos, directorios, rutas, variables de entorno y otras funcionalidades del sistema operativo."""


AroAro = [
    "Arriba de una gallina suspiraba un gallo criollo y en el suspiro decía: .......listo el pollo",
    "Ayer pase por tu casa y me tiraste con un corpiño,  ..... tirame con lo de adentro que lo agarro con mas cariño",
    "Ayer pasé por tu casa y me gritaste te adoro, pensaba que era tu hermano ¡Pero era tu feo loro!",
    "Ayer pase por tu casa y me tiraste con un balde de agua sucia .....suerte que me agache! ... ¡no contaban con mi astucia!",
    "Ayer pasé por tu casa y me tiraste una flor..... ¡La próxima vez sin maceta, por favor",
    "En la punta de aquel cerro suspiraba un perro mudo y en el suspiro decía: ..... Nada, porque era mudo",
    "Ayer pasé por tu casa y me tiraste un bidé. ¿Viste que no eras rubia?. ¡Adiviná qué encontré!"
]

chistes_verdes = [
    "¿Cuál es el último animal que subió al arca de Noé? ...El delfin",
    "¿Cuál es el animal más antiguo? La cebra, ¡porque está en blanco y negro!",
    "¿Qué le dice un semáforo a otro semáforo? No me mires, que me estoy cambiando.",
    "¿Cómo se dice psicoanalista en japonés? ..Sakudo Tukoko",
    "¿Por qué las focas del circo siempre miran para arriba? .. Porque allí es donde están los focos",
    "¡Mozo dice, este churrasco tiene muchos nervios. Es normal, será la primera vez que se lo van a comer.",
    "Un pez le pregunta a otro pez: ¿qué hace tu mamá? Este le contesta: Nada, ¿y la tuya qué hace? Nada también.",
    "Si se muere una pulga, ¿a dónde va? Al pulgatorio.",
    "¿Cómo se dice pelo sucio en chino? Chin cham pu.",
    "Mamá, mamá, ¿sabías que Juana de Arco era drogadicta? La mamá le mire y le dice: ¿Pero qué dices? Eso no es cierto. Que sí, mamá, en el libro pone que murió por heroína.",
    "¿Qué le dice un jardinero a otro? Nos vemos cuando podamos.",
    "El otro día vendí mi aspiradora. Lo único que hacía era acumular polvo.",
    "¿Cómo se despiden los químicos? Ácido un placer.",
    "¿Cómo se llama el campeón de buceo japonés? Tokofondo.",
    "¿Cómo se llama hacer dieta en chino? Kita Kilito.",
    "Mamá, en el cole me llaman enchufado. ¿Y tú que les dices? -¡Les sigo la corriente!",
    "Mamá, mamá, en el cole me llaman detective. ¿Y tú que les dices, Jaimito? -Silencio, aquí las preguntas las hago yo.",
    "En clase de psicología, una maestra les dice a sus alumnos: A ver, quien crea que es tonto y no sepa nada, que se ponga de pie. Después de unos minutos de silencio, Jaimito se levanta. -Jaimito, ¿crees que eres tonto? Le pregunta la maestra. - No profe, pero me da pena ver que solo tú estás de pie",
    "A ver Jaimito, dime dos pronombres. ¿Quien, yo? -¡Muy bien!",
    "¿Qué hace un mudo bailando? Una mudanza.",
    "Hola, busco trabajo ... ¿Le interesa de jardinero? ¿Dejar dinero? ¡Si lo que busco es trabajo!",
    "¿Qué le dice una impresora a otra? ... Esta hoja es tuya o es impresión mía.",
    "¿Y qué le dice una morsa a otra morsa? ¿Almorsamos o qué?",
    "¿Y qué le dice un pato a otro pato con el que estaba compitiendo en una carrera? Hemos empatado.",
    "Cariño, estás obsesionado con el fútbol y me haces falta. ¿Qué dices? ¿Cómo que falta? ¡Pero si ni te he tocado!",
    "¿Qué hace una vaca con los ojos cerrados? Leche concentrada.",
    "¿Por qué la luna es más grande que el sol? Porque la dejan salir de noche.",
    "¿Por qué los gatos no van al baile? Porque les asusta el perreo.",
    "¿Qué pasa si tiras un pato al agua? Nada.",
    "Qué mal me caen los químicos: los sodio",
    "Ayer me caí y pensé que me había roto el peroné. Peronó.",
    "¿Por qué la gallina cuida tanto a sus pollitos? Porque le costó un huevo tenerlos.",
    "Me sacaron del grupo de WhatsApp de paracaidismo. Se ve que no caía bien."
        
]

colmos = [
    "¿Cuál es el colmo de un jardinero? .... Que su hija se llame Flor y su mujer Rosa le deje plantado.",
    "¿Cuál es el colmo de un nadador? ... Ahogarse en un vaso de agua.",
    "¿Cuál es el colmo de un relojero? ... Perder el tiempo.",
    "¿Cuál es el colmo de un electricista? ... Que su esposa se llame Luz y sus hijos le sigan la corriente.",
    "¿Cuál es el colmo de un sordo? ... Que al morir le dediquen un minuto de silencio.",
    "¿Cuál es el colmo de un calvo? ... Tener ideas descabelladas.",
    "¿Cuál es el colmo de un astronauta? ... Enfermarse de gravedad.",
    "¿Cuál es el colmo de un fotógrafo? ... No poder revelarle sus secretos a nadie.",
    "¿Cuál es el colmo mas pequeño? ..El colmillo.",
    "¿Cuál es el colmo de un gallo? ... Que se le ponga la piel de gallina?",
    "¿Cuál es el colmo de un bombero? ... Tener una mujer ardiente.",
    "¿Cuál es el colmo de un músico? ... Perder el conocimiento y en lugar de volver en sí, volver en do.",
    "¿Cuál es el colmo de Aladdín? Tener mal genio.",
    "¿Cuál es el colmo de un puerco espín? Que le dé mala espina.",
    "¿Cuál es el colmo de un constructor? Llamarse Armando Torres",
    "¿Cuál es el colmo de un robot? Tener nervios de acero.",
    "¿Cuál es el colmo de un astronauta? Tener una esposa lunática.",
    "¿Cuál es el colmo de un astrónomo? Enamorarse de una estrella de cine.",
    "¿Cuál es el colmo de un gato? Tener un día de perros.",
    "¿Cuál es el colmo de un matemático? Tener cálculos en la vesícula.",
    "¿Cuál es el colmo de un carpintero? Tener una hija cómoda.",
    "¿Cuál es el colmo de un policía? Tener dos esposas.",
    
]


chistes_de_gallegos = [
    "Un gallego le dice a otro:...Oye Manolo pásame otro shampoo ... Pero si ahí en el baño hay uno ... Si hombre, pero este es para cabello seco y ...  yo ya me lo he mojado",
    "Varios astronautas se reúnen en la NASA.... Un ruso dice: Nosotros enviaremos un cohete a Mercurio, para estudiar la atmósfera de ese planeta ... Uno de USA dice: Nosotros enviaremos un radar a la Luna para estudiar el interior de este satélite. Y un gallego dice: Nosotros enviaremos un cohete al Sol... En ese momento todos dicen: ¡Pero el cohete, al acercarse al Sol, se derretirá!... Y el Gallego responde: ... Bueno, no vamos a ser tan brutos como para ir de día...",
    "¿Por qué los gallegos se sientan en la última fila cuando van a ver películas cómicas?... porque el que ríe último, ríe mejor",
    "¿Para qué los gallegos le ponen azúcar a la almohada?... para tener dulces sueños.",
    "¿Por qué los gallegos van al supermercado desnudos?... porque afuera hay un anuncio que dice 50 porciento de descuento en pelotas.",
    "Un gallego le dice al otro: - Oye Manolo, ¿sabías que David mató a Goliat con su onda? - Coño! sabía que ese gilipollas era un peligro con esa moto.",
    "Un niño gallego le pregunta a su padre: - Papá, ¿donde están los Andes? -Pues, pregúntale a tu madre que es ella la que guarda todo.",
    "Un gallego le dice al otro: - Oye Manolo, ¿te enteraste que se murió Paco? - Coño! ¿pero como sucedió?! - Fue a tirar el cigarrillo por el balcón y olvidó soltarlo.",
    "José como te fue ayer con el apagón? Deja, dos horas encerrado en el ascensor. Eso no es nada, yo estuve cuatro en la escalera mecánica...",
    "¿Qué hacen 50 gallegos en una farmacia? Van a comprar desodorante en barra.",
    "¿Que hace un gallego corriendo alrededor de una universidad?...una carrera universitaria.",
    "¿Por qué un gallego mira fijamente el cartón de jugo?...porque tenía escrito - concentrado",
    "A un gallego lo detiene la policía y le dice:- Deme su nombre y apellido.- Esta Usted loco, y yo después cómo me llamo ?",
    "Qué sale de un gallego y una pecosa?... un dado.",
    "Oye Manolo, te invito a una fiesta de 15 años.- Bueno, pero yo a los tres meses me vuelvo.",
    "Mira Manolo, me compré un reloj... ¿Qué marca? - Pues la hora, hombre.",
    "Qué sale de un gallego y una pelirroja?... un ladrillo.",
    "Cómo enfrían los gallegos el té?... le quitan el saquito.",
    "Por qué los gallegos se tapan los ojos cuando se ponen crema?...porque es nívea.",
    "Un gallego pide una pizza a domicilio y le preguntan:-En cuántos pedazos quiere que la cortemos? 6 o 12?- Hombre, pues 6 nada más, yo no me como tantos.",
    "Oye, Manolo... dime cuántos grados marca el termómetro... - Cero grados.- Qué bueno, hombre... Ni frio, ni calor.",
    "Entra un gallego con un perico a un bar, y el cantinero pregunta:-Habla el animal?- Y yo qué sé? - respondió el perico.",
    "Un helicóptero se ha estrellado en el cementerio de Galicia... la policía local informa que se han encontrado más de 3 mil cuerpos." 
    
]



audio = pyttsx3.init() # iniciar motor de audio

# Funciónes para contar aros aros, chistes, colmos
def contar_chiste():
    chiste = random.choice(AroAro) # devuelve una eleccion aleatoria de los chistes, aro o colmos
    print(chiste)
    audio.say(chiste) # decir
    audio.runAndWait() # corre y espera
    
def divertite():
    chisteverde = random.choice(chistes_verdes)
    print(chisteverde)
    audio.say(chisteverde)
    audio.runAndWait()
    
def colmoscolmos():
    colmo1 = random.choice(colmos)
    print(colmo1)
    audio.say(colmo1)
    audio.runAndWait()

def gallegos():
    chistesgallegos = random.choice(chistes_de_gallegos)
    print(chistesgallegos)
    audio.say(chistesgallegos)
    audio.runAndWait()


# Crear la ventana principal
ventana = tk.Tk()
ventana.config(bg="DarkBlue")  # cambiar el color de fondo de la ventana
ventana.title("Aros Aros de Salon")
ventana.geometry("800x600")
ventana.resizable(1, 1) # ajuste de ventana

#imagenes de fondo 
img = tk.PhotoImage(file="imagen3.png")
lbl_img = tk.Label(ventana,image = img)
lbl_img.pack() #control para que aparezca el widget
lbl_img.place(x=400, y=50) 

imgen2 = tk.PhotoImage(file="comedia.png")
lbl_img2 = tk.Label(ventana,image = imgen2)
lbl_img2.place(x=800, y=400)

imgen3 = tk.PhotoImage(file="perritomalvado.png")
lbl_img3 = tk.Label(ventana,image = imgen3)
lbl_img3.place(x=1200, y=50)  


# Inicializar Pygame y cargar la música
pygame.init()
pygame.mixer.init() #carga el archivo de musica para reproducirlo


# Ruta del archivo de audio
audio_file = r"C:\Users\Francisco Flores\Documents\TRABAJO FINAL PYTHON\chiste.wav"

# Verificar si el archivo de música existe
if not os.path.isfile(audio_file):   #prueba la ruta y el archivo
    print(f"Error No se encontró el archivo de audio '{audio_file}'")
else:
    try: 
        pygame.mixer.music.load(audio_file) #llama a la ruta
        pygame.mixer.music.set_volume(0.05)  # Ajusta el volumen entre 0.0 y 1.0
        pygame.mixer.music.play(-1) #-1 para que no se detenga
        print(f"Reproduciendo {audio_file}")
    except pygame.error as e:
        print(f"Error al cargar el archivo de audio: {e}")
 
 #Titulo       
titulo = tk.Label(ventana, text="SHOW DEL HUMOR", font=("Helvetica", 24), bg="blue", fg="white") #fuente Helvetica
titulo.pack(pady=20)

#botones
boton_aros = tk.Button(ventana, text="Escuchar Aro Aro", command=contar_chiste,bg="orange", fg="black", font=("Helvetica", 14))
boton_aros.pack(pady=20)

boton_chistes = tk.Button(ventana, text="Escuchar chistes verdes", command=divertite, bg="green", fg="white", font=("Helvetica", 14))
boton_chistes.pack(pady=20)

boton_colmos = tk.Button(ventana, text="Escuchar colmos", command=colmoscolmos, bg="red", fg="white", font=("Helvetica", 14))
boton_colmos.pack(pady=20)

boton_gallegos = tk.Button(ventana, text="Eschar chistes gallegos", command=gallegos, bg="purple", fg="white", font=("Helvetica", 14))
boton_gallegos.pack(pady=20)


ventana.mainloop()

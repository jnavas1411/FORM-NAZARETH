from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.spinner import MDSpinner
from kivy.properties import StringProperty
import os, cryptocode, requests
import gdown
import threading
import time
# juyawasa jujutaliaka jia einjatka wanepia julu maima
KV = """
#:kivy 2.0
#: import SlideTransition kivy.uix.screenmanager.SlideTransition
#: import RiseInTransition kivy.uix.screenmanager.RiseInTransition
#-------------------------------------------------------------------------------------
<ElementCard@MDCard>:
    md_bg_color: 239/255, 239/255, 239/255, 1
    radius: '10dp'
    spacing: '10dp'
    paddin: '10dp'
    elevation: 3
    image: ''
    text: ''
    orientation: 'vertical'
    ripple_behavior: True
    on_release:
        app.root.transition = RiseInTransition()
    Image:
        source: root.image
    MDBoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: root.text
            halign: 'center'
#-------------------------------------------------------------------------------------
<Un_Texto@MDLabel>:
    text: ''
    markup: True
    font_size:
    adative_height: True
    bold: True
#-------------------------------------------------------------------------------------
<Cajas_De_Texto@MDTextField>
    elevation: 3
    id: ''
    hint_text: ''
    line_color_focus: 239/255, 239/255, 239/255, 1
    line_color_normal: 239/255, 239/255, 239/255, 1
    hint_text_color_focus: '039200'
    text_color_focus: '039200'
    mode: 'rectangle'
#-------------------------------------------------------------------------------------
<Botones_General@MDRaisedButton>
    md_bg_color: '039200'
#-------------------------------------------------------------------------------------
<Pagina_Principal>:
    MDScreen:
        name: 'pagina_waneshia'
        md_bg_color: 239/255, 239/255, 239/255, 1
        MDBoxLayout:
            orientation: 'vertical'
            padding: 30
            MDBoxLayout
                size_hint: 1, 0.4
                MDBoxLayout:
                    orientation: 'vertical'
                    MDBoxLayout:
                        size_hint: 1, 0.6
                        orientation: 'horizontal'
                        MDBoxLayout:
                            size_hint: 0.9, 1
                            Image:
                                source: 'anajaikai/juyakua/HeliosESP.png'
                        MDBoxLayout:
                            size_hint: 0.1, 1
                            MDIconButton:
                                icon: 'exit-to-app'
                                pos_hint: {'top': 1, 'right': 1}
                                icon_color: 'gray'
                                on_release:
                                    root.Cerrar_Aplicacion()
                    MDBoxLayout:
                        size_hint: 1, 0.4
                        Un_Texto:
                            text: 'Bienvenido'
                            font_size: 35
                            halign: 'center'
                            color: '039200'
            MDBoxLayout:
                size_hint: 1, 0.4
                MDBoxLayout:
                    orientation: 'vertical'
                    MDBoxLayout:
                        size_hint: 1, 0.3
                        Cajas_De_Texto:
                            id: text_field_usuario
                            hint_text: 'Usuario'
                    MDBoxLayout:
                        size_hint: 1, 0.3
                        Cajas_De_Texto:
                            id: text_field_contrasena
                            hint_text: 'Contraseña'
                            password: True
                        MDIconButton:
                            icon: "eye-off"
                            on_release:
                                self.icon = "eye" if self.icon == "eye-off" else "eye-off"
                                text_field_contrasena.password = False if text_field_contrasena.password is True else True
                    MDBoxLayout:
                        size_hint: 1, 0.1
                        Un_Texto:
                            text: '¿Olvidaste tu contraseña?'
                            font_size: 15
                            halign: 'right'
                            color: '039200'
                    MDBoxLayout:
                        size_hint: 1, 0.3
                        Botones_General:
                            size_hint_x: 1
                            on_release:
                                x = root.Boton_Ingresar()
                                root.current = 'pagina_piama' if x == True else None
                            Un_Texto:
                                text: 'Iniciar Sesión'
                                halign: 'center'
                                color: 'white'
                                font_size: 20
            MDBoxLayout:
                size_hint: 1, 0.2
                orientation: 'vertical'
                MDBoxLayout:
                    size_hint: 1, 0.4
                    Un_Texto:
                        text: 'Síguenos en:'
                        font_size: 25
                        halign: 'center'
                        color: '039200'
                MDBoxLayout:
                    size_hint: 1, 0.6
                    MDBoxLayout:
                        orientation: 'horizontal'
                        MDBoxLayout:
                            MDIconButton:
                                icon: 'facebook'
                                theme_icon_color: 'Custom'
                                icon_color: 'blue'
                                size_hint: .5, 1
                                on_release:
                                    root.Cuadro_de_Spinner()
                        MDBoxLayout:
                            MDIconButton:
                                size_hint: .5, 1
                                icon: 'twitter'
                                theme_icon_color: 'Custom'
                                icon_color: '#00acee'
                        MDBoxLayout:
                            MDIconButton:
                                size_hint: .5, 1
                                icon: 'instagram'
                                theme_icon_color: 'Custom'
                                icon_color: '#3f729b'
                        MDBoxLayout:
                            MDIconButton:
                                size_hint: .5, 1
                                icon: 'help'
                                theme_icon_color: 'Custom'
                                icon_color: 'black'
                                #botonayuda----------------------------------------------------
                                on_release:
                                    x_ayuda = root.Boton_Ayuda()
                                    root.current = 'pagina_apunuin' if x_ayuda == False else None
        
    MDScreen:
        name: 'pagina_piama'
        MDBoxLayout:
            orientation: 'vertical'
            MDBoxLayout:
                size_hint: 1, 0.1
                orientation: 'horizontal'
                padding: 20
                MDBoxLayout:
                    size_hint: 0.9, 1
                    Un_Texto:
                        text: root.nombre_usuario_actual
                    Un_Texto:
                        id: tipo_de_usuario
                        text: root.tipo_usuario_actual
                        color: 239/255, 239/255, 239/255, 1
                MDBoxLayout:
                    size_hint: 0.1, 1
                    MDIconButton:
                        icon: 'close'
                        size_hint: 1,1
                        on_release:
                            root.Cerrar_Sesion()
            MDGridLayout:
                cols: 2
                size_hint: 1, 0.9
                padding: ['10dp','10dp','10dp','10dp']
                spacing: '10dp'
                ElementCard:
                    text: 'Ingresar Lectura de Medidor'
                    image: 'anajaikai/juyakua/ordenes.png'
                    on_release:
                        root.current = 'pagina_facturacion' if tipo_de_usuario.text == '2' else None
                ElementCard:
                    text: 'Creacion de Órdenes'
                    image: 'anajaikai/juyakua/crear.png'
                ElementCard:
                    text: 'Trabajo Actual'
                    image: 'anajaikai/juyakua/trabajo.png'
                ElementCard:
                    text: 'Entidades'
                    image: 'anajaikai/juyakua/entidades.png'
                ElementCard:
                    text: 'Estadisticas'
                    image: 'anajaikai/juyakua/estadisticas.png'
                ElementCard:
                    text: 'Descargas'
                    image: 'anajaikai/juyakua/descargas.png'
                ElementCard:
                    text: 'Mapas'
                    image: 'anajaikai/juyakua/mapas.png'
                ElementCard:
                    text: 'Atencion al Cliente'
                    image: 'anajaikai/juyakua/whatsapp.png'
                ElementCard:
                    text: 'Administración'
                    image: 'anajaikai/juyakua/admin.png'
                    on_release:
                        root.current = 'pagina_aluwatawa' if tipo_de_usuario.text == '1' else None
    MDScreen:
        name: 'pagina_facturacion'
        MDBoxLayout:
            orientation: 'vertical'
            MDBoxLayout:
                size_hint: 1, 0.1
                padding: 20
                orientation: 'horizontal'
                MDBoxLayout:
                    size_hint: 0.9, 1
                    Un_Texto:
                        text: root.nombre_usuario_actual
                    Un_Texto:
                        id: tipo_de_usuario
                        text: root.tipo_usuario_actual
                        color: 239/255, 239/255, 239/255, 1
                MDBoxLayout:
                    size_hint: 0.1, 1
                    MDIconButton:
                        icon: 'close'
                        size_hint: 1,1
                        on_release:
                            root.current = 'pagina_piama'
                            root.limpieza_pagina_piama()
            MDBoxLayout:
                size_hint: 1, 0.9
                padding: 20
                MDBoxLayout:
                    orientation: 'vertical'
                    MDBoxLayout:
                        orientation: 'vertical'
                        size_hint: 1, 0.2
                        MDBoxLayout:
                            size_hint: 1, 0.3
                            Un_Texto:
                                text: 'Consultar Usuario'
                                halign: 'center'
                        MDBoxLayout:
                            size_hint: 1, 0.7
                            orientation: 'horizontal'
                            MDBoxLayout:
                                size_hint: 0.3, 1
                                Un_Texto:
                                    text: 'Cédula o ID Usuario'
                                    font_size: 15
                                    halign: 'center'
                            MDBoxLayout:
                                size_hint: 0.4, 1
                                Cajas_De_Texto:
                                    id: criterio_busqueda_usuario
                                    hint_text: 'Ingrese CC o ID usuario'
                            MDBoxLayout:
                                size_hint: 0.3, 1
                                Botones_General:
                                    size_hint: 1, 0.8
                                    on_release:
                                        root.Busqueda_Entidad()
                                    Un_Texto:
                                        text: 'Buscar'
                                        font_size: 20
                                        halign: 'center'
                                        color: 'white'


                    MDBoxLayout:
                        size_hint: 1, 0.4
                        MDBoxLayout:
                            orientation: 'horizontal'
                            MDBoxLayout:
                                orientation: 'vertical'
                                size_hint: 0.25, 1
                                Un_Texto:
                                    text: 'Comunidad: '
                                    font_size: 15
                                    halign: 'right'
                                    bold: False
                                    italic: True
                                Un_Texto:
                                    text: 'ID: '
                                    font_size: 15
                                    halign: 'right'
                                    bold: False
                                    italic: True
                                Un_Texto:
                                    text: 'Usuario: '
                                    font_size: 15
                                    halign: 'right'
                                    bold: False
                                    italic: True
                                Un_Texto:
                                    text: 'Cedula: '
                                    font_size: 15
                                    halign: 'right'
                                    bold: False
                                    italic: True
                                Un_Texto:
                                    text: 'Dirección: '
                                    font_size: 15
                                    halign: 'right'
                                    bold: False
                                    italic: True
                                Un_Texto:
                                    text: 'Mes: '
                                    font_size: 15
                                    halign: 'right'
                                    bold: False
                                    italic: True
                                Un_Texto:
                                    text: 'Lectura: '
                                    font_size: 15
                                    halign: 'right'
                                    bold: False
                                    italic: True
                                Un_Texto:
                                    text: 'Mes: '
                                    font_size: 15
                                    halign: 'right'
                                    bold: False
                                    italic: True
                                Un_Texto:
                                    text: 'Lectura: '
                                    font_size: 15
                                    halign: 'right'
                                    bold: False
                                    italic: True
                                Un_Texto:
                                    text: 'Mes: '
                                    font_size: 15
                                    halign: 'right'
                                    bold: False
                                    italic: True
                                Un_Texto:
                                    text: 'Lectura: '
                                    font_size: 15
                                    halign: 'right'
                                    bold: False
                                    italic: True

                            MDBoxLayout:
                                orientation: 'vertical'
                                size_hint: 0.75, 1
                                Un_Texto:
                                    text: root.dato_vereda_usuario
                                    font_size: 15
                                    halign: 'left'
                                    italic: True
                                Un_Texto:
                                    text: root.dato_id_usuario
                                    font_size: 15
                                    halign: 'left'
                                    italic: True
                                Un_Texto:
                                    text: root.dato_nombre_usuario
                                    font_size: 15
                                    halign: 'left'
                                    italic: True
                                Un_Texto:
                                    text: root.dato_cedula_usuario
                                    font_size: 15
                                    halign: 'left'
                                    italic: True
                                Un_Texto:
                                    text: root.dato_direccion_usuario
                                    font_size: 15
                                    halign: 'left'
                                    italic: True
                                Un_Texto:
                                    text: root.dato_mesAP_usuario
                                    font_size: 15
                                    halign: 'left'
                                    italic: True
                                Un_Texto:
                                    text: root.dato_lecturaAP_usuario
                                    font_size: 15
                                    halign: 'left'
                                    italic: True
                                Un_Texto:
                                    text: root.dato_mesP_usuario
                                    font_size: 15
                                    halign: 'left'
                                    italic: True
                                Un_Texto:
                                    text: root.dato_lecturaP_usuario
                                    font_size: 15
                                    halign: 'left'
                                    italic: True
                                Un_Texto:
                                    text: root.dato_mesU_usuario
                                    font_size: 15
                                    halign: 'left'
                                    italic: True
                                Un_Texto:
                                    text: root.dato_lecturaU_usuario
                                    font_size: 15
                                    halign: 'left'
                                    italic: True
                    MDBoxLayout:
                        md_bg_color: 'red'
                        size_hint: 1, 0.4

    MDScreen:
        name: 'pagina_apunuin'
        md_bg_color: 239/255, 239/255, 239/255, 1
        MDBoxLayout:
            orientation: 'vertical'
            padding: 30
            MDBoxLayout:
                orientation: 'vertical'
                MDBoxLayout:
                    orientation: 'vertical'
                    MDBoxLayout:
                        size_hint: 1, 0.8
                        Image:
                            source: 'anajaikai/juyakua/HeliosESP.png'
                    MDBoxLayout:
                        size_hint: 1, 0.2
                        Un_Texto:
                            text: 'Ingrese su configuración'
                            font_size: 30
                            halign: 'center'
                            color: '039200'
                MDBoxLayout:
                    orientation: 'vertical'
                    MDBoxLayout:
                        Cajas_De_Texto:
                            id: text_field_configuracion 
                            hint_text: 'Ingrese su configuracion'
                    MDBoxLayout:
                        Botones_General:
                            size_hint_x: 1
                            on_release:
                                x_configuracion = root.Ingreso_Configuracion()
                                root.current = 'pagina_waneshia' if x_configuracion == True else None
                            Un_Texto:
                                text: 'Aceptar'
                                halign: 'center'
                                color: 'white'
                                font_size: 20
                    MDBoxLayout:
                        Botones_General:
                            size_hint_x: 1
                            on_release:
                                root.current = 'pagina_waneshia'
                            Un_Texto:
                                text: 'Volver'
                                halign: 'center'
                                color: 'white'
                                font_size: 20
                MDBoxLayout:
                    Image:
                        source: 'anajaikai/juyakua/esperando.png'
    MDScreen:
        name: 'pagina_aluwatawa'
        md_bg_color: 239/255, 239/255, 239/255, 1
        MDBoxLayout:
            orientation: 'vertical'
            padding: 20
            MDBoxLayout:
                size_hint: 1, 0.1
                orientation: 'horizontal'
                MDBoxLayout:
                    size_hint: 0.9, 1
                    Un_Texto:
                        text: root.nombre_usuario_actual
                    Un_Texto:
                        id: tipo_de_usuario
                        text: root.tipo_usuario_actual
                        color: 239/255, 239/255, 239/255, 1
                MDBoxLayout:
                    size_hint: 0.1, 1
                    MDIconButton:
                        icon: 'close'
                        size_hint: 1,1
                        on_release:
                            root.current = 'pagina_piama'
            MDBoxLayout:
                size_hint: 1, 0.9
                MDBoxLayout:
                    orientation: 'vertical'
                    Un_Texto:
                        text: 'Registrar un Usuario'
                        halign: 'center'
                    Cajas_De_Texto:
                        id: text_field_tipo_usuario
                        hint_text: 'Tipo Usuario'
                        max_text_length: 1
                    Cajas_De_Texto:
                        id: text_field_nombres_y_apellidos_usuario
                        hint_text: 'Nombres y Apellidos'
                    Cajas_De_Texto:
                        id: text_field_cedula_usuario
                        hint_text: 'Número de Cédula'
                    Cajas_De_Texto:
                        id: text_field_usuario_usuario
                        hint_text: 'Usuario'
                    Cajas_De_Texto:
                        id: text_field_contrasena_usuario
                        hint_text: 'Contraseña'
                    Botones_General:
                        size_hint_x: 1
                        on_release:
                            root.guardar_datos_nuevo_usuario()
                        Un_Texto:
                            text: 'Guardar Datos'
                            halign: 'center'
                            color: 'white'
                            font_size: 20


"""
#------------------------------------------------------------------------------
# CUADRO DE ALERTA
#------------------------------------------------------------------------------
def cuadro_de_alerta(self, b):
    btn_cerrar = MDFlatButton(text="Aceptar", theme_text_color="Custom", on_release=self.cerrar)
    self.dialogbox = MDDialog(text=b, buttons=[btn_cerrar])
    self.dialogbox.open()
#ARRIBA CUADRO DE ALERTA
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# DECARGAR ARCHIVO DE GOOGLE
#------------------------------------------------------------------------------
def descargar_archivo_google(url, id_archivoka):
    gdown.download(url+id_archivoka, output='./anajaikai/maima/jujutaliaka.txt')
#ARRIBA DESCARGAR ARCHIVO DE GOOGLE
#------------------------------------------------------------------------------

class Pagina_Principal(ScreenManager):
    nombre_usuario_actual = StringProperty('')
    tipo_usuario_actual = StringProperty('')
    #------------------------------------------------------------------------------
    #------------------------------------------------------------------------------
    # DATOS DE USUARIOS Y O ENTIDADES
    #------------------------------------------------------------------------------
    dato_vereda_usuario = StringProperty('')
    dato_id_usuario = StringProperty('')
    dato_nombre_usuario = StringProperty('')
    dato_cedula_usuario = StringProperty('')
    dato_direccion_usuario = StringProperty('')
    dato_mesAP_usuario = StringProperty('')
    dato_lecturaAP_usuario = StringProperty('')
    dato_mesP_usuario = StringProperty('')
    dato_lecturaP_usuario = StringProperty('')
    dato_mesU_usuario = StringProperty('')
    dato_lecturaU_usuario = StringProperty('')
    #-------------------------------------------------------------------------------
    # INGRESO CONFIGURACION
    #------------------------------------------------------------------------------
    def Ingreso_Configuracion(self):
        estado_configuracion = False
        if self.ids['text_field_configuracion'].text == "" or len(list(self.ids['text_field_configuracion'].text)) != 7:
            cuadro_de_alerta(self, "Debe ingresar una configuración válida")
            self.ids['text_field_configuracion'].text = ""
        else:
            texto = list(self.ids['text_field_configuracion'].text)
            if texto[0].upper() == "U" and int(texto[3]) == 1 and texto[6].upper() == "G":
                # aqui comienza la conexion a internet
                try:
                    request = requests.get("https://www.google.com.co/", timeout=5)
                except (requests.ConnectionError, requests.Timeout):
                    cuadro_de_alerta(self, "Debe conectarse a internet")
                else:
                    x = "HD364"+"".join(texto).upper()+"TE54F"
                    archivo = open('anajaikai/maima/ekerrotia.txt', 'w')
                    archivo.write(x)
                    archivo.write("\n")
                    archivo.close()
                    self.ids['text_field_configuracion'].text = ""
                    if os.path.isfile('./anajaikai/maima/juyawasa_jujutaliaka.txt') == True:
                        archivo_juyawasa = open('./anajaikai/maima/juyawasa_jujutaliaka.txt', 'r')
                        lectura_juyawasa = archivo_juyawasa.read().split("\n")[:-1]
                        archivo_jujutalia = open('./anajaikai/maima/ekerrotia.txt', 'r')
                        lectura_jujutalia = archivo_jujutalia.read().split("\n")[:-1]
                        llave_jujutalia = "".join(list("".join(lectura_jujutalia))[5:12])
                        llave_juyawasa = "".join(lectura_juyawasa)
                        id_archivoka = cryptocode.decrypt(llave_juyawasa, llave_jujutalia)
                        url = 'https://drive.google.com/uc?/export=download&id='
                        t1 = threading.Thread(target=descargar_archivo_google, args = (url, id_archivoka))
                        t1.start()
                        contador = 0
                        while contador < 0:
                            if os.path.isfile('./anajaikai/maima/jujutaliaka.txt') == True:
                                break
                            time.sleep(3)
                            contador = contador + 1
                        estado_configuracion = True
                        cuadro_de_alerta(self, "Descarga completa")
                    else:
                        cuadro_de_alerta(self, "No existe el ID del archivo a descargar")
            else:
                cuadro_de_alerta(self, "Error configuración, favor verificar")
                self.ids['text_field_configuracion'].text = ""
        return estado_configuracion
    #ARRIBA INGRESO CONFIGURACION
    #------------------------------------------------------------------------------
    #------------------------------------------------------------------------------
    # CERRAR CUADRO DE ALERTA
    #------------------------------------------------------------------------------
    dialog = None
    def cerrar(self, obj):
        self.dialogbox.dismiss()
    #ARRIBA CERRAR CUADRO DE ALERTA
    #------------------------------------------------------------------------------
    #------------------------------------------------------------------------------
    # CERRAR LA APLICACION
    #------------------------------------------------------------------------------
    def Cerrar_Aplicacion(self):
        MDApp.get_running_app().stop()
        Window.close()
    #ARRIBA CERRAR LA APLICACION
    #------------------------------------------------------------------------------
    #------------------------------------------------------------------------------
    # BOTON DE AYUDA
    #------------------------------------------------------------------------------
    def Boton_Ayuda(self):
        estado_ayuda = False
        if os.path.isfile('anajaikai/maima/ekerrotia.txt') == True:
            estado_ayuda = True
        return estado_ayuda
    #ARRIBA BOTON DE AYUDA
    #------------------------------------------------------------------------------
    #------------------------------------------------------------------------------
    # BOTON INGRESAR
    #------------------------------------------------------------------------------
    def Boton_Ingresar(self):
        estado = False
        if os.path.isfile('anajaikai/maima/ekerrotia.txt') == True:
            if self.ids['text_field_contrasena'].text == "" or self.ids['text_field_usuario'].text == "":
                cuadro_de_alerta(self, "Debe ingresar usuario y/o contraseña")
                self.ids['text_field_contrasena'].text = ""
                self.ids['text_field_usuario'].text = ""
            else:
                datos = []
                lista_usuario = []
                lista_contras = []
                lista_nombres_usuarios = []
                lista_tipo_usuario = []
                archivo_ayatalika = open('anajaikai/maima/jujutaliaka.txt', 'r')
                lectura_ayatalika = archivo_ayatalika.read().split("\n")[:-1]
                archivo_jujutalia = open('./anajaikai/maima/ekerrotia.txt', 'r')
                lectura_jujutalia = archivo_jujutalia.read().split("\n")[:-1]
                llave_jujutalia = "".join(list("".join(lectura_jujutalia))[5:12])
                for i in lectura_ayatalika:
                    aux = []
                    for j in i.split(","):
                        aux.append(cryptocode.decrypt(j,llave_jujutalia))
                    datos.append(aux)
                for x in datos:
                    lista_tipo_usuario.append(x[0])
                    lista_nombres_usuarios.append(x[1])
                    lista_usuario.append(x[3])
                    lista_contras.append(x[4])
                self.usuario = self.ids['text_field_usuario'].text
                self.contrasena = self.ids['text_field_contrasena'].text
                if len([x for x in lista_usuario if x == self.usuario]) != 0:
                    usuario_encontrado = "".join([x for x in lista_usuario if x == self.usuario])
                    if usuario_encontrado == self.ids['text_field_usuario'].text and self.ids['text_field_contrasena'].text == lista_contras[lista_usuario.index(usuario_encontrado)]:
                        estado = True
                        cuadro_de_alerta(self, "Bienvenido")
                        self.ids['text_field_contrasena'].text = ""
                        self.ids['text_field_usuario'].text = ""
                        usuario_actual = lista_nombres_usuarios[lista_usuario.index(usuario_encontrado)]
                        tipo_usuario_actual_local = lista_tipo_usuario[lista_usuario.index(usuario_encontrado)]
                        self.nombre_usuario_actual = usuario_actual
                        self.tipo_usuario_actual = tipo_usuario_actual_local
                    else:
                        cuadro_de_alerta(self, "Usuario o contraseña errados")
                        self.ids['text_field_contrasena'].text = ""
                        self.ids['text_field_usuario'].text = ""

                else:
                    cuadro_de_alerta(self, "Usuario no existe")
                    self.ids['text_field_contrasena'].text = ""
                    self.ids['text_field_usuario'].text = ""
        else:
            cuadro_de_alerta(self, "Debe ingresar su codigo de configuración")
            self.ids['text_field_contrasena'].text = ""
            self.ids['text_field_usuario'].text = ""
        return estado        
    #ARRIBA BOTON INGRESAR
    #------------------------------------------------------------------------------
    #------------------------------------------------------------------------------
    # CUADRO DE DIALOGO
    #------------------------------------------------------------------------------
    def Cerrar_Sesion(self):
        btn_cancelar = MDFlatButton(text="Cancelar", theme_text_color="Custom", on_release=self.cerrar_dialogo)
        btn_aceptar = MDFlatButton(text="Aceptar", theme_text_color="Custom",  on_release=self.aceptar_salir)
        self.dialogbox = MDDialog(text="Realmente desea salir?", buttons=[btn_cancelar, btn_aceptar])
        self.dialogbox.open()
    #ARRIBA CUADRO DE DIALOGO
    #------------------------------------------------------------------------------
    def cerrar_dialogo(self, obj):
        self.dialogbox.dismiss()
    def aceptar_salir(self, *args):
        self.current = "pagina_waneshia"
        self.dialogbox.dismiss()
    #------------------------------------------------------------------------------
    # LIMPIEZA DE CASILLAS PAGINA PIAMA
    #------------------------------------------------------------------------------
    def limpieza_pagina_piama(self):
        self.dato_vereda_usuario = ''
        self.dato_id_usuario = ''
        self.dato_nombre_usuario = ''
        self.dato_cedula_usuario = ''
        self.dato_direccion_usuario = ''
        self.dato_mesAP_usuario = ''
        self.dato_lecturaAP_usuario = ''
        self.dato_mesP_usuario = ''
        self.dato_lecturaP_usuario = ''
        self.dato_mesU_usuario = ''
        self.dato_lecturaU_usuario = ''
    #------------------------------------------------------------------------------
    # ARRIBA LIMPIEZA DE CASILLAS
    ##------------------------------------------------------------------------------

    #------------------------------------------------------------------------------
    # CUADRO DE BUSQUEDA ENTIDAD
    #------------------------------------------------------------------------------
    def Busqueda_Entidad(self):
        if self.ids['criterio_busqueda_usuario'].text == "":
            cuadro_de_alerta(self, "Debe ingresar un codigo de usuario")
        else:
            meses = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV","DIC"]
            listado_vereda_usuario = []
            listado_id_usuario = []
            listado_nombre_usuario = []
            listado_cedula_usuario = []
            listado_direccion_usuario = []
            listado_mesAP_usuario = []
            listado_lecturaAP_usuario = []
            listado_mesP_usuario = []
            listado_lecturaP_usuario = []
            listado_mesU_usuario = []
            listado_lecturaU_usuario = []
            archivo_entidades = open('anajaikai/maima/entidades.txt', 'r')
            mensaje_entidades = archivo_entidades.read().split('\n')[:-1]
            for ids in mensaje_entidades:
                listado_vereda_usuario.append(ids.split(",")[0])
                listado_id_usuario.append(ids.split(",")[2])
                listado_nombre_usuario.append(ids.split(",")[3])
                listado_cedula_usuario.append(ids.split(",")[4])
                listado_direccion_usuario.append(ids.split(",")[5])
                listado_mesAP_usuario.append(ids.split(",")[6])
                listado_lecturaAP_usuario.append(ids.split(",")[7])
                listado_mesP_usuario.append(ids.split(",")[8])
                listado_lecturaP_usuario.append(ids.split(",")[9])
                listado_mesU_usuario.append(ids.split(",")[10])
                listado_lecturaU_usuario.append(ids.split(",")[11])
            if len([x for x in listado_id_usuario if x == self.ids['criterio_busqueda_usuario'].text]) !=0:
                cliente_encontrado = "".join([x for x in listado_id_usuario if x == self.ids['criterio_busqueda_usuario'].text])
                self.dato_vereda_usuario = (listado_vereda_usuario[listado_id_usuario.index(cliente_encontrado)])
                self.dato_id_usuario = (listado_id_usuario[listado_id_usuario.index(cliente_encontrado)])
                self.dato_nombre_usuario = (listado_nombre_usuario[listado_id_usuario.index(cliente_encontrado)])
                self.dato_cedula_usuario = (listado_cedula_usuario[listado_id_usuario.index(cliente_encontrado)])
                self.dato_direccion_usuario = (listado_direccion_usuario[listado_id_usuario.index(cliente_encontrado)])
                dato1 = (listado_mesAP_usuario[listado_id_usuario.index(cliente_encontrado)])
                self.dato_mesAP_usuario = meses[int(dato1.split("/")[1])-1]+"/"+dato1.split("/")[-1]
                self.dato_lecturaAP_usuario = (listado_lecturaAP_usuario[listado_id_usuario.index(cliente_encontrado)])
                dato2 = (listado_mesP_usuario[listado_id_usuario.index(cliente_encontrado)])
                self.dato_mesP_usuario = meses[int(dato2.split("/")[1])-1]+"/"+dato2.split("/")[-1]
                self.dato_lecturaP_usuario = (listado_lecturaP_usuario[listado_id_usuario.index(cliente_encontrado)])
                dato3 = (listado_mesU_usuario[listado_id_usuario.index(cliente_encontrado)])
                self.dato_mesU_usuario = meses[int(dato3.split("/")[1])-1]+"/"+dato3.split("/")[-1]
                self.dato_lecturaU_usuario = (listado_lecturaU_usuario[listado_id_usuario.index(cliente_encontrado)])
                self.ids['criterio_busqueda_usuario'].text = ''
            else:
                cuadro_de_alerta(self, "No existe ningún usuario con el codigo ingresado")
                self.ids['criterio_busqueda_usuario'].text = ''
                limpieza_pagina_piama()
        
    #ARRIBA BUSQUEDA ENTIDAD
    def guardar_datos_nuevo_usuario(self):
        if self.ids['text_field_tipo_usuario'].text == '' or self.ids['text_field_nombres_y_apellidos_usuario'].text == '' or \
            self.ids['text_field_cedula_usuario'].text == '' or self.ids['text_field_usuario_usuario'].text == '' or \
                self.ids['text_field_contrasena_usuario'].text == '':
                cuadro_de_alerta(self, "hay alguna celda vacia")
        else:
            datos_usuario_nuevo = []
            archivo_jujutalia = open('./anajaikai/maima/ekerrotia.txt', 'r')
            lectura_jujutalia = archivo_jujutalia.read().split("\n")[:-1]
            llave_jujutalia = "".join(list("".join(lectura_jujutalia))[5:12])
            datos_usuario_nuevo.insert(0,cryptocode.encrypt(self.ids['text_field_contrasena_usuario'].text,llave_jujutalia))
            datos_usuario_nuevo.insert(0,cryptocode.encrypt(self.ids['text_field_usuario_usuario'].text,llave_jujutalia))
            datos_usuario_nuevo.insert(0,cryptocode.encrypt(self.ids['text_field_cedula_usuario'].text,llave_jujutalia))
            datos_usuario_nuevo.insert(0,cryptocode.encrypt((self.ids['text_field_nombres_y_apellidos_usuario'].text).title(),llave_jujutalia))
            datos_usuario_nuevo.insert(0,cryptocode.encrypt(self.ids['text_field_tipo_usuario'].text,llave_jujutalia))
            datos_de_usuario_a_guardar = (",".join(datos_usuario_nuevo))
            archivo_datos_de_usuario_a_guardar = open('anajaikai/maima/jujutaliaka.txt', 'a+')
            archivo_datos_de_usuario_a_guardar.write(datos_de_usuario_a_guardar)
            archivo_datos_de_usuario_a_guardar.write("\n")
            archivo_datos_de_usuario_a_guardar.close()
            self.ids['text_field_tipo_usuario'].text = ''
            self.ids['text_field_nombres_y_apellidos_usuario'].text = ''
            self.ids['text_field_cedula_usuario'].text = ''
            self.ids['text_field_usuario_usuario'].text = ''
            self.ids['text_field_contrasena_usuario'].text = ''

# Clase principal de la aplicación utilizando KivyMD
class HeliosESP(MDApp):
    def build(self):
        Builder.load_string(KV)
        return Pagina_Principal()
if __name__ == "__main__":
    HeliosESP().run()
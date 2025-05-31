import sys
from PyQt5.QtWidgets import *
from widgetsInicio import mostrarWidgetsInicio

usuario = "1"
contraseña = "1"

listaTurnos =  [
    {"nombre": "Juan Pérez", "fecha": "2025-06-01", "hora": "10:00 AM"},
    {"nombre": "Ana González", "fecha": "2025-06-01", "hora": "11:00 AM"},
    {"nombre": "Luis Rodríguez", "fecha": "2025-06-02", "hora": "02:30 PM"},
    {"nombre": "Marta López", "fecha": "2025-06-03", "hora": "03:00 PM"},
    {"nombre": "Carlos García", "fecha": "2025-06-03", "hora": "04:00 PM"}
]
listaTurnosDisponibles = [
    {"nombre": "Turno 1", "fecha": "2025-06-01", "hora": "10:00 AM", "estado": "disponible"},
    {"nombre": "Turno 2", "fecha": "2025-06-01", "hora": "11:00 AM", "estado": "disponible"},
    {"nombre": "Turno 3", "fecha": "2025-06-02", "hora": "02:30 PM", "estado": "disponible"},
    {"nombre": "Turno 4", "fecha": "2025-06-03", "hora": "03:00 PM", "estado": "disponible"},
    {"nombre": "Turno 5", "fecha": "2025-06-03", "hora": "04:00 PM", "estado": "disponible"}
]

class PrimerVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Primer Ventana en PyQt")
        self.setGeometry(100,100,300,200)

        layout = QVBoxLayout()

        self.input = QLineEdit(self)
        self.input.setPlaceholderText("Ingresa tu nombre")
        self.input.setStyleSheet("font-size: 14px; padding: 10px; border: 2px solid gray;")

        self.inputContra = QLineEdit(self)
        self.inputContra.setPlaceholderText("Ingresa tu nombre")
        self.inputContra.setStyleSheet("font-size: 14px; padding: 10px; border: 2px solid gray;")
        self.inputContra.setEchoMode(QLineEdit.Password)


        self.label = QLabel("", self)
        self.label.move(100,80)
        self.label.setStyleSheet("""
            background-color: yellow;
            color: red;
            font-size: 18px;
            font-family: Arial;
            font-weight: bold;
            padding: 10px;
            border: 2px solid black;""")
        self.label.hide()
        
        self.button = QPushButton("Mostrar mensaje", self)
        self.button.setStyleSheet("background-color: lightblue; font-size: 14px; border-radius: 5px;")
        self.button.clicked.connect(self.mostrarMensaje)
        
        self.botonTurnos = QPushButton("Ver turnos", self)
        self.botonTurnos.setStyleSheet("background-color: lightblue; font-size: 14px; border-radius: 5px;")
        self.botonTurnos.clicked.connect(self.mostrarTurnos)
        self.botonTurnos.hide()
        #Agregar etiquetas al layout
        
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.inputContra)
        layout.addWidget(self.button)
        layout.addWidget(self.botonTurnos)


        self.setLayout(layout)
    
    def ingresarTurno(self):
        self.nombre = QLineEdit(self)
        self.nombre.setPlaceholderText("Ingresa tu nombre")
        self.nombre.setStyleSheet("font-size: 14px; padding: 10px; border: 2px solid gray;")
        self.layout().addWidget(self.nombre)
        


    def mostrarTurnos(self):
        turnosTexto = ""
        for item in listaTurnos:
            turnoInfo = f"Paciente: {item['nombre']}, Fecha: {item['fecha']}, Hora: {item['hora']}\n"
            turnosTexto +=turnoInfo
        turnosEtiqueta = QLabel(turnosTexto, self)
        turnosEtiqueta.setStyleSheet("font-size: 14px; font-family: Arial; color: black; padding: 10px;")
        turnosEtiqueta.setWordWrap(True)  # Asegura que el texto se ajuste en la pantalla
        turnosEtiqueta.move(20, 150)
        self.layout().addWidget(turnosEtiqueta)
    def mostrarMensaje(self):
        nombre = self.input.text()
        contra = self.inputContra.text()
        if nombre == usuario and contra == contraseña :
            self.label.setText(f'Hola querido {nombre}, has iniciado sesion')
            mostrarWidgetsInicio(self)
            self.botonTurnos.show()
        else:
            self.label.setText(f"Hola amigo desconocido, no estas en la base de datos.")
            mostrarWidgetsInicio(self)
    
#Crea la app QT
app = QApplication(sys.argv)

#Crea la ventana

window = PrimerVentana()
window.show()

sys.exit(app.exec_())



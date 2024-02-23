import subprocess
import time
import pyautogui
def abrir_bloc_de_notas():
    try:
        # Abrir el Bloc de notas en el sistema
        subprocess.Popen(['notepad.exe'])
        print("Bloc de notas abierto correctamente.")
    except Exception as e:
        print(f"Error al abrir el Bloc de notas: {e}")

def evitar_cerrar_bloc_de_notas():
    while True:
        time.sleep(1)
        # Verificar si el Bloc de notas está abierto
        if "Bloc de notas" in pyautogui.getWindowsWithTitle('Bloc de notas')[0].title:
            # Mover el ratón para evitar el cierre
            pyautogui.moveTo(100, 100, duration=0.25)
            # Mostrar mensaje
            print("¿Qué haces?")

if __name__ == "__main__":
    abrir_bloc_de_notas()
    evitar_cerrar_bloc_de_notas()

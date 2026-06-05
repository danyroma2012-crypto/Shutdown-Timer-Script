import os
import pyautogui
import subprocess
import winsound

si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
si.wShowWindow = 0

risposta = pyautogui.confirm (
    text = "Tra quanti secondi/minuti vuoi spegnere i pc? \n ⚠️AVVERTeNZE⚠️: \n \n 1) Questo programma arresta il pc, quindi controllare se non ci sono programmi non salvati. \n \n 2)Se appare un avviso ufficiale di Windows (es. Stai per essere disconnesso) non ti preoccupare, il pc verrà arrestato al tempo selezionato precedentemente.",
    title = "Shutdown Timer Script⏲️ (versione 1.0)",
    buttons = [ "10 secondi", "30 secondi","1 minuto","2 minuti", "3 minuti", "5 minuti", "10 minuti", "15 minuti", "20 minuti", "30 minuti", "40 minuti", "50 minuti", "1 ora", "2 ore", "3 ore"]
)
if risposta == "10 secondi":
    subprocess.Popen ("shutdown /s /t 10", startupinfo=si)
    winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
    scelta = pyautogui.confirm (text="Il pc verrà spento tra 10 secondi.", buttons= ["OK", "Annulla"])
    if scelta == "Annulla":
        subprocess.Popen("shutdown /a", startupinfo=si)
        pyautogui.alert(text="Annullato con successo!")

elif risposta == "30 secondi":
    subprocess.Popen ("shutdown /s /t 30", startupinfo=si)
    winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
    scelta = pyautogui.confirm (text="Il pc verrà spento tra 30 secondi.", buttons= ["OK", "Annulla"])
    if scelta == "Annulla":
        subprocess.Popen("shutdown /a", startupinfo=si)
        pyautogui.alert(text="Annullato con successo!")

elif risposta == "1 Minuto":
    subprocess.Popen("shutdown /s /t 60", startupinfo=si)
    winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
    scelta = pyautogui.confirm (text="Il pc verrà spento tra 1 minuto.", buttons= ["OK", "Annulla"])
    if scelta == "Annulla":
        subprocess.Popen("shutdown /a", startupinfo=si)
        pyautogui.alert(text="Annullato con successo!")

elif risposta == "2 minuti":
    subprocess.Popen("shutdown /s /t 120", startupinfo=si)
    winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
    scelta = pyautogui.confirm (text="Il pc verrà spento tra 2 minuti.", buttons= ["OK", "Annulla"])
    if scelta == "Annulla":
        subprocess.Popen("shutdown /a", startupinfo=si)
        pyautogui.alert(text="Annullato con successo!")

elif risposta == "3 minuti":
    subprocess.Popen("shutdown /s /t 180", startupinfo=si)
    winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
    scelta = pyautogui.confirm (text="Il pc verrà spento tra 3 minuti.", buttons= ["OK", "Annulla"])
    if scelta == "Annulla":
        subprocess.Popen("shutdown /a", startupinfo=si)
        pyautogui.alert(text="Annullato con successo!")

elif risposta == "5 minuti":
    subprocess.Popen("shutdown /s /t 300", startupinfo=si)
    winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
    scelta = pyautogui.confirm (text="Il pc verrà spento tra 5 minuti.", buttons= ["OK", "Annulla"])
    if scelta == "Annulla":
        subprocess.Popen("shutdown /a", startupinfo=si)
        pyautogui.alert(text="Annullato con successo!")

elif risposta == "10 minuti":
    subprocess.Popen("shutdown /s /t 600", startupinfo=si)
    winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
    scelta = pyautogui.confirm (text="Il pc verrà spento tra 2 minuti.", buttons= ["OK", "Annulla"])
    if scelta == "Annulla":
        subprocess.Popen("shutdown /a", startupinfo=si)
        pyautogui.alert(text="Annullato con successo!")

elif risposta == "15 minuti":
    subprocess.Popen("shutdown /s /t 900", startupinfo=si)
    winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
    scelta = pyautogui.confirm (text="Il pc verrà spento tra 15 minuti.", buttons= ["OK", "Annulla"])
    if scelta == "Annulla":
        subprocess.Popen("shutdown /a", startupinfo=si)
        pyautogui.alert(text="Annullato con successo!")

elif risposta == "20 minuti":
    subprocess.Popen ("shutdown /s /t 1200", startupinfo=si)
    winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
    scelta = pyautogui.confirm (text="Il pc verrà spento tra 30 minuti.", buttons= ["OK", "Annulla"])
    if scelta == "Annulla":
        subprocess.Popen("shutdown /a", startupinfo=si)
        pyautogui.alert(text="Annullato con successo!")

elif risposta == "40 minuti":
    subprocess.Popen ("shutdown /s /t 2400", startupinfo=si)
    winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
    scelta = pyautogui.confirm (text="Il pc verrà spento tra 40 minuti.", buttons= ["OK", "Annulla"])
    if scelta == "Annulla":
        subprocess.Popen("shutdown /a", startupinfo=si)
        pyautogui.alert(text="Annullato con successo!")

elif risposta == "50 minuti":
    subprocess.Popen ("shutdown /s /t 3000", startupinfo=si)
    winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
    scelta = pyautogui.confirm (text="Il pc verrà spento tra 50 minuti.", buttons= ["OK", "Annulla"])
    if scelta == "Annulla":
        subprocess.Popen("shutdown /a", startupinfo=si)
        pyautogui.alert(text="Annullato con successo!")

elif risposta == "1 ora":
    subprocess.Popen ("shutdown /s /t 3600", startupinfo=si)
    winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
    scelta = pyautogui.confirm (text="Il pc verrà spento tra 1 ora.", buttons= ["OK", "Annulla"])
    if scelta == "Annulla":
        subprocess.Popen("shutdown /a", startupinfo=si)
        pyautogui.alert(text="Annullato con successo!")

elif risposta == "2 ore":
    subprocess.Popen("shutdown /s /t 7200", startupinfo=si)
    winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
    scelta = pyautogui.confirm (text="Il pc verrà spento tra 2 ore.", buttons= ["OK", "Annulla"])
    if scelta == "Annulla":
        subprocess.Popen("shutdown /a", startupinfo=si)
        pyautogui.alert(text="Annullato con successo!")

elif risposta == "3 ore":
    subprocess.Popen ("shutdown /s /t 10800", startupinfo=si)
    winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
    scelta = pyautogui.confirm (text="Il pc verrà spento tra 3 ore.", buttons= ["OK", "Annulla"])
    if scelta == "Annulla":
        subprocess.Popen("shutdown /a", startupinfo=si)
        pyautogui.alert(text="Annullato con successo!")

else: 
    winsound.PlaySound("Systemquestion", winsound.SND_ALIAS)
    pyautogui.alert(
        text = f"Programma chiuso con successo!"
    )
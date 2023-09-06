import webbrowser
import subprocess


entry=str(input("Enter your entry: "))
length=str(input("Enter length of qr code(press enter to use default len): "))

def qr_gen(entry,length='150x150'):
    chromepath="C:\Program Files\Google\Chrome\Application\chrome.exe"
    qr=f"https://api.qrserver.com/v1/create-qr-code/?size={length}&data={entry}"
    subprocess.Popen(chromepath,shell=True)
    webbrowser.open_new_tab(qr)
qr_gen(entry,length)
   
    
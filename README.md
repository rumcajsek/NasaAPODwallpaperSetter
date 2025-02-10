**Wersja PL poniżej**
## NasaAPODwallpaperSetter
A python Script for retrieving a NASA Astronomy Picture of The Day and setting it as a wallpaper (Only on Windows! Maybe will add the functions for others sometime in the future...).\
**IMPORTANT NOTICE**\
Prerequisite for running this script is an installed Python distribution. Unfortunately there's no chance of creating an universally working executable file (though it is possible), since the script requires providing your own API key and folderpath.\
Get Python from: https://www.python.org/downloads/

## Tips on running
First of all, in order to execute this script correctly, enter your NASA_API_KEY (you can also leave "DEMO_KEY", it's limited, but for a personal usage it suffices) in line 11 of the script.\
You can either run this script manually from command line (navigate to the folder in which you saved the script and just write "python ./apodScript.py"), or set up a task in Task Scheduler to run this task periodically (preferable on startup and/or login).\
The script is written in a way that saves a state of execution everyday to "state.json" file - there's a field "count" there which provides the number of runs of the script on given day, to provide execution of full script (including call to NASA API) multiple times (most of the time only the first execution is needed) to save on your PC resources and network. If, for any reason, you want to rerun the full script, just change the value of "count" from any number present there, to 0. The script will then behave as it is its first time today.\
Any problems, errors, and the info during script execution is being logged to "apod_logs.log" file. You can see the file and check whatever was the problem if your wallpaper wasn't changed

## Task scheduler setup (for dummies):
* Press Win+R and enter "taskschd.msc", press "OK".
* Navigate to "Task Scheduler Library" on the left pane.
* Click "Create Task" on the right pane.
* On "General" Tab name your task, e.g. "Set APOD Wallpaper", optionally provide a "Description".
* In "Triggers" Tab, click "New...".
* On "Begin the task:" select "At log on" and confirm with OK.
* In "Actions" Tab click "New...".
* In "Action" select "Start a program".
* In "Program/script" enter (with quotation marks if your path contains spaces) - "C:\Path\To\Python\Folder\python.exe", change to your Python instalation folder, most often it stays "C:\Program Files\Python313\python.exe". 313 indicates version, so it depends on which Python version did you install.
* In "Add arguments (optional):" enter: (again mind quotation marks) - "C:\Path\To\Python\Script\Location\apodScript.py" and confirm with OK.
* **OPTIONALLY**: If you're not always booting up your PC/Laptop (using Sleep (or just closing the lid) instead of Shutdown), add a second Trigger - "On workstation unlock", everything else remains the same. Waking up from sleep won't trigger the "At log on" trigger if you're already logged on, and only locked (the normal state for Sleep mode).
* Confirm the task with "OK".
* Test the task by logging off and on again, or just select your created task and press "Run".
* Enjoy your NASA APOD wallpaper (almost) everyday :)

# **WERSJA PL**
## NasaAPODwallpaperSetter
Skrypt napisany w Pythonie służący do odpytywania serwisu NASA, pobranie "NASA Astronomy Picture of the Day" (Astronomiczne Zdjęcie Dnia NASA) i ustawienie go jako tapety pulpitu.\
**WAŻNE** \
Skrypt do działania wymaga zainstalowanej dystrybucji Python. Niestety nie mogę stworzyć uniwersalnego wykonywalnego pliku (tj. .exe), ponieważ skrypt do działania wymaga wprowadzenia własnego klucza API NASA i ścieżki folderu do zapisywania zdjęć.\
Jeżeli nie posiadasz Pythona, możesz zainstalować z oficjalnej strony: https://www.python.org/downloads/

## Instrukcja uruchamiania
W pierwszej kolejności, aby skrypt w ogóle zadziałał, należy wprowadzić Twój klucz API od NASA (linia 11, chociaż można również zostawić "DEMO_KEY", jest to klucz ograniczony w ilości użyć na dzień na adres IP, ale do takiego pojedynczego zastosowania wystarczy).\
Skrypt możesz uruchomić manualnie (np. z lini komend - będąc w tym samym folderze co skrypt, uruchom komendę: "python ./apodScript.py"), lub ustawić regularne zadanie w Windowsowym Harmonogramie Zadań, żeby skrypt wykonywał się regularnie (zalecam ustawienie uruchomienia przy każdym uruchomieniu systemu).\
Skrypt jest napisany w taki sposób, że zlicza ilość uruchomień każdego dnia i zapisuje tę liczbę w pliku "state.json". Znajduje się tam pole "count", które przyjmuje wartość liczbową. Służy to ograniczeniu niepotrzebnego (wtórnego) wykonywania zapytań do NASA API po raz kolejny, w sytuacji kiedy już raz pobraliśmy i ustawiliśmy zdjęcie jako tapetę. Jeżeli z jakiegokolwiek powodu potrzebujesz uruchomić pełen skrypt od początku, zmień po prostu wartość dnia dzisiejszego na "0" i skrypt zareaguje tak, jakby był uruchamiany po raz pierwszy.\
W przypadku jakichkolwiek problemów, błędów, ale także przy normalnym wykonywaniu programu, wszystkie informacje zapisywane są w "apod_logs.log". Jeżeli coś pójdzie nie tak, lub chcesz po prostu sprawdzić co się dzieje - zajrzyj tam.

## Ustawienie Harmonogramu Zadań (dla opornych)
* Naciśnij Win+R, wpisz "taskschd.msc i naciśnij "OK".
* Przejdź do "Biblioteka Harmonogramu Zadań" na liście po lewej.
* Naciśnij "Utwórz zadanie..." na liście po prawej.
* W karcie "Ogólne" wpisz swoją nazwę zadania w polu "Nazwa", opcjonalnie dodaj "Opis".
* W karcie "Wyzwalacze" naciśnij "Nowy..."
* Jako "Rozpocznij zadanie:" wybierz "Przy logowaniu" i potwierdź OK.
* W karcie "Akcje" wybierz "Nowa..."
* Jako akcję "Akcja:" wybierz "Uruchom program"
* W polu "Program/skrypt" wpisz ścieżkę do Pythona - najczęściej powinno to być "C:\Program Files\Python313\python.exe" - 313 w tym wypadku oznacza wersję, więc zwróć uwagę na to jaką wersję masz zainstalowaną. Zwracaj uwagę na spację w ścieżce, jeżeli występują, tak jak w podanym przykładzie, **musisz** ścieżkę ująć w cudzysłowie. Jeżeli spacje nie występują, to cudzysłów i tak nie zaszkodzi.
* W polu "Dodaj argumenty (opcjonalne):" wpisz ścieżkę w której masz zapisany skrypt. np. "C:\Users\test\Pobrane\apodScript.py" - ponownie zwracaj uwagę na spacje w ścieżce.
* **OPCJONALNIE** Jeżeli nie za każdym razem wyłączasz komputer/laptopa, ale używasz opcji Uśpij lub zamykasz klapę laptopa, wyzwalacz "Przy logowaniu" nie zadziała (wyzwalacz reaguje tylko jeżeli użytkownik był całkowicie wylogowany i ponownie się loguje). W tej sytuacji dodaj dodatkowy wyzwalacz - "Przy odblokowaniu stacji roboczej".  
* Zatwierdź akcję i całe zadanie "OK".
* Przetestuj wykonalność zadania z listy po prawej stronie "Uruchom".
* Ciesz się (prawie) codziennym zdjęciem astronomicznym jako tapetą ;)

**Wersja PL poniżej**
## NasaAPODwallpaperSetter
A python Script and it's .exe representation for retrieving a NASA Astronomy Picture of The Day and setting it as a wallpaper.\
**IMPORTANT NOTICE**\
**Update 10.02** .exe files in exec/ directory added. It uses DEMO_KEY as a NASA_API_KEY, so don't overuse it, otherwise NASA might block your IP. Choose between console (console window pops up during execution, nothing is printed there) and no_console versions.
Prerequisite for running this script is an installed Python distribution. If you'd prefer to use compiled .exe file, discard this instruction. \
Get Python from: https://www.python.org/downloads/

## Downloading the script
In order to download the script or .exe file, open the file, and click the "Download raw file" button:
![image](https://github.com/user-attachments/assets/ac0a998f-8b62-4c2b-ab7b-1aadc8144cde) \
save it wherever you want.

## Tips on running
First of all, if using python script, and not .exe file, enter your NASA_API_KEY (you can also leave "DEMO_KEY" though, it's limited, but for a personal usage it suffices) in line 13 of the script.\
If you don't have your API key, you can request one here: https://api.nasa.gov/ \
You can either run this script manually from command line (navigate to the folder in which you saved the script and just write "python ./apodScript.py"), or set up a task in Task Scheduler to run this task periodically (preferable on startup and/or login).\
The script is written in a way that saves a state of execution everyday to "state.json" file - there's a field "count" there which provides the number of runs of the script on given day, to provide execution of full script (including call to NASA API) multiple times (most of the time only the first execution is needed) to save on your PC resources and network. If, for any reason, you want to rerun the full script, just change the value of "count" from any number present there, to 0. The script will then behave as it is its first time today.\
Any problems, errors, and the info during script execution is being logged to "apod_logs.log" file. You can see the file and check whatever was the problem if your wallpaper wasn't changed

## Task scheduler setup (basic walkthrough, Windows only):
* Press Win+R and enter "taskschd.msc", press "OK".
* Navigate to "Task Scheduler Library" on the left pane.
* Click "Create Task" on the right pane.
* On "General" Tab name your task, e.g. "Set APOD Wallpaper", optionally provide a "Description".
* In "Triggers" Tab, click "New...".
* On "Begin the task:" select "At log on" and confirm with OK.
* In "Actions" Tab click "New...".
* In "Action" select "Start a program".
* In "Program/script" enter "python" if using python script, or path to .exe file you downloaded.
* In "Add arguments (optional):" enter, if using python script, otherwise leave blank: (mind the spaces in path, if there are any, you **must** contain the path in quotation marks) - "C:\Path\To\Python\Script\Location\apodScript.py" and confirm with OK. 
* **OPTIONALLY**: If you're not always booting up your PC/Laptop (using Sleep (or just closing the lid) instead of Shutdown), add a second Trigger - "On workstation unlock", everything else remains the same. Waking up from sleep won't trigger the "At log on" trigger if you're already logged on, and only locked (the normal state for Sleep mode).
* Confirm the task with "OK".
* Test the task by logging off and on again, or just select your created task and press "Run".
* Enjoy your NASA APOD wallpaper (almost) everyday :)

# **WERSJA PL**
## NasaAPODwallpaperSetter
Skrypt napisany w Pythonie i jego reprezentacja .exe służące do odpytywania serwisu NASA, pobranie "NASA Astronomy Picture of the Day" (Astronomiczne Zdjęcie Dnia NASA) i ustawienie go jako tapety pulpitu.\
**WAŻNE** \
**AKTUALIZACJA 10.02** \
Dodałem pliki .exe w folderze exec/. Dostępne są wersje "console" i "no_console", różnica między nimi jest taka, że "console" podczas egzekucji programu wyświetla okienko lini komend, w którym nic się nie zapisuje, no_console po prostu wykonuje program. W pliku .exe jako "NASA_API_KEY" użyty jest "DEMO_KEY", więc nie nadużywaj tego programu, w innym wypadku NASA może zablokować Twoje IP jako potencjalny spam ;) \
Skrypt do działania wymaga zainstalowanej dystrybucji Python. Jeżeli wolisz użyć pliku .exe, zignoruj poniższą instrukcję instalacji \
Jeżeli nie posiadasz Pythona, możesz zainstalować z oficjalnej strony: https://www.python.org/downloads/

## Instrukcja pobierania
Aby pobrać skrypt, wejdź w skrypt apodScript.py lub plik .exe i naciśnij "Download raw file" jak poniżej:
![image](https://github.com/user-attachments/assets/ac0a998f-8b62-4c2b-ab7b-1aadc8144cde) \
Przenieś pobrany plik gdziekolwiek chcesz na komputerze.

## Instrukcja uruchamiania
W pierwszej kolejności, należy wprowadzić Twój klucz API od NASA (linia 13, chociaż można również zostawić "DEMO_KEY", jest to klucz ograniczony w ilości użyć na dzień na adres IP, aczkolwiek do takiego pojedynczego zastosowania wystarczy).\
Jeżeli nie posiadasz klucza API od NASA, możesz zawnioskować o swój pod tym adresem: https://api.nasa.gov/
Skrypt możesz uruchomić manualnie (np. z lini komend - będąc w tym samym folderze co skrypt, uruchom komendę: "python ./apodScript.py"), lub ustawić regularne zadanie w Windowsowym Harmonogramie Zadań, żeby skrypt wykonywał się regularnie (zalecam ustawienie uruchomienia przy każdym uruchomieniu systemu).\
Skrypt jest napisany w taki sposób, że zlicza ilość uruchomień każdego dnia i zapisuje tę liczbę w pliku "state.json". Znajduje się tam pole "count", które przyjmuje wartość liczbową. Służy to ograniczeniu niepotrzebnego (wtórnego) wykonywania zapytań do NASA API po raz kolejny, w sytuacji kiedy już raz pobraliśmy i ustawiliśmy zdjęcie jako tapetę. Jeżeli z jakiegokolwiek powodu potrzebujesz uruchomić pełen skrypt od początku, zmień po prostu wartość dnia dzisiejszego na "0" i skrypt zareaguje tak, jakby był uruchamiany po raz pierwszy.\
W przypadku jakichkolwiek problemów, błędów, ale także przy normalnym wykonywaniu programu, wszystkie informacje zapisywane są w "apod_logs.log". Jeżeli coś pójdzie nie tak, lub chcesz po prostu sprawdzić co się dzieje - zajrzyj tam.

## Ustawienie Harmonogramu Zadań (krok po kroku, tylko Windows)
* Naciśnij Win+R, wpisz "taskschd.msc i naciśnij "OK".
* Przejdź do "Biblioteka Harmonogramu Zadań" na liście po lewej.
* Naciśnij "Utwórz zadanie..." na liście po prawej.
* W karcie "Ogólne" wpisz swoją nazwę zadania w polu "Nazwa", opcjonalnie dodaj "Opis".
* W karcie "Wyzwalacze" naciśnij "Nowy..."
* Jako "Rozpocznij zadanie:" wybierz "Przy logowaniu" i potwierdź OK.
* W karcie "Akcje" wybierz "Nowa..."
* Jako akcję "Akcja:" wybierz "Uruchom program"
* W polu "Program/skrypt" wpisz "python", lub podaj ścieżkę do zapisanego pliku .exe jeżeli wolisz użyć jego.
* W polu "Dodaj argumenty (opcjonalne):" wpisz ścieżkę w której masz zapisany skrypt. np. "C:\Users\test\Pobrane\apodScript.py" - zwracaj uwagę na spacje w ścieżce, jeżeli występują, to **musisz** ująć ścieżkę w cudzysłowie. Jeżeli używasz pliku .exe - pozostaw pole puste.
* **OPCJONALNIE** Jeżeli nie za każdym razem wyłączasz komputer/laptopa, ale używasz opcji Uśpij lub zamykasz klapę laptopa, wyzwalacz "Przy logowaniu" nie zadziała (wyzwalacz reaguje tylko jeżeli użytkownik był całkowicie wylogowany i ponownie się loguje). W tej sytuacji dodaj dodatkowy wyzwalacz - "Przy odblokowaniu stacji roboczej".  
* Zatwierdź akcję i całe zadanie "OK".
* Przetestuj wykonalność zadania z listy po prawej stronie "Uruchom".
* Ciesz się (prawie) codziennym zdjęciem astronomicznym jako tapetą ;)

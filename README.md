# python-ai-PH
Projekt napisany w języku Python, mający za zadanie odczytanie zawartości pliku tekstowego, przerobienie go na strukturę HTML z wykorzystaniem OpenAI API oraz zapisanie wygenerowanej wartości w nowym pliku artykul.html.

Warunki do uruchomienia skryptu:
Wersja: Python 3.9 lub wyżej
OPENAI_API_KEY: zmienna środowiskowa odnosząca się do klucza API firmy OpenAI do autoryzacji requestów.

Instalacja i ustawienia:
git clone <repository-url>
cd <repository-folder>

Tworzenie wirtualnego środowiska:
python -m venv venv

Aby aktywować środowisko wirtualne należy użyć komendy:
W sysyemie Windows:
.\venv\Scripts\activate

Instalacja zależności:
Należu upewnić się czy mamy zainstalowany pip, następnie należy zainstalować wszystkie zależności z pliku requirements.txt komendą:
pip install -r requirements.txt

Ustawianie zmiennej środowiskowej OPENAI_API_KEY:
Upewnij się że zmienna środowiskowa OPENAI_API_KEY jest poprawnie ustawiona. Aby poprawnie ją ustawić można wykorzystać komendę:
W systemie Windows(Command Prompt):
set OPENAI_API_KEY=your_openai_api_key

Umieść plik.txt w tym samym katalogu co skrypt, ewentualnie podaj pełną ścieżkę prowadzącą do pliku
Uruchom skrypt następującą komendą:
python main.py

Skrypt powinien wykonać następujące czynności:
Odczyt zawartości pliku - skrypt przetwarza tekst z podanego pliku (domyślnie plik.txt).
Transformacja zawartości na HTML - Z wykorzystaniem OpenAI API przetwarza tekst z pliku i modyfikuje go na zawartość HTML, uwzględniając przekazane iformacje i parametry. Włącząjąc w to odpowiednie tagi, placeholdery zdjęć i inne.
Zapis pliku HTML - Przetransformowany plik HTML jest zapisywany do osobnego pliku (artykul.html).

Dla chętnych 
Dodatkowo realizując zadanie dla chętnych dodane zostały 4 pliki o nazwach:
szablon.html
podglad.html
script.js
style.css

Ich zadaniem było utworzenie wizualnego szablonu HTML, który miał zwiększyć estetykę artykułu.
Aby można było poprawnie podejrzeć zawartość pliku podglad.html należy przede wszystkim pobrać wszystkie pliki a następnie w terminalu zastosować komendę:
python -m http.server 8000

Utworzymy w ten sposób lokalny server dzięki któremu będzie można obejrzeć zawartość pliku podglad.html
Następnie w przeglądarce należy wpisać adres http://localhost:8000/podglad.html
Po wejściu na stronę powinniśmy otrzymać wizualną reprezentację szablonu wraz z artykułem.

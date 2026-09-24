# KumiHimo – Kumihimo-Planer

Planer für Kumihimo auf der runden Scheibe mit 32 Schlitzen (Kongo Gumi, 8 oder 16 Fäden) und der eckigen Platte (1–12 / A–H; Flachband und Vierkant mit je 8 Fäden).
Aus einem Muster berechnet er Startaufbau, Flechtschritte und Fadenbedarf; der Flechtplan lässt sich als PDF exportieren.

## Inhalt des Ordners

| Datei | Zweck |
|---|---|
| `kumihimo-planer.html` | Das Programm. Per Doppelklick im Browser öffnen, es läuft auch offline. |
| `kumihimo_modell.py` | Dasselbe Rechenmodell in Python, zum Nachrechnen und Weiterentwickeln. |
| `Muster/` | Gespeicherte Muster als JSON-Dateien. |
| `README.md` / `README.html` | Diese Anleitung (als Text bzw. für den Browser). |
| `kumihimo-planer.zip` | Alles oben in einem Paket, immer die aktuelle Version. |

„Meine Muster“ speichert der Planer im jeweiligen Browser.
Dauerhaft sind nur die Dateien im Ordner `Muster`.

## Zu Hause im Browser betreiben

Der Planer ist eine einzige HTML-Datei und braucht keine Installation und keinen Server.

1. **ZIP herunterladen und entpacken**, zum Beispiel nach `Dokumente\KumiHimo`. Wichtig: wirklich entpacken, nicht aus dem ZIP heraus öffnen.
2. **`kumihimo-planer.html` doppelklicken.** Sie öffnet sich im Standardbrowser (Chrome, Edge oder Firefox, jeweils aktuell).
3. **Muster laden:** unter „Export“ bzw. „Muster“ auf „Dateien öffnen“ und die Dateien aus dem Ordner `Muster` wählen (mehrere auf einmal gehen).
4. **Muster sichern:** „Als Datei speichern“ legt eine JSON-Datei im Download-Ordner ab; verschiebe sie in den Ordner `Muster`.

Gut zu wissen:

- **Offline:** Planer, Editor und Flechtanleitung laufen ohne Internet. Nur der PDF-Export lädt beim ersten Mal die PDF-Bibliothek jsPDF aus dem Internet; ohne Verbindung erscheinen außerdem Ersatzschriften.
- **„Meine Muster“ liegt im Browser**, nicht im Ordner. Ein anderer Browser, ein anderer Speicherort der HTML-Datei oder das Löschen der Browserdaten zeigt eine leere Liste. Dauerhaft sind nur die Dateien im Ordner `Muster`.
- **Anleitung:** `README.html` im selben Ordner; der Knopf „Anleitung“ im Planer öffnet sie.
- **Tablet oder Handy:** Dort lassen sich lokale HTML-Dateien oft nicht bequem öffnen. Einfacher ist es, den Ordner auf einen Webserver zu legen, zum Beispiel über GitHub Pages im Repository [thunder312/KumiHimo](https://github.com/thunder312/KumiHimo) (Einstellungen → Pages → Branch `main`). Dann öffnet man den Planer über eine normale Adresse.
- **Neue Version:** Einfach die neue ZIP über den alten Ordner entpacken. Der Ordner `Muster` bleibt erhalten, solange du deine eigenen Dateien nicht überschreibst.

## Bedienung

Oben wählst du die Scheibe (**Runde Scheibe** oder **Eckige Scheibe**), darunter die Arbeitsschritte:

1. **Muster**: Vorlagen, eigene Muster und (rund) der Musterkatalog. Ein Klick lädt das Muster und öffnet den Editor; alle weiteren Schritte werden mit aktualisiert.
2. **Editor**: Fadenzahl und Farben wählen und in die Matrix malen (rund) bzw. die Fäden auf der Platte färben (eckig). Rechts das flechtbare Ergebnis und „So passt es“. „Auf die Scheibe übernehmen“ springt zur Flechtanleitung.
3. **Flechtanleitung** (nur zum Ansehen, Farben kommen aus Muster und Editor): Zählrichtung, Scheibe Schritt für Schritt, Kordel und Musterbild, Aufbau und Flechtplan, Fadenbedarf.
4. **Export**: Muster speichern (Meine Muster, Datei, Code) und Flechtplan als PDF.

Jeder große Bereich (z. B. Muster-Editor, Scheibe und Kordel, Fadenbedarf) lässt sich über den Pfeil rechts ein- und ausklappen; der Browser merkt sich das, ebenso den zuletzt offenen Arbeitsschritt.
Für den PDF-Export wird einmal die PDF-Bibliothek jsPDF aus dem Internet geladen.

## Tab „Eckige Scheibe“ (erste Ausbaustufe)

- Platte mit Schlitzen 1–12 oben und unten, A–H links und rechts (von oben nach unten); die Platte wird nicht gedreht.
- Flechtart „Flachband, 8 Fäden“ mit den Zügen nach Fire Mountain Gems (Schritte 5–18): 14 Züge je Durchgang, 8 davon quer über die Platte, 6 zum Zurücksetzen.
- Flechtart „Vierkant, 8 Fäden“ nach Fire Mountain Gems (Square Braids): 12 Züge je Durchgang, 8 quer, 4 zum Zurücksetzen; das Bandbild zeigt alle vier Seiten.
- Muster-Editor: auf alle Bandseiten frei malen (Spalten = Zielschlitze der Seite, Zeilengruppen = Durchgänge); das Programm sucht den flechtbaren Aufbau (Mehrheit je Faden) und überträgt ihn mit „Auf die Platte übernehmen“.
- In der Flechtanleitung ist die Platte nur zum Ansehen; Aufbau-Vorlagen: Oben/unten, Abwechselnd, Außen/innen, Einfarbig.
- Zug für Zug durchklicken, Flechtplan für zwei Durchgänge, Fadenbedarf.
- Export: Muster speichern (Meine Muster, Datei, Code) und Flechtplan als A4-PDF (Plattenbild, Aufbau, Züge für zwei Durchgänge, Fadenbedarf). Gespeicherte Muster erscheinen unter „1 Muster“ → „Meine Muster“.
- „Dateien öffnen“ nimmt in beiden Tabs runde und eckige Muster an und sortiert sie richtig ein.
- Das Bandbild ist schematisch (Stich auf der Seite, zu der der Faden wandert) und noch nicht an einem echten Band geprüft.

## Regeln des Kongo Gumi (Ergebnis des Modells)

- **Flechtschritt:** oben rechts nach unten rechts, unten links nach oben links, dann die Scheibe gegen den Uhrzeigersinn drehen, bis das nächste Paar oben liegt.
- **Stiche:** Jeder Schritt legt zwei Stiche. Die Fäden wandern in einer festen Reihenfolge, der Musterkette.
- **Wiederholung:** In der Matrix wiederholt sich jedes Muster alle 4 Zeilen.
- **Zwillingsstich:** Zeile r+2 ist Zeile r, um eine halbe Runde versetzt. Jeder Faden liefert genau diese beiden Stiche.
- **Längs:** Streifen in bis zu 4 Farben sind möglich, jede Farbe erscheint zweimal gegenüberliegend. Auf der Kordel werden sie zu Spiralen.
- **Quer:** Ganze Ringe gibt es nur in 2 Farben im Wechsel.
- **Kontrolle:** 16 Fäden in 2 Farben ergeben 1162 verschiedene Muster, wie im Artikel „Changing Spots“ (Bridges 2022).

Die Stichform in den Vorschauen ist schematisch. Der Einarbeitungsfaktor für den Fadenbedarf (Standard 1,5) sollte mit einer Probe gemessen werden.

## Dateiformat der Muster

```json
{
  "kumihimo": 1,
  "name": "Band rot-orange-gelb-weiß",
  "n": 16,
  "neck": "0321032103210321",
  "pal": ["#C0392B", "#E67E22", "#F1C40F", "#F7F4EC"],
  "names": ["Rot", "Orange", "Gelb", "Weiß"],
  "matrix": ["01230123", "..."]
}
```

- `n`: Fadenzahl (8 oder 16).
- `neck`: Farbnummer für jede Position der Musterkette (Index in `pal`).
- `pal`, `names`: Farben als Hex-Code und ihre Namen.
- `matrix` (optional): die Editor-Zeichnung, Zeilen von oben nach unten, `.` steht für eine leere Zelle.

Muster der eckigen Platte haben `"typ": "eckig"`, dazu `struct` (`flach8` oder `vierkant8`), `col` (Farbnummer je Faden in Aufbau-Reihenfolge) und optional `editor` mit den Zeichnungen je Bandseite.

## Python-Modell

```
python kumihimo_modell.py muster Muster/band-rot-orange-gelb-weiss.json
python kumihimo_modell.py zeichnung 16 "ABCDABCD/ABCDABCD/ABCDABCD/ABCDABCD"
python kumihimo_modell.py katalog 16
```

## Download und Kontakt

- Aktuelle Version als ZIP: im Planer oben rechts „Download ZIP“ (enthält Planer, Anleitung, Python-Modell und die Beispielmuster).
- Anleitung im Browser: `README.html`.

© 2026 Daniel Ertl · [daniel-ertl.de](https://daniel-ertl.de) · [GitHub: thunder312](https://github.com/thunder312) · dertl@web.de

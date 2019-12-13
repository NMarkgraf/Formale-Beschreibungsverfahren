#
# Deterministischer Endlicher Automat
# =-----------------=---------=------
#
# Dabei ist:
#
# Q die Menge aller Zustände (als Liste)
# E die Menge des Eingabealphabet (als Liste)
# s der Startzustand, ein Element aus Q
# F die Menge der Endzustände (als Liste)
# Eingabe als Zeichenkette

def dea(Q, E, d, s, F, Eingabe, show=None):

    tmp = ""

    def observer(q, w, show_type = None,  first=False, last=False):
        if show_type:
            wort = "".join(str(e) for e in w)

            if last:
                end_chr = "\n"
            else:
                end_chr = ""

            if len(wort) < 1:
                wort = "epsilon"

            if first:
                tmp = ""
            else:
                tmp = " |-- "

            if show_type in {"d", "Übergangsfunktion", "Übergangsfkt", "Überführungsfunktion"}:
                print("d(" + q + ", " + a + ")=" + qn)
            if show_type in {"d_dach", "Erweiterte Übergangsfunktion", "Erweiterte Überführungsfunktion"}:
                print("d_dach(" + q + ", " + '' + wort + ")=" + qn)
            if show_type in {"konfiguration", "Konfiguration"}:
                print(tmp + "(" + q + ", " + wort + ")", end=end_chr)

    w = list(Eingabe)
    q = s

    if show:
        print("Start:")
        first = True

    while w:
        a = w[0]

        if (a in E):
            if a in d[q]:
                qn = d[q][a]
            else:
                return False
        else:
            return False

        observer(q, w, show, first)

        if first:
            first = False

        q=qn

        a = w[0]

        if w:
            w = w[1:]

    observer(q, w, show, last=True)

    if q in F:
        return True
    else:
        return False


if __name__ == '__main__':
    # Tabelle der totalen Übergangsfunktion
    d={"q0":{"a" : "q1", "b" : "q0"},
       "q1":{"a" : "q2", "b" : "q0"},
       "q2":{"a" : "q2", "b" : "q2"}}

    # Tabelle einer partiellen Übergangsfunktion
    d={"q0": {"a": "q0", "b": "q1"},
       "q1": {"a": "q2"},
       "q2":             {"b": "q2"}}

    # Tabelle der Übergangsfunktion
    d={"q0":{"a" : "q1", "b" : "q0"},
       "q1":{"a" : "q1", "b" : "q2"},
       "q2":{"a" : "q3", "b" : "q2"},
       "q3":{"a" : "q3", "b" : "q4"},
       "q4":{"a" : "q5", "b" : "q4"},
       "q5":{"a" : "q5", "b" : "q4"}}

    if dea({"q0", "q1", "q2", "q3", "q4", "q5"}, {"a", "b"}, d, "q0", {"q4", "q5"}, "abbaabb", show="konfiguration" ):
        print("Der DEA hat das Wort akzeptiert!")
    else:
        print("Der DEA hat das Wort nicht akzeptiert!")


x = (14, -1, -1) + r (-8, 2, 1)

A(-2, 5, 2) B(2, 3, 0) C(2, -1, 2)

## a)
### Parametergleichung
stützvektor + r * spannvektor1 + s * spannvektor2
A + r (A-B) + s (A-C) = (-2, 5, 2) + r (-4, 2, 2) + s (-4, 6, 0)

### Koordinatengleichung
kreuzprodukt zwischen spannvektor1 und spannvektor2

x = y1 * z2 - z1 * y2 = 5 * 2 - 2 * 2 = 10 - 4 = 6
y = x1 * z2 - z1 * x2 = (-2) * 2 - 2 * (-4) = -4 - -8 = 4
z = x1 * y2 - y1 * x2 = (-2) * 2 - 5 * (-4) = -4 - -20 = 16

Normalenvektor = (6, 4, 16)

Koordinatengleichung: 6x + 4y + 16z = d
Punkt A einsetzung um d zu erhalten
d = 6 * (-2) + 4 * 5 + 16 * 2 = -12 + 20 + 32 = 40

6x + 4y + 16z = 40

Probe mit B
d = 6 * 2 + 4 * 3 + 16 * 0 = 12 + 12

Da wurde versehentlich AxB gerechnet statt mit den Stüzvektoren (BxC), kein Bock das zu korriegieren. Berechne d mit einem Punkt, der definitif in der Ebene liegt. Wenn bei einem anderen Punkt auch das selbe d rauskommt, dann liegt er in der Ebene.

## b)
siehe A

## c)
Lagebeziehungen von Vektor und Ebene
mit Solve Schnittpunkt(e) ermitteln
kein Schnittpunkt -> real parallel
genau ein Schnittpunkt -> nicht parallel
unendlich Stützpunkte (solve gibt True aus oder einer der Faktoren kann alles sein) -> gerade liegt in der Ebene

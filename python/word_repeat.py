""" 
Dado el siguiente fragmento de la novela de Frankenstein.

"""
text = """
These visions faded when I perused, for the first time, those poets
whose effusions entranced my soul and lifted it to heaven.  I also
became a poet and for one year lived in a paradise of my own creation;
I imagined that I also might obtain a niche in the temple where the
names of Homer and Shakespeare are consecrated.  You are well
acquainted with my failure and how heavily I bore the disappointment.
But just at that time I inherited the fortune of my cousin, and my
thoughts were turned into the channel of their earlier bent."""
"""

Desarrollar un programa el cual imprima en consola la segunda palabra que más se repita.

Salida deseada:

"the" se repite 6 veces.

Ayuda: Puedes apoyarte del módulo collections para contar y ordenar las palabras.

Deseado: Intenta resolver el problema sin uso de ciclos o condicionales. """


from collections import Counter
import re


words = re.findall(r'\w+', text.lower())
Counter(words).most_common(2)[1]
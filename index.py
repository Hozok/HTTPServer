#coding:utf-8
import cgi
import hashlib 
import os

print("Content-type: text/html; charset=utf-8") # Pour préciser que tout ce qui va suivre après dans un print est du code HTML en utf-8.

html = """<!DOCTYPE html>
<head>
	<meta charset="utf-8">
	<title>Test test</title>
</head>
<body>
"""
# Voici donc le code html au dessus et en dessous, qui doit bien sur respecter la syntaxe. Malheureusement, un des seuls inconvénient c'est que le code html d'au dessus n'est pas la coloration syntaxique normal du html.
print(html)


# Voici l'endroit ou vous écrivez votre code HTML :
print("<h1>Ceci est un gros titre !</h1>")
print("""
<ul>
	<li>Ceci</li>
	<li>est</li>
	<li>une</li>
	<li>liste</li>
</ul>
""")
print("<p>Ceci est un texte !</p>")

html = """
</body>
</html>
"""
print(html)



# Donc voila le code principal et simplifié pour créer vos pages HTML, vous pouvez le modifier à votre guise, mais ce script reste un exemple à prendre en compte.
# Pour voir votre page dans votre navigateur web : localhost/index.py


  


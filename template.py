from  jinja2 import Template

# temp1 = "Hola {{nombre}}"
# print(Template(temp1).render(nombre="Nixon"))

# -------------------------------------------------------------

#Renderizando simples varianñes 
# temp2 = '<a href="{{url}}"> {{enlace}} </a>'
# print(Template(temp2).render(url="http://www.flask.com", enlace="Flask"))
# #Renderizando una lista de vriables 
# temp3 = '<a href="{{datos[0]}}"> {{datos[1]}} </a>'
# print(Template(temp3).render(datos=["http://www.flask.com", "Flask"]))
# #renderixando un directorio 
# temp4 = '<a href="{{datos["url"]}}"> {{datos.enlace}} </a>'
# print(Template(temp4).render(datos={"url":"http://www.flask.com", "enlace":"Flask"}))

# -------------------------------------------------------------

#funciones striptags y title
# temp5 = 'Hola{{nombre|striptags|title}}'
# print(Template(temp5).render(nombre="   pepe   "))

# #funcion join
# temp6 = "Los datos son {{lista|join(',  ')}}"
# print(Template(temp6).render(lista=["amarillo","verde","rojo"]))

# #funciones last y length
# temp7 = "el Ultimo elemento tiene  {{lista|first|length}} caracteres" #podemos cambiar "first por second, last"
# print(Template(temp7).render(lista=["amarillo","verde","rojo"]))

# #Funcion de escape
# temp8 = "la siguiente cadena muestra todos los caracteres:  {{info|escape}} "
# print(Template(temp8).render(info="  <hola&que&tal>  "))

# -------------------------------------------------------------
temp9 = '''
<ul>
{% for pais, capital in elems.items() -%}
    <li> {{loop.index}} - {{ pais }}- {{ capital }} </li>
{% endfor -%}
</ul>
'''
#print(Template(temp9).render(elems=["amarillo","verde","rojo"]))
print(Template(temp9).render(elems={"Colombia":"Ipiales","Ecuador":"Quito"}))


# -------------------------------------------------------------
temp10 = '''
{% if elems is defined %}
    <ul>
    {%- for elem in elems %}
        {%- if elem is divisibleby 2 %}
            <li> {{elem}} es divisible por 2</li>
        {%- else %}
            <li> {{elem}} No es divisible por 2</li>
        {%- endif-%}
    {% endfor %}
    </ul>
{% endif -%}
'''
print(Template(temp10).render(elems={1,2,3,4,5,6}))

# -------------------------------------------------------------



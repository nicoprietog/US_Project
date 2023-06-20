matches = [
    {
        "equipo_casa":"Bolivia",
        "equipo_invitado":"Uruguay",
        "equipo_casa_puntaje":3,
        "equipo_invitado_puntaje":1,
        "equipo_casa_resultado":"win"
    },
    {
        "equipo_casa":"Brazil",
        "equipo_invitado":"Mexico",
        "equipo_casa_puntaje":1,
        "equipo_invitado_puntaje":1,
        "equipo_casa_resultado":"Draw"
    },
    {
        "equipo_casa":"Ecuador",
        "equipo_invitado":"Venezuela",
        "equipo_casa_puntaje":5,
        "equipo_invitado_puntaje":0,
        "equipo_casa_resultado":"win"
    },
]

new_matches = list(filter(lambda item:item["equipo_casa_resultado"]=="win",matches))
print(new_matches)
academia = {
    "nombre": "Academia Fibonacci",
    "pais": "Guatemala",
    "cursos": {
        "python" : {
            "duracion_meses" : 10,
            "precio": 1500,
            "instructor": "Luis"
        },
        "javascript" : {
            "duracion_meses" : 12,
            "precio" : 1200,
            "instructor": "María"
        },
    },
    "fundado": 2024
}

print(academia["cursos"]["python"]["instructor"])
print(academia["cursos"]["javascript"]["precio"])

academia["cursos"]["python"]["precio"] = 1800

print(academia)
studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]

def gemiddelde_per_student(studentencijfers):
    gemCijfer = []
    for item in studentencijfers:
        gemPerStudent = sum(item) / len(item)
        gemCijfer.append(gemPerStudent)
    return gemCijfer

def gemiddelde_van_alle_studenten(studentencijfers):
    gemCijferStudent = gemiddelde_per_student(studentencijfers)
    gemPerStudent = sum(gemCijferStudent) / len(gemCijferStudent)
    return gemPerStudent

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))
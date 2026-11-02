import xml.etree.ElementTree as ET

tree = ET.parse("document.xml")
root = tree.getroot()

university = {
    "name": root.get("name"),
    "campus": {
        "location": root.findtext("campus/location"),
        "established": int(root.findtext("campus/established")),
        "website": root.findtext("campus/website")
    },
    "departments": []
}

for dept in root.findall("./departments/department"):
    department = {
        "id": dept.get("id"),
        "name": dept.findtext("name"),
        "hod": dept.findtext("hod"),
        "building": dept.findtext("building"),
        "students": []
    }

    for student in dept.findall("./students/student"):
        personal = student.find("personal_details")
        academic = student.find("academic_details")
        name = personal.find("name")
        address = personal.find("address")

        student_data = {
            "id": student.get("id"),
            "personal_details": {
                "first_name": name.findtext("first_name"),
                "last_name": name.findtext("last_name"),
                "gender": personal.findtext("gender"),
                "date_of_birth": personal.findtext("date_of_birth"),
                "phone": personal.findtext("phone"),
                "email": personal.findtext("email"),
                "address": {
                    "street": address.findtext("street"),
                    "city": address.findtext("city"),
                    "state": address.findtext("state"),
                    "postal_code": address.findtext("postal_code")
                }
            },
            "academic_details": {
                "year": int(academic.findtext("year")),
                "semester": int(academic.findtext("semester")),
                "cgpa": float(academic.findtext("cgpa")),
                "advisor": academic.findtext("advisor"),
                "courses": []
            }
        }

        for course in academic.findall("./courses/course"):
            student_data["academic_details"]["courses"].append({
                "code": course.get("code"),
                "name": course.findtext("name"),
                "credits": int(course.findtext("credits")),
                "marks": int(course.findtext("marks")),
                "grade": course.findtext("grade")
            })

        department["students"].append(student_data)

    university["departments"].append(department)

print(university)


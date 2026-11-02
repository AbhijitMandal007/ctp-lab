import xml.etree.ElementTree as ET

# Your XML data stored as a string
xml_data = """<?xml version="1.0" encoding="UTF-8"?>
<students>
    <student id="101">
        <name>Rahul Sharma</name>
        <department>CSE</department>
        <year>2</year>
        <email>rahul.sharma@example.com</email>
        <cgpa>8.2</cgpa>
    </student>
    <student id="102">
        <name>Anita Das</name>
        <department>ECE</department>
        <year>3</year>
        <email>anita.das@example.com</email>
        <cgpa>8.7</cgpa>
    </student>
    <student id="103">
        <name>Rohit Singh</name>
        <department>ME</department>
        <year>1</year>
        <email>rohit.singh@example.com</email>
        <cgpa>7.9</cgpa>
    </student>
    <student id="104">
        <name>Priya Devi</name>
        <department>CSE</department>
        <year>4</year>
        <email>priya.devi@example.com</email>
        <cgpa>9.1</cgpa>
    </student>
    <student id="105">
        <name>Amit Kumar</name>
        <department>EEE</department>
        <year>2</year>
        <email>amit.kumar@example.com</email>
        <cgpa>7.6</cgpa>
    </student>
    <student id="106">
        <name>Neha Singh</name>
        <department>CSE</department>
        <year>3</year>
        <email>neha.singh@example.com</email>
        <cgpa>8.9</cgpa>
    </student>
    <student id="107">
        <name>Arjun Das</name>
        <department>ECE</department>
        <year>4</year>
        <email>arjun.das@example.com</email>
        <cgpa>8.4</cgpa>
    </student>
    <student id="108">
        <name>Riya Sharma</name>
        <department>CE</department>
        <year>1</year>
        <email>riya.sharma@example.com</email>
        <cgpa>8.0</cgpa>
    </student>
    <student id="109">
        <name>Vikash Roy</name>
        <department>ME</department>
        <year>3</year>
        <email>vikash.roy@example.com</email>
        <cgpa>7.8</cgpa>
    </student>
    <student id="110">
        <name>Sneha Paul</name>
        <department>EEE</department>
        <year>2</year>
        <email>sneha.paul@example.com</email>
        <cgpa>8.6</cgpa>
    </student>
</students>"""

# 1. Parse the XML string
root = ET.fromstring(xml_data)

# 2. Extract data into a list of dictionaries
students_list = []
for student in root.findall('student'):
    student_data = {
        "id": student.get("id"),
        "name": student.find("name").text,
        "department": student.find("department").text,
        "year": int(student.find("year").text),
        "email": student.find("email").text,
        "cgpa": float(student.find("cgpa").text)
    }
    students_list.append(student_data)

# 3. Print the parsed results cleanly
for s in students_list:
    print(f"ID: {s['id']} | Name: {s['name']} | Dept: {s['department']} | CGPA: {s['cgpa']}")
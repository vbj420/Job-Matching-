import docx

def extract_resume_information(doc):
    document = doc  
    # Initialize variables to store extracted information
    name = ""
    main_skills = []
    soft_skills = []
    experience = []
    awards = []
    
    current_section = None
    
    for paragraph in document.paragraphs:
        text = paragraph.text.strip()
        
        if text == "Skills:":
            current_section = "skills"
        elif text == "Experience:":
            current_section = "experience"
        elif text == "Awards:":
            current_section = "awards"
        elif current_section:
            if current_section == "skills":
                main_skills.extend(text.split(', '))
            elif current_section == "experience":
                experience.append(text)
            elif current_section == "awards":
                awards.append(text)
            elif current_section == "soft_skills":
                soft_skills.extend(text.split(', '))
        elif not name:
            name = text
    
    return {
        "Name": name,
        "Main Skills": main_skills,
        "Experience": experience,
        "Awards": awards
    }

# Replace 'resume.docx' with the path to your actual resume file

doc = docx.Document('resumes/001.docx')
resume_info = extract_resume_information(doc)

print("Name:", resume_info["Name"])
print()
print("Skills:", resume_info["Main Skills"])
print()
print("Experience:", resume_info["Experience"])
print()
print("Awards:", resume_info["Awards"])

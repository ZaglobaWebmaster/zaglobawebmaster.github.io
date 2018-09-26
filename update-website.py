from subprocess import call
from docx import Document

call(["git", "add", "."])
call(["git", "commit", "-m", "\"Update\""])
call(["git", "push"])

doc = Document("frontpage.docx")
p = doc.paragraphs
for i in range(len(p)):
	text = p[i].text
	if text == "BANNER":
		i += 1
		print("Banner Text:")
		print(p[i].text)
	elif text == "EVENT":
		i += 1
		print("Event Details:")
		event_name = str(p[i].text).replace("Name: ", "")
		i += 1
		event_name += "\n"
		event_details = str(p[i].text).replace("Location: ", "")
		i += 1
		event_details += " - "
		event_details += str(p[i].text).replace("Date: ", "")
		i += 1
		event_details += " - "
		event_details += str(p[i].text).replace("Time: ", "")
		print(event_name + event_name)
	print(i)

input()
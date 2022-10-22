data = input(" ")

data = data[1:-1]
sections = data.split("#")
new_sections = []
for section in sections:
    wolves_in_section = section.count("V")
    sheep_in_section = section.count("O")
    if wolves_in_section >= sheep_in_section:
        new_sections.append("V" * wolves_in_section)
    else:
        new_sections.append("O" * sheep_in_section)

new_sections_connected = "#".join(new_sections)
print("#" + new_sections_connected + "#")

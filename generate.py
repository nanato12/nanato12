from mdutils.mdutils import MdUtils

from generate_lib.models.skill import Skill

TARGET_MD_FILE_PATH = "README.md"

m = MdUtils(TARGET_MD_FILE_PATH, title="")
m.new_header(level=1, title="Hi 👋, I'm nanato12")

m.new_header(level=2, title="Skills (Order by years of experience)")

for k, skills in Skill.from_json_file("./data/skills.json").items():
    m.new_header(level=3, title=k)
    m.new_line(" ".join([skill.html_tag for skill in skills]))
    m.new_line()

with open(TARGET_MD_FILE_PATH, "wt") as f:
    f.write(m.get_md_text().strip() + "\n")

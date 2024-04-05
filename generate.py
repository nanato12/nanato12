from mdutils.mdutils import MdUtils

from generate_lib.models.budge import Budge
from generate_lib.models.contribution import Contribution
from generate_lib.models.skill import Skill
from generate_lib.models.summary import Summary

TARGET_MD_FILE_PATH = "README.md"

m = MdUtils(TARGET_MD_FILE_PATH, title="")
m.new_header(level=1, title="Hi 👋, I'm nanato12")

m.new_line(
    " ".join([b.markdown for b in Budge.from_json_file("./data/budges.json")])
)
m.new_line()

m.new_header(level=2, title="Skills (Order by years of experience)")
for k, skills in Skill.from_json_file("./data/skills.json").items():
    m.new_header(level=3, title=k)
    m.new_line(" ".join([skill.html_tag for skill in skills]))
    m.new_line()

m.new_header(level=2, title="GitHub Summaries")
m.new_line(
    " ".join(
        [s.markdown for s in Summary.from_json_file("./data/summaries.json")]
    )
)
m.new_line()

m.new_header(level=2, title="OSS Contributions")
m.new_line(
    " ".join(
        [
            p.markdown
            for p in Contribution.from_json_file("./data/contributions.json")
        ]
    )
)

with open(TARGET_MD_FILE_PATH, "wt") as f:
    f.write(m.get_md_text().strip() + "\n")

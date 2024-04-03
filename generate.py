import json

from mdutils.mdutils import MdUtils

from generate_lib.models.contribution import Contribution
from generate_lib.models.skill import Skill

TARGET_MD_FILE_PATH = "README.md"

m = MdUtils(TARGET_MD_FILE_PATH, title="")
m.new_header(level=1, title="Hi 👋, I'm nanato12")

with open("./data/summaries.json") as f:
    summaries: list[str] = json.load(f)

m.new_line(
    " ".join([m.new_inline_image(summary, summary) for summary in summaries])
)
m.new_line()

m.new_header(level=2, title="Skills (Order by years of experience)")
for k, skills in Skill.from_json_file("./data/skills.json").items():
    m.new_header(level=3, title=k)
    m.new_line(" ".join([skill.html_tag for skill in skills]))
    m.new_line()

m.new_header(level=2, title="OSS Contributions")
m.new_list(
    [
        m.new_inline_link(p.author_pr_url, f"{p.username}/{p.repository}")
        for p in Contribution.from_json_file("./data/contributions.json")
    ]
)

with open(TARGET_MD_FILE_PATH, "wt") as f:
    f.write(m.get_md_text().strip() + "\n")

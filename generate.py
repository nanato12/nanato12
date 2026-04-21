"""Generate a simple yet rich GitHub profile README."""

from pathlib import Path

from generate_lib.models.budge import Budge
from generate_lib.models.contribution import Contribution
from generate_lib.models.skill import Skill

TARGET_MD_FILE_PATH = "README.md"
USERNAME = "nanato12"
TWITTER_HANDLE = "nanato12_dev"
QIITA_HANDLE = "nanato12"
THEME = "tokyonight"


def hero() -> str:
    banner = (
        "https://capsule-render.vercel.app/api"
        "?type=waving&color=gradient&customColorList=12"
        "&height=220&section=header&text=nanato12"
        "&fontColor=ffffff&fontSize=80&fontAlignY=36&animation=fadeIn"
    )
    typing = (
        "https://readme-typing-svg.demolab.com"
        "?font=Fira+Code&weight=600&size=24&pause=800"
        "&color=5A9DF7&center=true&vCenter=true&width=640"
        "&lines=Backend+Engineer+%E2%9C%A8"
        ";Python+%7C+Go+%7C+PHP+%7C+Rust"
        ";OSS+Contributor+%40+LINE+Bot+SDK"
    )
    badges = " ".join(
        b.markdown for b in Budge.from_json_file("./data/budges.json")
    )
    return (
        '<div align="center">\n\n'
        f'<img src="{banner}" alt="banner" />\n\n'
        f'<a href="https://github.com/{USERNAME}">'
        f'<img src="{typing}" alt="typing" /></a>\n\n'
        f"{badges}\n\n"
        "</div>\n"
    )


def about() -> str:
    return (
        "## About Me\n\n"
        "> Backend engineer based in Japan. "
        "Building APIs, bots, and tools — "
        "and contributing back to OSS when I can.\n\n"
        "- Daily drivers: **Python**, **Go**, **PHP**, **Rust**\n"
        "- Currently playing with: *cloud infra*, *distributed systems*\n"
        "- Contributor of the official **LINE Bot SDKs** "
        "(`python` / `php` / `go` / `nodejs`)\n"
        f"- Reach me on [Twitter](https://x.com/{TWITTER_HANDLE}) "
        f"/ [Qiita](https://qiita.com/{QIITA_HANDLE})\n"
    )


def skills() -> str:
    by_category = Skill.from_json_file("./data/skills.json")
    rows = []
    for category, items in by_category.items():
        keys = [s.skill_icon for s in items if s.skill_icon]
        badges = [s.badge_html for s in items if s.badge]

        cells = []
        if keys:
            url = (
                "https://skillicons.dev/icons"
                f"?i={','.join(keys)}&theme=dark&perline=10"
            )
            cells.append(f'<img src="{url}" alt="{category}" height="48" />')
        cells.extend(badges)
        icons_html = " ".join(cells)

        rows.append(
            "  <tr>\n"
            f'    <td valign="middle" align="right" width="180">'
            f"<sub><b>{category}</b></sub></td>\n"
            f'    <td valign="middle">{icons_html}</td>\n'
            "  </tr>"
        )
    table = "\n".join(rows)
    return "## Tech Stack\n\n" f"<table>\n{table}\n</table>\n"


def stats() -> str:
    top_langs = (
        "https://github-readme-stats.vercel.app/api/top-langs/"
        f"?username={USERNAME}&theme={THEME}&hide_border=true"
        "&layout=compact&langs_count=8&card_width=420"
    )
    activity = (
        "https://github-readme-activity-graph.vercel.app/graph"
        f"?username={USERNAME}&theme=tokyo-night"
        "&hide_border=true&area=true"
    )

    return (
        "## GitHub Stats\n\n"
        '<div align="center">\n\n'
        f'<img src="{top_langs}" alt="top langs" />\n\n'
        f'<img src="{activity}" alt="commit activity" />\n\n'
        "</div>\n"
    )


def contributions() -> str:
    items = Contribution.from_json_file("./data/contributions.json")
    cards = []
    for c in items:
        url = f"{c.card_url}&theme={THEME}" "&hide_border=true&show_owner=true"
        href = f"https://github.com/{c.username}/{c.repository}"
        cards.append(
            f'<a href="{href}"><img src="{url}" alt="{c.repository}" /></a>'
        )
    body = "\n  ".join(cards)
    return (
        "## OSS Contributions\n\n"
        '<div align="center">\n  '
        f"{body}\n"
        "</div>\n"
    )


def footer() -> str:
    return (
        "<!-- footer -->\n"
        '<div align="center">\n\n'
        "<sub>Made with Python <code>generate.py</code> — "
        "data lives in <code>./data/*.json</code></sub>\n\n"
        "</div>\n"
    )


def main() -> None:
    parts = [
        hero(),
        about(),
        skills(),
        stats(),
        contributions(),
        footer(),
    ]
    body = "\n---\n\n".join(p.rstrip() + "\n" for p in parts)
    Path(TARGET_MD_FILE_PATH).write_text(body.strip() + "\n")


if __name__ == "__main__":
    main()

"""Generate a simple yet rich GitHub profile README."""

from pathlib import Path

from generate_lib.models.budge import Budge
from generate_lib.models.contribution import Contribution
from generate_lib.models.skill import Skill
from generate_lib.models.summary import Summary

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
        icons = " ".join(s.html_tag for s in items)
        rows.append(
            "  <tr>\n"
            f'    <td valign="middle" align="right" width="180">'
            f"<sub><b>{category}</b></sub></td>\n"
            f'    <td valign="middle">{icons}</td>\n'
            "  </tr>"
        )
    table = "\n".join(rows)
    return "## Tech Stack\n\n" f"<table>\n{table}\n</table>\n"


def stats() -> str:
    stats_card = (
        f"https://github-readme-stats.vercel.app/api?username={USERNAME}"
        f"&theme={THEME}&show_icons=true&hide_border=true"
        "&count_private=true&include_all_commits=true"
    )
    top_langs = (
        "https://github-readme-stats.vercel.app/api/top-langs/"
        f"?username={USERNAME}&theme={THEME}&hide_border=true"
        "&layout=compact&langs_count=8"
    )
    streak = (
        "https://github-readme-streak-stats.herokuapp.com/"
        f"?user={USERNAME}&theme={THEME}&hide_border=true"
    )
    activity = (
        "https://github-readme-activity-graph.vercel.app/graph"
        f"?username={USERNAME}&theme=tokyo-night"
        "&hide_border=true&area=true"
    )

    summary_urls = [
        s.url for s in Summary.from_json_file("./data/summaries.json")
    ]
    trophy_url = next((u for u in summary_urls if "trophy" in u), "")
    summary_cards = [u for u in summary_urls if "trophy" not in u]

    def img(url: str) -> str:
        return f'<img src="{url}" alt="summary" />' if url else ""

    summary_rows = []
    for i in range(0, len(summary_cards), 2):
        left = img(summary_cards[i])
        right = img(summary_cards[i + 1] if i + 1 < len(summary_cards) else "")
        summary_rows.append(
            "  <tr>\n"
            f"    <td>{left}</td>\n"
            f"    <td>{right}</td>\n"
            "  </tr>"
        )
    summary_table = "\n".join(summary_rows)

    trophy_block = (
        f'<div align="center">\n\n'
        f'<img src="{trophy_url}" alt="trophy" />\n\n'
        "</div>\n"
        if trophy_url
        else ""
    )

    return (
        "## GitHub Stats\n\n"
        '<div align="center">\n\n'
        f'<img src="{stats_card}" alt="stats" height="165" /> '
        f'<img src="{top_langs}" alt="top langs" height="165" />\n\n'
        f'<img src="{streak}" alt="streak" />\n\n'
        f'<img src="{activity}" alt="activity graph" />\n\n'
        "</div>\n\n"
        "<details>\n"
        "  <summary><b>More Summary Cards</b></summary>\n\n"
        f"<table>\n{summary_table}\n</table>\n\n"
        "</details>\n\n"
        f"{trophy_block}"
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

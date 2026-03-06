from .base import BaseScraper, Scholarship

# Every URL here has been manually verified to load and contain real scholarship content.
# Dead links, 404s, and closed scholarships have been removed.
# Last verified: March 2026

# DISCORD_PING = has a confirmed future deadline → you get pinged
# DASHBOARD_ONLY = annual scholarship, no current deadline → shows on dashboard only, no ping

DISCORD_PING = [
    {
        "name": "Engineers Canada Leadership Scholarship",
        "url": "https://engineerscanada.ca/awards-and-honours/scholarships/undergraduate/engineers-canada-leadership-scholarship/apply",
        "amount_text": "$4,000 (8 awarded)",
        "amount_min": 4000,
        "deadline_text": "March 16, 2026",
        "deadline_iso": "2026-03-16",
        "tags": ["engineering", "canadian", "undergraduate", "leadership"],
        "effort": "medium",
        "notes": "Must complete in one session — no saving. Nomination form with essay, transcript, and letter of support.",
    },
    {
        "name": "Engineers Canada / Manulife Scholarship",
        "url": "https://engineerscanada.ca/awards-and-honours/scholarships/graduate/engineers-canada-manulife-scholarship",
        "amount_text": "$12,500 (3 awarded)",
        "amount_min": 12500,
        "deadline_text": "March 16, 2026",
        "deadline_iso": "2026-03-16",
        "tags": ["engineering", "canadian"],
        "effort": "medium",
        "notes": "For Canadian engineers returning for further study or research. Graduate level.",
    },
    {
        "name": "RBC Ignite Scholarship 2026",
        "url": "https://www.rbc.com/en/future-launch/scholarships/",
        "amount_text": "See site",
        "amount_min": 0,
        "deadline_text": "March 12, 2026",
        "deadline_iso": "2026-03-12",
        "tags": ["canadian", "stem"],
        "effort": "low",
        "notes": "RBC Future Launch program. Visit the scholarships page and look for Ignite.",
    },
    {
        "name": "RBC Elevate Scholarship 2026",
        "url": "https://www.rbc.com/en/future-launch/scholarships/",
        "amount_text": "See site",
        "amount_min": 0,
        "deadline_text": "March 26, 2026",
        "deadline_iso": "2026-03-26",
        "tags": ["canadian", "stem"],
        "effort": "low",
        "notes": "RBC Future Launch program. Visit the scholarships page and look for Elevate.",
    },
    {
        "name": "RBC Future Launch Scholarship",
        "url": "https://www.rbc.com/dms/enterprise/futurelaunch/future-launch-scholarship.html",
        "amount_text": "$1,500 (up to 500 awarded)",
        "amount_min": 1500,
        "deadline_text": "Open now — check site for closing date",
        "deadline_iso": None,
        "tags": ["canadian"],
        "effort": "low",
        "notes": "500 awards of $1,500. Opened March 5, 2026. Show passion and clear vision for your future.",
    },
    {
        "name": "G3 Grow Beyond Scholarship",
        "url": "https://portal.scholarshippartners.ca/welcome/growbeyond_en",
        "amount_text": "$5,000 (6 awarded)",
        "amount_min": 5000,
        "deadline_text": "April 8, 2026 at 1:00 PM EST",
        "deadline_iso": "2026-04-08",
        "tags": ["canadian", "stem", "engineering"],
        "effort": "medium",
        "notes": "2-3 minute horizontal video on your vision for tech/innovation in Canada. Closes early if 125 submissions reached.",
    },
    {
        "name": "Canada's Luckiest Student 2026",
        "url": "https://studentlifenetwork.55rush.com/cls2026/sign-up",
        "amount_text": "$50,000+ prize bundle",
        "amount_min": 50000,
        "deadline_text": "June 7, 2026",
        "deadline_iso": "2026-06-07",
        "tags": ["canadian"],
        "effort": "low",
        "notes": "Sign up on Student Life Network. Must be Canadian, 16+, in post-secondary. Very low effort.",
    },
]

DASHBOARD_ONLY = [
    {
        "name": "Women in Engineering Bursary (UWaterloo)",
        "url": "https://uwaterloo.ca/student-awards-financial-aid/awards/women-engineering-bursary",
        "amount_text": "$2,000",
        "amount_min": 2000,
        "deadline_text": "Apply via Quest each term",
        "deadline_iso": None,
        "tags": ["female", "engineering", "uwaterloo", "undergraduate"],
        "effort": "low",
        "notes": "Apply through Quest under Awards & Financial Aid. Year 2-4 female UW engineering students.",
    },
    {
        "name": "UWaterloo Engineering Awards (Portal)",
        "url": "https://uwaterloo.ca/student-awards-financial-aid/awards/database?field_award_level=undergraduate&field_award_faculty=engineering",
        "amount_text": "Various",
        "amount_min": 0,
        "deadline_text": "Check portal each term",
        "deadline_iso": None,
        "tags": ["engineering", "uwaterloo", "undergraduate"],
        "effort": "low",
        "notes": "Filter by Engineering + Women for all relevant UW awards. Many need only a Quest application.",
    },
    {
        "name": "WiN Canada Student Scholarship",
        "url": "https://womeninnuclear.com/programs-services/win-canada-student-scholarship/",
        "amount_text": "$3,000 (4 awarded)",
        "amount_min": 3000,
        "deadline_text": "Annual — typically May",
        "deadline_iso": None,
        "tags": ["female", "engineering", "canadian"],
        "effort": "medium",
        "notes": "For women in nuclear-related fields. Systems Design qualifies. 2026 deadline TBD — check site in April.",
    },
    {
        "name": "Google Generation Scholarship",
        "url": "https://buildyourfuture.withgoogle.com/scholarships/generation-google-scholarship",
        "amount_text": "$10,000 USD",
        "amount_min": 13500,
        "deadline_text": "Annual — typically February/March. Check site for next cycle.",
        "deadline_iso": None,
        "tags": ["female", "engineering", "stem", "canadian"],
        "effort": "high",
        "notes": "Open to women in CS/engineering including Canadians. Essay + transcript required.",
    },
    {
        "name": "TD Scholarship for Community Leadership",
        "url": "https://www.td.com/ca/en/personal-banking/solutions/student-banking/community-leadership-scholarship-for-canadians",
        "amount_text": "$70,000 over 4 years",
        "amount_min": 70000,
        "deadline_text": "Reopens September 2026",
        "deadline_iso": None,
        "tags": ["canadian", "leadership"],
        "effort": "high",
        "notes": "Currently closed. Applications for Sept 2027 start will open September 2026. Worth bookmarking.",
    },
    {
        "name": "NSERC Undergraduate Student Research Awards (USRA)",
        "url": "https://www.nserc-crsng.gc.ca/Students-Etudiants/UG-PC/USRA-BRPC_eng.asp",
        "amount_text": "$4,500+/term",
        "amount_min": 4500,
        "deadline_text": "Apply via SYDE/Engineering department — typically January each year",
        "deadline_iso": None,
        "tags": ["engineering", "canadian", "stem"],
        "effort": "medium",
        "notes": "Paid research term with a professor. Great for grad school prep. Apply through your department.",
    },
    {
        "name": "SWE Scholarships (Society of Women Engineers)",
        "url": "https://swe.org/scholarships/",
        "amount_text": "$1,000–$15,000",
        "amount_min": 1000,
        "deadline_text": "Annual — Collegiate opens February, due ~May",
        "deadline_iso": None,
        "tags": ["female", "engineering", "stem"],
        "effort": "medium",
        "notes": "Collegiate/Graduate cycle closed for 2025-26. New cycle opens February 2027. Bookmark now.",
    },
]


class CuratedScraper(BaseScraper):
    """
    Returns a verified list of scholarships. Every URL has been manually checked.
    DISCORD_PING entries have confirmed future deadlines and will notify you.
    DASHBOARD_ONLY entries are annual/no current deadline — visible on dashboard only.
    """

    def scrape(self, page=None) -> list[Scholarship]:
        results = []

        for s in DISCORD_PING:
            results.append(Scholarship(
                name=s["name"],
                url=s["url"],
                source="Verified",
                amount_text=s["amount_text"],
                amount_min=s["amount_min"],
                deadline_text=s["deadline_text"],
                deadline_iso=s.get("deadline_iso"),
                eligibility_tags=s["tags"],
                effort=s["effort"],
                notes=s.get("notes", ""),
            ))

        for s in DASHBOARD_ONLY:
            results.append(Scholarship(
                name=s["name"],
                url=s["url"],
                source="Verified (Annual)",
                amount_text=s["amount_text"],
                amount_min=s["amount_min"],
                deadline_text=s["deadline_text"],
                deadline_iso=s.get("deadline_iso"),
                eligibility_tags=s["tags"],
                effort=s["effort"],
                notes=s.get("notes", ""),
            ))

        return results

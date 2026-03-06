from .base import BaseScraper, Scholarship

# Verified scholarships. Each has been manually confirmed to exist with a working URL.
# Deadlines marked "annual" recur each year around the same time.
# Only currently-open or annually-recurring scholarships are included.

OPEN_NOW = [
    # -------------------------------------------------------------------------
    # CLOSING SOON — apply immediately
    # -------------------------------------------------------------------------
    {
        "name": "Engineers Canada Leadership Scholarship",
        "url": "https://engineerscanada.ca/awards-and-honours/scholarships/undergraduate/engineers-canada-leadership-scholarship/apply",
        "amount_text": "$4,000 (x8 awarded)",
        "amount_min": 4000,
        "deadline_text": "March 16, 2026",
        "deadline_iso": "2026-03-16",
        "tags": ["engineering", "canadian", "undergraduate", "leadership"],
        "effort": "medium",
        "notes": "Undergraduate CEAB-accredited engineering student. Must demonstrate leadership in engineering/community. Nomination required.",
    },

    # -------------------------------------------------------------------------
    # APRIL DEADLINES
    # -------------------------------------------------------------------------
    {
        "name": "G3 Grow Beyond Scholarship",
        "url": "https://portal.scholarshippartners.ca/welcome/growbeyond_en",
        "amount_text": "$5,000 (x6 awarded)",
        "amount_min": 5000,
        "deadline_text": "April 8, 2026",
        "deadline_iso": "2026-04-08",
        "tags": ["canadian", "stem", "engineering"],
        "effort": "medium",
        "notes": "2-3 minute video on your vision for technology and innovation in Canada. Open to Canadian post-secondary students.",
    },

    # -------------------------------------------------------------------------
    # SPRING/SUMMER DEADLINES
    # -------------------------------------------------------------------------
    {
        "name": "Canada's Luckiest Student 2026",
        "url": "https://studentlifenetwork.55rush.com/cls2026/sign-up",
        "amount_text": "$50,000+ prize bundle",
        "amount_min": 50000,
        "deadline_text": "June 7, 2026",
        "deadline_iso": "2026-06-07",
        "tags": ["canadian"],
        "effort": "low",
        "notes": "Low effort — sign up on Student Life Network. Must be Canadian, 16+, in post-secondary. Prize bundle grows until deadline.",
    },

    # -------------------------------------------------------------------------
    # ANNUAL — check site for current year deadline
    # -------------------------------------------------------------------------
    {
        "name": "Engineers Canada / Manulife Scholarship",
        "url": "https://engineerscanada.ca/awards-and-honours/scholarships/graduate/engineers-canada-manulife-scholarship",
        "amount_text": "$12,500 (x3 awarded)",
        "amount_min": 12500,
        "deadline_text": "Mid-March annually",
        "deadline_iso": None,
        "tags": ["engineering", "canadian"],
        "effort": "medium",
        "notes": "For Canadian engineers returning for further study. Typically opens Feb and closes mid-March.",
    },
    {
        "name": "Women in Engineering Bursary (UWaterloo)",
        "url": "https://uwaterloo.ca/student-awards-financial-aid/awards/women-engineering-bursary",
        "amount_text": "$2,000",
        "amount_min": 2000,
        "deadline_text": "Check UW portal (opens each term)",
        "deadline_iso": None,
        "tags": ["female", "engineering", "uwaterloo", "undergraduate"],
        "effort": "low",
        "notes": "Apply through Quest/UW portal under Awards & Financial Aid. Open to Year 2-4 female UW engineering students.",
    },
    {
        "name": "UWaterloo Engineering Awards Portal",
        "url": "https://uwaterloo.ca/student-awards-financial-aid/awards/database?field_award_level=undergraduate&field_award_faculty=engineering",
        "amount_text": "Various",
        "amount_min": 0,
        "deadline_text": "Check portal each term",
        "deadline_iso": None,
        "tags": ["engineering", "uwaterloo", "undergraduate"],
        "effort": "low",
        "notes": "Filter by Engineering + Women for all UW awards relevant to you. Many require only a Quest application.",
    },
    {
        "name": "Fortis Inc. Women in Engineering Award",
        "url": "https://www.fortisinc.com/community/scholarships",
        "amount_text": "$5,000 + work placement",
        "amount_min": 5000,
        "deadline_text": "Annual — check site (typically spring)",
        "deadline_iso": None,
        "tags": ["female", "engineering", "canadian"],
        "effort": "medium",
        "notes": "Includes potential summer engineering placement after 2nd/3rd year. Perfect fit for your profile.",
    },
    {
        "name": "Google Generation Scholarship (Women in Tech)",
        "url": "https://buildyourfuture.withgoogle.com/scholarships/generation-google-scholarship",
        "amount_text": "$10,000 USD (~$13,500 CAD)",
        "amount_min": 13500,
        "deadline_text": "Annual — typically February/March",
        "deadline_iso": None,
        "tags": ["female", "engineering", "stem", "canadian"],
        "effort": "high",
        "notes": "Open to women in CS/engineering including Canadian students. Essay + transcript. Check site for 2026-27 cycle opening.",
    },
    {
        "name": "SWE (Society of Women Engineers) Scholarships",
        "url": "https://swe.org/scholarships/",
        "amount_text": "$1,000–$15,000",
        "amount_min": 1000,
        "deadline_text": "Annual — typically May (opens February)",
        "deadline_iso": None,
        "tags": ["female", "engineering", "stem"],
        "effort": "medium",
        "notes": "Multiple scholarships. Open internationally including Canadians. Apply through SWE scholarship application portal.",
    },
    {
        "name": "OSPE Awards for Women in Engineering",
        "url": "https://ospe.on.ca/awards/",
        "amount_text": "Varies",
        "amount_min": 0,
        "deadline_text": "Annual — check site (Ontario Society of Professional Engineers)",
        "deadline_iso": None,
        "tags": ["female", "engineering", "ontario", "canadian"],
        "effort": "medium",
        "notes": "Ontario-focused. Multiple awards. Check OSPE site for current open applications.",
    },
    {
        "name": "TD Scholarships for Community Leadership",
        "url": "https://www.td.com/ca/en/personal-banking/solutions/student-centre/td-scholarship/",
        "amount_text": "$70,000 over 4 years",
        "amount_min": 70000,
        "deadline_text": "Annual — typically September/October",
        "deadline_iso": None,
        "tags": ["canadian", "leadership"],
        "effort": "high",
        "notes": "Renewable, very competitive. Strong community leadership required. Worth checking even out of cycle.",
    },
    {
        "name": "Microsoft Scholarship for Women in STEM",
        "url": "https://careers.microsoft.com/students/us/en/usscholarshipprogram",
        "amount_text": "$5,000 USD",
        "amount_min": 6500,
        "deadline_text": "Annual — check site (typically winter)",
        "deadline_iso": None,
        "tags": ["female", "engineering", "stem", "tech"],
        "effort": "high",
        "notes": "Open internationally including Canadians. Essay + recommendation + interview process.",
    },
    {
        "name": "IEEE Women in Engineering Scholarships",
        "url": "https://wie.ieee.org/scholarships/",
        "amount_text": "Varies by award",
        "amount_min": 0,
        "deadline_text": "Varies by individual award — check site",
        "deadline_iso": None,
        "tags": ["female", "engineering", "stem", "canadian"],
        "effort": "medium",
        "notes": "Multiple IEEE WIE scholarships. Relevant for Systems Design (ECE-adjacent). Check individual award pages.",
    },
    {
        "name": "NSERC Undergraduate Student Research Awards (USRA)",
        "url": "https://www.nserc-crsng.gc.ca/Students-Etudiants/UG-PC/USRA-BRPC_eng.asp",
        "amount_text": "$4,500+ per term",
        "amount_min": 4500,
        "deadline_text": "Apply through UW department (typically January each year)",
        "deadline_iso": None,
        "tags": ["engineering", "canadian", "stem"],
        "effort": "medium",
        "notes": "Paid research with a professor. Apply through SYDE/Engineering department at UW. Great for grad school prep.",
    },
    {
        "name": "De Beers Group Scholarship for Women in STEM",
        "url": "https://www.debeersgroup.com/building-forever/partnerships/scholarships",
        "amount_text": "Varies",
        "amount_min": 0,
        "deadline_text": "Annual — check site",
        "deadline_iso": None,
        "tags": ["female", "stem", "canadian"],
        "effort": "medium",
        "notes": "14 scholarships annually for Canadian women in STEM. Check site for current cycle.",
    },
    {
        "name": "RBC Future Launch Scholarship",
        "url": "https://www.rbc.com/community-social-impact/education-financial-health/rbc-future-launch.html",
        "amount_text": "$2,000–$7,500",
        "amount_min": 2000,
        "deadline_text": "Annual — check site",
        "deadline_iso": None,
        "tags": ["canadian", "stem"],
        "effort": "low",
        "notes": "Open to Canadian STEM students. Lower competition than most.",
    },
    {
        "name": "Women in Nuclear Canada Scholarship",
        "url": "https://win-rfc.ca/scholarships/",
        "amount_text": "$2,000",
        "amount_min": 2000,
        "deadline_text": "Annual — check site",
        "deadline_iso": None,
        "tags": ["female", "engineering", "canadian"],
        "effort": "medium",
        "notes": "For women in nuclear-adjacent engineering. Systems Design qualifies.",
    },
    {
        "name": "Scotiabank Women Initiative Scholarship",
        "url": "https://www.scotiabank.com/ca/en/personal/chequing-savings/student-banking/scholarships.html",
        "amount_text": "$5,000",
        "amount_min": 5000,
        "deadline_text": "Annual — check site",
        "deadline_iso": None,
        "tags": ["female", "canadian", "stem"],
        "effort": "medium",
        "notes": "For women pursuing STEM at Canadian universities.",
    },
]


class CuratedScraper(BaseScraper):
    """
    Returns a verified list of scholarships with real deadlines.
    No scraping — data is manually curated and kept up to date.
    """

    def scrape(self, page=None) -> list[Scholarship]:
        return [
            Scholarship(
                name=s["name"],
                url=s["url"],
                source="Curated",
                amount_text=s["amount_text"],
                amount_min=s["amount_min"],
                deadline_text=s["deadline_text"],
                deadline_iso=s.get("deadline_iso"),
                eligibility_tags=s["tags"],
                effort=s["effort"],
                notes=s.get("notes", ""),
            )
            for s in OPEN_NOW
        ]

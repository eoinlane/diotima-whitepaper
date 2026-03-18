"""
Diotima: Compliance-Grade AI Infrastructure for Formative Assessment
A manim video showcasing the whitepaper narrative.

Render with:
    manim -pqh diotima_video.py DiotimaVideo

For lower quality preview:
    manim -pql diotima_video.py DiotimaVideo
"""

from manim import *

# ── Colour palette ──────────────────────────────────────────────────────────
NAVY = "#1B3A5C"
TEAL = "#2A7F7F"
LIGHT_BG = "#EAF4F4"
MID_BG = "#D0E8E8"
DARK_TEXT = "#1A1A1A"
MUTED_GREY = "#666666"
WARM_WHITE = "#F8F8F8"
ACCENT_CORAL = "#E07A5F"
ACCENT_GOLD = "#F2CC8F"
DEEP_NAVY = "#0F2440"


class DiotimaVideo(Scene):
    """Full Diotima whitepaper video — single scene with sequential acts."""

    def construct(self):
        self.camera.background_color = DEEP_NAVY
        self.act_title()
        self.act_problem()
        self.act_what_is_diotima()
        self.act_lifecycle()
        self.act_architecture()
        self.act_human_oversight()
        self.act_explainability()
        self.act_model_selection()
        self.act_data_governance()
        self.act_compliance_moat()
        self.act_conclusion()

    # ── helpers ──────────────────────────────────────────────────────────────

    def clear_scene(self, fade_time=0.6):
        self.play(FadeOut(Group(*self.mobjects)), run_time=fade_time)

    def section_header(self, number, title, subtitle=None):
        """Animated section header with number pill and title."""
        pill = (
            VGroup(
                RoundedRectangle(
                    corner_radius=0.15, width=1.0, height=0.5,
                    fill_color=TEAL, fill_opacity=1, stroke_width=0,
                ),
                Text(f"{number:02d}", font_size=24, color=WHITE, weight=BOLD),
            )
            .arrange(ORIGIN)
            .to_edge(LEFT, buff=1)
            .shift(UP * 0.5)
        )
        heading = Text(title, font_size=40, color=WHITE, weight=BOLD).next_to(
            pill, RIGHT, buff=0.4
        )
        group = VGroup(pill, heading)
        if subtitle:
            sub = Text(subtitle, font_size=22, color=MUTED_GREY).next_to(
                heading, DOWN, aligned_edge=LEFT, buff=0.2
            )
            group.add(sub)
        group.move_to(ORIGIN).shift(UP * 2.5)
        self.play(FadeIn(pill, shift=LEFT * 0.3), Write(heading), run_time=0.8)
        if subtitle:
            self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.4)
        self.wait(0.5)
        return group

    def bullet_list(self, items, start_y=1.0, font_size=24, color=WARM_WHITE):
        """Animate a bullet list one item at a time."""
        bullets = VGroup()
        for i, text in enumerate(items):
            tri = (
                Triangle(fill_color=TEAL, fill_opacity=1, stroke_width=0)
                .scale(0.08)
                .rotate(-PI / 2)
            )
            label = Text(text, font_size=font_size, color=color)
            row = VGroup(tri, label).arrange(RIGHT, buff=0.25)
            row.move_to(UP * (start_y - i * 0.6)).to_edge(LEFT, buff=1.5)
            bullets.add(row)
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.35)
        self.wait(1.0)
        return bullets

    def fade_between(self, old_group=None):
        """Fade out everything and return a clean slate."""
        self.clear_scene()
        self.wait(0.3)

    # ── ACT 1: Title ────────────────────────────────────────────────────────

    def act_title(self):
        # Background glow
        glow = Circle(radius=3, fill_color=TEAL, fill_opacity=0.06, stroke_width=0)
        self.add(glow)

        title = Text("Diotima", font_size=72, color=WHITE, weight=BOLD)
        subtitle = Text(
            "Compliance-Grade AI Infrastructure\nfor Formative Assessment in Education",
            font_size=26,
            color=MID_BG,
            line_spacing=1.4,
        ).next_to(title, DOWN, buff=0.5)

        rule = Line(LEFT * 3, RIGHT * 3, color=TEAL, stroke_width=2).next_to(
            subtitle, DOWN, buff=0.4
        )
        byline = Text(
            "Noval Consulting  |  Working Paper 2025",
            font_size=18,
            color=MUTED_GREY,
        ).next_to(rule, DOWN, buff=0.3)

        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.8)
        self.play(Create(rule), FadeIn(byline), run_time=0.6)
        self.wait(2)
        self.fade_between()

    # ── ACT 2: The Problem ──────────────────────────────────────────────────

    def act_problem(self):
        header = self.section_header(1, "The Compliance Gap", "AI in education is high-risk by default")

        # Three pillars
        pillars_data = [
            ("THE REGULATION", "EU AI Act classifies\nstudent assessment AI\nas high-risk"),
            ("THE GAP", "Most products treat\ncompliance as\ndownstream"),
            ("THE APPROACH", "Diotima builds\nregulatory alignment\nfrom first principles"),
        ]
        pillars = VGroup()
        for i, (label, desc) in enumerate(pillars_data):
            box = RoundedRectangle(
                corner_radius=0.15, width=3.5, height=2.8,
                fill_color=NAVY, fill_opacity=0.8, stroke_color=TEAL,
                stroke_width=1.5,
            )
            num_text = Text(f"0{i+1}", font_size=36, color=TEAL, weight=BOLD)
            title_text = Text(label, font_size=16, color=ACCENT_GOLD, weight=BOLD)
            desc_text = Text(desc, font_size=15, color=WARM_WHITE, line_spacing=1.3)
            content = VGroup(num_text, title_text, desc_text).arrange(DOWN, buff=0.25)
            pillar = VGroup(box, content).arrange(ORIGIN)
            pillars.add(pillar)

        pillars.arrange(RIGHT, buff=0.4).move_to(DOWN * 0.5)
        for p in pillars:
            self.play(FadeIn(p, shift=UP * 0.3), run_time=0.5)
        self.wait(2)

        # Callout
        callout_box = RoundedRectangle(
            corner_radius=0.1, width=11, height=0.8,
            fill_color=TEAL, fill_opacity=0.15, stroke_color=TEAL,
            stroke_width=1,
        ).move_to(DOWN * 2.8)
        callout_text = Text(
            "Annex III, Section 3(a): AI in student assessment = high-risk",
            font_size=18, color=TEAL, weight=BOLD,
        ).move_to(callout_box)
        self.play(FadeIn(callout_box), Write(callout_text), run_time=0.6)
        self.wait(2)
        self.fade_between()

    # ── ACT 3: What Diotima Is ──────────────────────────────────────────────

    def act_what_is_diotima(self):
        header = self.section_header(
            2, "What Diotima Actually Is",
            "A teacher-centred decision-support system"
        )

        # Three-column flow: AI PROPOSES → TEACHER DECIDES → STUDENTS BENEFIT
        cols_data = [
            (TEAL, "AI PROPOSES", "Generates curriculum-\naligned questions,\nrubrics, and feedback"),
            (NAVY, "TEACHER DECIDES", "Approves, edits,\noverrides, or replaces\nany AI output"),
            (ACCENT_CORAL, "STUDENTS BENEFIT", "Higher-quality,\nconsistent formative\nfeedback"),
        ]
        cols = VGroup()
        for color, title, desc in cols_data:
            circle = Circle(radius=0.5, fill_color=color, fill_opacity=0.3, stroke_color=color, stroke_width=2)
            icon_label = Text(title[:1], font_size=28, color=color, weight=BOLD).move_to(circle)
            title_t = Text(title, font_size=16, color=color, weight=BOLD)
            desc_t = Text(desc, font_size=14, color=WARM_WHITE, line_spacing=1.3)
            col = VGroup(VGroup(circle, icon_label), title_t, desc_t).arrange(DOWN, buff=0.3)
            cols.add(col)

        cols.arrange(RIGHT, buff=1.2).move_to(DOWN * 0.3)

        # Arrows between columns
        arrows = VGroup()
        for i in range(len(cols) - 1):
            arr = Arrow(
                cols[i].get_right() + LEFT * 0.1,
                cols[i + 1].get_left() + RIGHT * 0.1,
                color=MUTED_GREY, stroke_width=2, max_tip_length_to_length_ratio=0.15,
            )
            arrows.add(arr)

        self.play(*[FadeIn(c, shift=UP * 0.3) for c in cols], run_time=0.8)
        self.play(*[GrowArrow(a) for a in arrows], run_time=0.5)
        self.wait(1)

        # Key constraint callout
        constraint = Text(
            "No AI output is final without human confirmation.",
            font_size=22, color=ACCENT_GOLD, weight=BOLD,
        ).move_to(DOWN * 2.8)
        self.play(Write(constraint), run_time=0.8)
        self.wait(2)
        self.fade_between()

    # ── ACT 4: Assessment Lifecycle ─────────────────────────────────────────

    def act_lifecycle(self):
        header = self.section_header(
            3, "The Formative Assessment Lifecycle",
            "Seven stages — design through audit"
        )

        stages = [
            ("1", "DESIGN", "Curriculum-grounded\nassessment design"),
            ("2", "APPROVE", "Teacher pre-approval\nof all content"),
            ("3", "RESPOND", "Student response\n& optional AI pre-check"),
            ("4", "REVEAL", "Conditional rubric\nvisibility"),
            ("5", "REVIEW", "Teacher review,\noverride & finalisation"),
            ("6", "REFLECT", "Student feedback\nand reflection"),
            ("7", "AUDIT", "Comprehensive logging\n& auditability"),
        ]

        # Build circular / arc layout
        stage_mobs = VGroup()
        # Use two rows: 4 on top, 3 on bottom
        top_row = VGroup()
        bottom_row = VGroup()

        for i, (num, label, desc) in enumerate(stages):
            pill = RoundedRectangle(
                corner_radius=0.12, width=2.6, height=1.6,
                fill_color=NAVY, fill_opacity=0.85,
                stroke_color=TEAL, stroke_width=1.5,
            )
            num_t = Text(num, font_size=22, color=TEAL, weight=BOLD)
            label_t = Text(label, font_size=14, color=ACCENT_GOLD, weight=BOLD)
            desc_t = Text(desc, font_size=11, color=WARM_WHITE, line_spacing=1.2)
            content = VGroup(num_t, label_t, desc_t).arrange(DOWN, buff=0.1)
            stage = VGroup(pill, content).arrange(ORIGIN)

            if i < 4:
                top_row.add(stage)
            else:
                bottom_row.add(stage)

        top_row.arrange(RIGHT, buff=0.25).move_to(UP * 0.2)
        bottom_row.arrange(RIGHT, buff=0.25).move_to(DOWN * 1.8)
        stage_mobs = VGroup(top_row, bottom_row)

        # Animate stages sequentially
        for row in [top_row, bottom_row]:
            for stage in row:
                self.play(FadeIn(stage, shift=UP * 0.2), run_time=0.3)

        # Draw connecting arrows along the top row
        arrows = VGroup()
        for i in range(len(top_row) - 1):
            a = Arrow(
                top_row[i].get_right(), top_row[i + 1].get_left(),
                color=TEAL, stroke_width=1.5, buff=0.1,
                max_tip_length_to_length_ratio=0.2,
            )
            arrows.add(a)
        # Arrow from top row last to bottom row first
        a = Arrow(
            top_row[-1].get_bottom(), bottom_row[0].get_top(),
            color=TEAL, stroke_width=1.5, buff=0.1,
            max_tip_length_to_length_ratio=0.2,
        )
        arrows.add(a)
        for i in range(len(bottom_row) - 1):
            a = Arrow(
                bottom_row[i].get_right(), bottom_row[i + 1].get_left(),
                color=TEAL, stroke_width=1.5, buff=0.1,
                max_tip_length_to_length_ratio=0.2,
            )
            arrows.add(a)

        self.play(*[GrowArrow(a) for a in arrows], run_time=0.6)
        self.wait(2.5)
        self.fade_between()

    # ── ACT 5: Architecture ─────────────────────────────────────────────────

    def act_architecture(self):
        header = self.section_header(
            4, "Architecture Built for Compliance",
            "Grounded generation & narrowly scoped high-risk"
        )

        # Left side: Bloom's taxonomy tower
        bloom_title = Text("Bloom's Taxonomy", font_size=18, color=ACCENT_GOLD, weight=BOLD)
        bloom_levels = ["Remember", "Understand", "Apply", "Analyse", "Evaluate", "Create"]
        bloom_colors = [
            "#3D5A80", "#4A7C7C", "#5B9279", "#7EAE5B", "#C4A35A", "#E07A5F"
        ]
        bloom_bars = VGroup()
        for i, (level, col) in enumerate(zip(bloom_levels, bloom_colors)):
            width = 2.0 + i * 0.15
            bar = RoundedRectangle(
                corner_radius=0.08, width=width, height=0.35,
                fill_color=col, fill_opacity=0.85, stroke_width=0,
            )
            label = Text(level, font_size=13, color=WHITE).move_to(bar)
            bloom_bars.add(VGroup(bar, label))
        bloom_bars.arrange(UP, buff=0.06)
        bloom_group = VGroup(bloom_title, bloom_bars).arrange(DOWN, buff=0.3)
        bloom_group.move_to(LEFT * 4 + DOWN * 0.5)

        # Arrow label
        arrow_label = Text("Lower → Higher Order", font_size=12, color=MUTED_GREY)
        arrow_label.next_to(bloom_bars, RIGHT, buff=0.2).shift(DOWN * 0.3)

        self.play(FadeIn(bloom_group, shift=UP * 0.3), FadeIn(arrow_label), run_time=0.8)

        # Right side: System architecture boxes
        arch_title = Text("System Architecture", font_size=18, color=ACCENT_GOLD, weight=BOLD)

        # High-risk components
        hr_label = Text("High-Risk (EU AI Act)", font_size=12, color=ACCENT_CORAL, weight=BOLD)
        hr_box1 = RoundedRectangle(
            corner_radius=0.1, width=3.5, height=0.5,
            fill_color=ACCENT_CORAL, fill_opacity=0.2,
            stroke_color=ACCENT_CORAL, stroke_width=1.5,
        )
        hr_text1 = Text("QAR Generation", font_size=14, color=ACCENT_CORAL).move_to(hr_box1)
        hr_box2 = RoundedRectangle(
            corner_radius=0.1, width=3.5, height=0.5,
            fill_color=ACCENT_CORAL, fill_opacity=0.2,
            stroke_color=ACCENT_CORAL, stroke_width=1.5,
        )
        hr_text2 = Text("AI Inference & Feedback", font_size=14, color=ACCENT_CORAL).move_to(hr_box2)

        hr_group = VGroup(hr_label, VGroup(hr_box1, hr_text1), VGroup(hr_box2, hr_text2)).arrange(DOWN, buff=0.15)

        # Supporting infrastructure
        si_label = Text("Supporting Infrastructure", font_size=12, color=TEAL, weight=BOLD)
        si_items = ["Curriculum Ingestion", "Orchestration Layer", "User Interface", "Data Storage", "Integration APIs"]
        si_boxes = VGroup()
        for item in si_items:
            box = RoundedRectangle(
                corner_radius=0.08, width=3.5, height=0.4,
                fill_color=TEAL, fill_opacity=0.15,
                stroke_color=TEAL, stroke_width=1,
            )
            txt = Text(item, font_size=12, color=TEAL).move_to(box)
            si_boxes.add(VGroup(box, txt))
        si_boxes.arrange(DOWN, buff=0.06)
        si_group = VGroup(si_label, si_boxes).arrange(DOWN, buff=0.15)

        arch_stack = VGroup(arch_title, hr_group, si_group).arrange(DOWN, buff=0.3)
        arch_stack.move_to(RIGHT * 2.5 + DOWN * 0.3)

        self.play(FadeIn(arch_stack, shift=UP * 0.3), run_time=0.8)
        self.wait(2.5)

        # Highlight: only 2 components are high-risk
        highlight_text = Text(
            "Only 2 of 7 components are high-risk — narrowing the regulatory perimeter.",
            font_size=18, color=ACCENT_GOLD,
        ).move_to(DOWN * 3.2)
        self.play(Write(highlight_text), run_time=0.7)
        self.wait(2)
        self.fade_between()

    # ── ACT 6: Human Oversight ──────────────────────────────────────────────

    def act_human_oversight(self):
        header = self.section_header(
            5, "Human Oversight",
            "Article 14 — enforced by workflow, not policy"
        )

        # Central teacher figure (abstract)
        teacher_circle = Circle(
            radius=0.8, fill_color=NAVY, fill_opacity=0.9,
            stroke_color=TEAL, stroke_width=2,
        ).move_to(ORIGIN)
        teacher_label = Text("THE\nTEACHER", font_size=18, color=WHITE, weight=BOLD).move_to(teacher_circle)
        teacher = VGroup(teacher_circle, teacher_label)

        # Four surrounding responsibilities
        responsibilities = [
            (UP * 2, "Approves Every Item", "No AI output reaches students\nwithout teacher approval"),
            (RIGHT * 3.5, "Overrides AI Judgement", "AI rubric placements are\nalways provisional"),
            (DOWN * 2, "Owns the Record", "Only teacher-confirmed results\nstored as authoritative"),
            (LEFT * 3.5, "Holds Accountability", "Accountability stays with\nthe human, not the algorithm"),
        ]

        resp_mobs = VGroup()
        for pos, title, desc in responsibilities:
            title_t = Text(title, font_size=15, color=ACCENT_GOLD, weight=BOLD)
            desc_t = Text(desc, font_size=12, color=WARM_WHITE, line_spacing=1.2)
            group = VGroup(title_t, desc_t).arrange(DOWN, buff=0.1)
            group.move_to(pos)
            resp_mobs.add(group)

        self.play(FadeIn(teacher, scale=0.8), run_time=0.6)

        # Animate each responsibility with a connecting line
        for resp in resp_mobs:
            line = Line(
                teacher_circle.get_center(),
                resp.get_center(),
                color=TEAL, stroke_width=1, stroke_opacity=0.5,
            )
            self.play(Create(line), FadeIn(resp, shift=OUT * 0.1), run_time=0.4)

        self.wait(1)

        # Bottom callout
        callout = Text(
            "The AI proposes. The teacher decides. That is the architecture.",
            font_size=20, color=TEAL, weight=BOLD,
        ).move_to(DOWN * 3.3)
        self.play(Write(callout), run_time=0.8)
        self.wait(2)
        self.fade_between()

    # ── ACT 7: Explainability ───────────────────────────────────────────────

    def act_explainability(self):
        header = self.section_header(
            6, "Explainability",
            "Calibrated to role and context"
        )

        # Two columns: Teachers vs Students
        def make_column(title, color, items):
            title_t = Text(title, font_size=22, color=color, weight=BOLD)
            rows = VGroup()
            for label, desc in items:
                l = Text(label, font_size=15, color=color, weight=BOLD)
                d = Text(desc, font_size=13, color=WARM_WHITE)
                row = VGroup(l, d).arrange(DOWN, aligned_edge=LEFT, buff=0.05)
                rows.add(row)
            rows.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            col = VGroup(title_t, rows).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            return col

        teacher_col = make_column("FOR TEACHERS", TEAL, [
            ("Full Visibility", "See rubrics, source texts, and AI reasoning"),
            ("Traceable Outputs", "Every item linked to curriculum materials"),
            ("Rejection Signals", "Rejection patterns signal model performance"),
        ])
        student_col = make_column("FOR STUDENTS", ACCENT_CORAL, [
            ("Progressive Reveal", "Rubric shown conditionally after attempt"),
            ("After Genuine Attempt", "Performance bands revealed post-attempt"),
            ("Growth-Oriented", "Feedback for improvement, not terminal judgement"),
        ])

        teacher_col.move_to(LEFT * 3.2 + DOWN * 0.3)
        student_col.move_to(RIGHT * 3.2 + DOWN * 0.3)

        divider = DashedLine(UP * 1.5, DOWN * 2.5, color=MUTED_GREY, stroke_width=1)

        self.play(FadeIn(teacher_col, shift=RIGHT * 0.3), run_time=0.6)
        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(student_col, shift=LEFT * 0.3), run_time=0.6)
        self.wait(2.5)
        self.fade_between()

    # ── ACT 8: Model Selection ──────────────────────────────────────────────

    def act_model_selection(self):
        header = self.section_header(
            7, "Responsible Model Selection",
            "Model choice = governance decision"
        )

        benchmarks = [
            ("MMLU / GPQA", "Knowledge & Reasoning", 0.85),
            ("LongFact", "Factuality & Hallucination", 0.78),
            ("IFEval", "Instruction Following", 0.90),
            ("BBQ", "Bias & Fairness", 0.82),
            ("RTP + Custom", "Toxicity & Safety", 0.88),
        ]

        bars = VGroup()
        for i, (name, category, score) in enumerate(benchmarks):
            # Label
            name_t = Text(name, font_size=14, color=ACCENT_GOLD, weight=BOLD)
            cat_t = Text(category, font_size=12, color=MUTED_GREY)
            label = VGroup(name_t, cat_t).arrange(DOWN, aligned_edge=RIGHT, buff=0.05)
            label.move_to(LEFT * 3)

            # Bar background
            bar_bg = RoundedRectangle(
                corner_radius=0.08, width=6, height=0.35,
                fill_color=NAVY, fill_opacity=0.6, stroke_width=0,
            )
            # Bar fill
            bar_fill = RoundedRectangle(
                corner_radius=0.08, width=6 * score, height=0.35,
                fill_color=TEAL, fill_opacity=0.7, stroke_width=0,
            )
            bar_fill.align_to(bar_bg, LEFT)
            bar_group = VGroup(bar_bg, bar_fill).move_to(RIGHT * 1.5)

            row = VGroup(label, bar_group).arrange(RIGHT, buff=0.4)
            bars.add(row)

        bars.arrange(DOWN, buff=0.3).move_to(DOWN * 0.2)

        for bar in bars:
            self.play(FadeIn(bar, shift=RIGHT * 0.2), run_time=0.35)

        # Footer note
        footer = Text(
            "Zero student data in training  •  Model versions logged for every inference",
            font_size=16, color=TEAL,
        ).move_to(DOWN * 3.0)
        self.play(Write(footer), run_time=0.6)
        self.wait(2)
        self.fade_between()

    # ── ACT 9: Data Governance ──────────────────────────────────────────────

    def act_data_governance(self):
        header = self.section_header(
            8, "Data Governance & Privacy",
            "Data minimisation as a foundational principle"
        )

        stakeholders = [
            ("STUDENTS", TEAL, ["No behavioural profiling", "No sensitive data collected", "Never used for training"]),
            ("TEACHERS", ACCENT_CORAL, ["Assessment records owned", "Rejection data for monitoring", "No performance tracking"]),
            ("PUBLISHERS", ACCENT_GOLD, ["Explicit licensing", "Controlled processing", "No unauthorised derivatives"]),
            ("INSTITUTIONS", MID_BG, ["DPIA-aligned retention", "Full audit trail", "Compliant DPAs"]),
        ]

        cards = VGroup()
        for title, color, items in stakeholders:
            box = RoundedRectangle(
                corner_radius=0.12, width=2.8, height=2.8,
                fill_color=NAVY, fill_opacity=0.85,
                stroke_color=color, stroke_width=1.5,
            )
            title_t = Text(title, font_size=14, color=color, weight=BOLD)
            item_texts = VGroup()
            for item in items:
                dot = Dot(radius=0.03, color=color)
                txt = Text(item, font_size=11, color=WARM_WHITE)
                row = VGroup(dot, txt).arrange(RIGHT, buff=0.15)
                item_texts.add(row)
            item_texts.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
            content = VGroup(title_t, item_texts).arrange(DOWN, buff=0.3)
            card = VGroup(box, content).arrange(ORIGIN)
            cards.add(card)

        cards.arrange(RIGHT, buff=0.3).move_to(DOWN * 0.3)

        for card in cards:
            self.play(FadeIn(card, shift=UP * 0.2), run_time=0.4)

        self.wait(2.5)
        self.fade_between()

    # ── ACT 10: Compliance Moat ─────────────────────────────────────────────

    def act_compliance_moat(self):
        header = self.section_header(
            9, "Why Compliance Is the Moat",
            "Regulation is not friction — it is a filter"
        )

        advantages = [
            ("STRATEGIC\nADVANTAGE", TEAL,
             "EU AI Act will progressively\nexclude non-compliant products"),
            ("INSTITUTIONAL\nVALUE", ACCENT_GOLD,
             "Embedded compliance achieves\nverifiable trustworthiness"),
            ("HUMAN\nIMPACT", ACCENT_CORAL,
             "Teachers retain authority.\nStudents get safer feedback."),
        ]

        cols = VGroup()
        for title, color, desc in advantages:
            # Shield-like shape using rounded rectangle
            shield = RoundedRectangle(
                corner_radius=0.2, width=3.2, height=3.0,
                fill_color=NAVY, fill_opacity=0.85,
                stroke_color=color, stroke_width=2,
            )
            title_t = Text(title, font_size=16, color=color, weight=BOLD, line_spacing=1.2)
            rule = Line(LEFT * 1, RIGHT * 1, color=color, stroke_width=1)
            desc_t = Text(desc, font_size=13, color=WARM_WHITE, line_spacing=1.3)
            content = VGroup(title_t, rule, desc_t).arrange(DOWN, buff=0.25)
            col = VGroup(shield, content).arrange(ORIGIN)
            cols.add(col)

        cols.arrange(RIGHT, buff=0.5).move_to(DOWN * 0.3)

        self.play(
            LaggedStart(*[FadeIn(c, shift=UP * 0.3) for c in cols], lag_ratio=0.3),
            run_time=1.2,
        )
        self.wait(2.5)
        self.fade_between()

    # ── ACT 11: Conclusion ──────────────────────────────────────────────────

    def act_conclusion(self):
        # Big statement
        line1 = Text(
            "High-risk AI in education",
            font_size=36, color=WHITE, weight=BOLD,
        )
        line2 = Text(
            "does not have to mean unsafe AI.",
            font_size=36, color=TEAL, weight=BOLD,
        )
        statement = VGroup(line1, line2).arrange(DOWN, buff=0.15).move_to(UP * 1.5)

        self.play(Write(line1), run_time=0.8)
        self.play(Write(line2), run_time=0.8)
        self.wait(1)

        # Three pillars
        pillars = VGroup()
        for label, color in [
            ("Educationally\nSound", TEAL),
            ("Technically\nRobust", ACCENT_GOLD),
            ("Legally\nDefensible", ACCENT_CORAL),
        ]:
            dot = Circle(
                radius=0.6, fill_color=color, fill_opacity=0.15,
                stroke_color=color, stroke_width=2,
            )
            txt = Text(label, font_size=16, color=color, weight=BOLD, line_spacing=1.2).move_to(dot)
            pillars.add(VGroup(dot, txt))

        pillars.arrange(RIGHT, buff=1.5).move_to(DOWN * 0.5)
        self.play(
            LaggedStart(*[FadeIn(p, scale=0.8) for p in pillars], lag_ratio=0.2),
            run_time=0.8,
        )
        self.wait(1)

        # Final line
        rule = Line(LEFT * 4, RIGHT * 4, color=TEAL, stroke_width=1.5).move_to(DOWN * 1.8)
        final = Text(
            "Diotima: compliance-grade AI that institutions can trust\nand regulators can verify.",
            font_size=22, color=MID_BG, line_spacing=1.4,
        ).move_to(DOWN * 2.5)

        byline = Text(
            "novalconsultancy.com", font_size=16, color=MUTED_GREY,
        ).move_to(DOWN * 3.3)

        self.play(Create(rule), run_time=0.4)
        self.play(Write(final), run_time=0.8)
        self.play(FadeIn(byline), run_time=0.4)
        self.wait(3)

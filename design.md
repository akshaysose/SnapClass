# SnapClass Design Specification

## 1. Product Overview

SnapClass is an AI-assisted attendance application with two primary user journeys:

- Student: identify or register through FaceID, optionally enroll a voice profile, view enrolled subjects, and review attendance.
- Teacher: log in or register with a password, create and share subjects, collect attendance images or audio, run AI analysis, and review attendance records.

The interface should feel friendly, direct, and practical. The visual language combines a bright blue and lavender foundation with high-contrast black, white, and pink actions.

## 2. Design Principles

1. Make the next action obvious. Each screen should have one dominant task and a clear primary button.
2. Separate user roles early. Student and teacher entry points are equal in prominence on the home screen.
3. Use strong visual hierarchy. Display headings identify the current task; supporting labels explain inputs and states.
4. Keep AI operations understandable. Use explicit progress, warning, success, and error feedback around face and voice processing.
5. Preserve context. Dashboard headers, role identity, logout, and navigation remain visible while users work.
6. Prefer compact operational layouts. Attendance workflows should prioritize scanning, selecting, uploading, and confirming over decoration.

## 3. Color System

| Token | Hex | Usage |
| --- | --- | --- |
| Snap blue | `#5865F2` | Home background, primary buttons, active navigation, logo accent |
| Lavender | `#E0E3FF` | Home panels, dashboard and authentication background, subject metadata badges |
| Snap pink | `#EB459E` | Secondary buttons, logout, destructive or high-attention accents, subject-card border |
| Ink | `#25243A` | Dark headings, labels, form text, primary readable content |
| Black | `#000000` | Tertiary buttons and inactive dashboard navigation |
| White | `#FFFFFF` | Button text, dashboard headings, card surfaces, input surfaces |
| Muted slate | `#64748B` | Secondary subject-card metadata |
| Warning pale yellow | `#E9EACB` | Empty-state and caution messaging |

### Contrast Requirements

- White text must only be used on Snap blue, Snap pink, or black surfaces.
- Ink text should be used on lavender and white surfaces.
- Warning text must remain readable against the pale yellow warning surface.
- Do not use the lavender background for long body text without an ink or slate foreground.

## 4. Typography

The current stylesheet imports two Google Fonts:

- `Climate Crisis`: display font for `h1` and `h2`; use for brand-scale and page-level headings.
- `Outfit`: body font for paragraphs, labels, controls, and supporting text.

Recommended hierarchy:

| Element | Treatment |
| --- | --- |
| Brand | `Climate Crisis`, uppercase, compact line height |
| Page heading | `Climate Crisis`, large, short phrase |
| Section heading | `Climate Crisis`, medium size |
| Labels and body | `Outfit`, regular weight, readable line height |
| Buttons | `Outfit`, medium or semibold, concise verb-first labels |
| Metadata | `Outfit`, muted slate, smaller size |

Headings should be short. Avoid placing long explanatory paragraphs in display typography.

## 5. Global Layout

- Streamlit's default top menu, header, and footer are hidden through the shared base stylesheet.
- The main content container uses a small top inset so the brand header has room to breathe.
- Desktop layouts use Streamlit columns for side-by-side role panels, dashboard header/action groups, tab navigation, and two-column content.
- Content should collapse into a single column on narrow screens. Inputs and primary actions must remain full width when columns become too narrow.
- Use consistent horizontal alignment and spacing. Do not let content touch the viewport edges.
- Use dividers to separate navigation from the active workflow and form fields from submit actions.

## 6. Home Screen

### Purpose

Route visitors to either the Student Portal or Teacher Portal.

### Structure

1. Centered SnapClass logo and wordmark.
2. Two equal role panels:
   - `I'm Student`
   - `I'm Teacher`
3. Role mascot image inside each panel.
4. Portal action button with an outward-arrow icon.
5. Centered attribution footer.

### Visual Treatment

- Page background: Snap blue.
- Role panels: Lavender.
- Panels: large rounded corners, generous internal padding, equal visual weight.
- Role headings: dark Ink and display typography.
- Portal buttons: blue primary actions with white text.
- Mascot images should be centered and maintain their aspect ratio.

### Interaction

Clicking Student Portal sets `login_type` to `student`. Clicking Teacher Portal sets `login_type` to `teacher`. The page reruns after the state change.

## 7. Authentication Screens

Authentication includes teacher password login, teacher registration, and student FaceID login.

### Shared Structure

1. Dashboard-style SnapClass header at the top.
2. Pink `Go back to Home` action aligned beside the header.
3. Centered page title.
4. Form or capture control area.
5. Divider before action buttons.
6. Two-action row where applicable.
7. Attribution footer.

### Teacher Login

- Title: `Login using password`.
- Fields: username and password.
- Password input must provide a visibility toggle.
- Primary action: `Login`.
- Alternate action: `Register Instead`.
- Invalid credentials use an error message without clearing the user's input.

### Teacher Registration

- Title: `Register your teacher profile`.
- Fields: username, name, password, and password confirmation.
- Primary action: `Register now`.
- Alternate action: `Login Instead`.
- Validate required fields, duplicate usernames, and password mismatch before submission.
- Success should confirm creation and return the user to login.

### Student FaceID Login

- Title: `Login using FaceID`.
- Use a camera input with a concise positioning instruction.
- Provide distinct states for no face, multiple faces, unrecognized face, and successful recognition.
- On recognition, resolve the student record and enter the student dashboard.
- If no match is found, expose the new-profile registration flow.

### Student Registration

- Use the captured face image as the identity source.
- Ask for the student's name.
- Offer optional voice enrollment with a short spoken phrase.
- The create action should remain disabled or reject submission when the name is missing.
- Show processing feedback while face embeddings and voice embeddings are created.

## 8. Dashboard Shell

The teacher and student dashboards share the same shell:

1. Left or first column: SnapClass dashboard header.
2. Right or second column: welcome message and pink Logout action.
3. Navigation or section content below the header.
4. Footer attribution at the bottom.

### Dashboard Visual Target

- Background: Lavender.
- Welcome text: white and prominent.
- Logout: pink rounded button with a keyboard shortcut indicator where supported.
- Active navigation: Snap blue.
- Inactive navigation: black.
- Navigation labels should include familiar icons and remain readable at equal widths.

## 9. Teacher Dashboard

### Navigation

The main teacher navigation has three equal-width tabs:

- Take Attendance
- Manage Subjects
- Attendance Records

The active tab is blue. Inactive tabs are black. Navigation changes the session state and reruns the page.

### Take Attendance

- Heading: `Take AI Attendance`.
- Select a subject before analysis.
- Provide `Add Photos` as the entry point for camera or upload capture.
- Show captured images in a gallery.
- Allow clearing all photos.
- Keep `Run Face Analysis` unavailable until photos exist.
- Offer voice attendance as a secondary workflow.
- Show clear empty, processing, success, and failure states.

### Manage Subjects

- Show `Create New Subject` as the main action.
- Present subjects as repeated cards.
- Each card should expose the subject name, code, section, and share action.
- When no subjects exist, show an informative empty state with a direct creation action.

### Attendance Records

- Use a scan-friendly table or structured result layout.
- Keep student name, identity, attendance status, timestamp, and source visible where available.
- Confirmation dialogs must distinguish `Discard` from `Confirm & Save`.

## 10. Student Dashboard

- Heading: `Your Enrolled Subjects`.
- Place `Enroll in Subject` beside the heading as the primary action.
- Show enrolled subjects in a responsive two-column grid on desktop and one column on mobile.
- Each subject card includes name, subject code, section, total attendance, attended count, and unenroll action.
- Subject cards use a white surface, pink left accent, dark title, and lavender code badge.
- Destructive unenrollment remains a tertiary black action and should require a clear user gesture.

## 11. Components and Surfaces

### Subject Card

- White background.
- Pink left border for identity and emphasis.
- Small corner radius or a restrained rounded shape; avoid excessive nesting.
- Dark subject title.
- Slate metadata.
- Lavender code badge with blue text.
- Compact attendance statistics with readable labels.

### Dialogs

Dialogs are used for:

- Adding attendance photos.
- Creating subjects.
- Sharing subject codes.
- Enrolling in subjects.
- Auto-enrolling from a join code.
- Confirming attendance results.
- Voice attendance.

Each dialog needs a clear title, one primary action, a dismissal path, and explicit error or success feedback.

### Feedback States

- `st.info`: neutral guidance and optional workflow explanations.
- `st.warning`: missing data, invalid workflow state, or recoverable attention state.
- `st.error`: failed authentication, processing, or synchronization.
- `st.success`: completed creation, enrollment, or save operation.
- `st.spinner`: active AI, database, or model-processing work.

## 12. Interaction and Accessibility

- Every button must use an action-oriented label.
- Icons should support text, not replace important text.
- Keep keyboard shortcuts visible when the application exposes them.
- Inputs require visible labels and useful placeholders.
- Do not rely on color alone to communicate attendance status; pair status with text or an icon.
- Focus states should remain visible against the lavender background.
- Ensure buttons and camera/audio controls are usable on touch screens.
- Preserve entered form values after validation errors where Streamlit state permits.

## 13. Responsive Behavior

### Desktop

- Two-column home role layout.
- Two-column dashboard header.
- Three-column teacher navigation.
- Two-column student subject grid.

### Mobile and Narrow Windows

- Stack role panels vertically.
- Stack dashboard header and logout action.
- Convert teacher navigation to a vertically stacked or horizontally scrollable group without clipped labels.
- Stack subject cards vertically.
- Make form and capture controls full width.
- Keep headings within their containers and allow natural wrapping.

## 14. Motion and States

The current global button treatment uses a subtle scale-up hover transition. Keep motion restrained and functional:

- Button hover: small scale change only.
- Page transitions: rely on Streamlit reruns; do not add distracting animations.
- Loading: use a spinner and preserve the current context.
- Empty states: explain what is missing and provide the next action.

Respect reduced-motion preferences if custom CSS animations are added later.

## 15. Content Guidelines

- Use plain, direct language.
- Prefer `Create Account`, `Register now`, `Run Face Analysis`, and `Confirm & Save` over vague labels.
- Keep spelling consistent: `registered`, `successful`, `attendance`, and `FaceID`.
- Avoid exposing implementation details such as embedding generation in user-facing copy.
- Error messages should explain what happened and what the user can do next.

## 16. Design Tokens and Implementation Notes

The visual system is currently implemented primarily in `src/ui/base_layout.py`, with inline HTML styles in the header, footer, and subject-card components. The role screens compose the layout with Streamlit columns and controls.

Recommended next cleanup steps:

1. Move repeated colors into shared CSS variables.
2. Replace inline header/footer styles with reusable classes.
3. Add stable selectors or classes for auth titles, dashboard navigation, cards, and feedback panels instead of relying only on Streamlit-generated selectors.
4. Keep button semantics consistent: primary blue, secondary pink, tertiary black.
5. Add a small viewport review for home, teacher login, teacher registration, teacher dashboard, student login, and student dashboard.
6. Run `python -m py_compile` on all changed Python modules before launching Streamlit.

## 17. Current Implementation Gaps

This document describes the intended design as well as the current visual conventions. The current source snapshot has some gaps that should be addressed before treating the design as fully implemented:

- The current `base_layout.py` contains the basic blue, lavender, pink, and black button styling but does not include all earlier auth and dashboard-specific selectors.
- The current student screen contains malformed nested-quote f-strings in two toast messages, which can prevent compilation and must be fixed before runtime validation.
- Some labels and messages contain spelling inconsistencies, such as `tihs`, `Succesfully`, and `registerd`.
- Several components use inline CSS, which makes responsive and theme-wide updates harder.
- The dashboard design depends on Streamlit's generated DOM structure in places; stable classes would make future visual maintenance safer.

## 18. Validation Checklist

Before release, verify:

- [ ] Home screen shows equal Student and Teacher entry panels.
- [ ] Student and Teacher portals route to the correct flows.
- [ ] Teacher login and registration render all fields and actions correctly.
- [ ] Student FaceID capture handles all face-count states.
- [ ] Teacher dashboard active and inactive tabs use the intended colors.
- [ ] Student subject cards fit at desktop and mobile widths.
- [ ] Empty, warning, error, success, and loading states are readable.
- [ ] Logout and back-to-home actions clear or update the correct session state.
- [ ] No text is clipped or hidden behind Streamlit controls.
- [ ] Python compilation and a live Streamlit smoke test pass.

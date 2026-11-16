import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(
    page_title="EDU Revolution Assistant",
    page_icon="🎓",
    layout="centered",
)

# -----------------------------
# API configuration
# -----------------------------
def get_api_key():
    try:
        return st.secrets["GEMINI_API_KEY"]
    except Exception:
        return None


# -----------------------------
# EDU Revolution knowledge base
# -----------------------------
MANUAL = """
EDU REVOLUTION GUIDE - LPU

EDU Revolution is LPU's student-centric academic framework for recognizing
and rewarding learning beyond the classroom. It includes Revenue Generation,
Projects and Hackathons, Internships, Certifications, Recognition of Prior
Learning, Community Service and other approved activities.

APPLICATION:
Students can apply through:
UMS -> LMS -> Edu Revolution: Be the Change -> Apply for EDU Revolution.

For guidance, students can visit the EDU-Revolution Query and Assistance Zone,
Block 38-205B.

ACADEMIC BENEFITS:
Students may receive benefits such as:
- Course Equivalence
- Grade Upgradation
- Attendance Benefit
- Duty Leave
- Recognition of Prior Learning (RPL)
- CA/MTT Evaluation Benefits
- Value Addition in Academic Transcript

REVENUE GENERATION:
Revenue Generation means income earned by students through approved
entrepreneurial, professional, technical, creative or service-based activities.

Eligibility:
- No minimum CGPA requirement.
- Revenue must come from University-approved activities.
- Revenue from family-owned businesses is not considered.
- Academic benefit applies only to courses in which the student has passed.
- For attendance benefit, minimum 60% attendance is required.
- Students must appear in End Term Examination irrespective of benefit claimed.
- Revenue proof must be submitted at least 15 days before the last teaching day.

Benefits:
- Revenue above Rs. 1,25,000 may provide complete course equivalence
  for one non-core course.
- Revenue between Rs. 50,000 and Rs. 1,00,000 may provide 10% attendance benefit.
- Revenue between Rs. 1,00,000 and Rs. 5,00,000 may provide 15% attendance benefit.
- Revenue above Rs. 5,00,000 may provide 20% attendance benefit.
- Revenue between Rs. 5,000 and Rs. 10,000 may provide 1 CA equivalence in 1 course.
- Revenue between Rs. 10,000 and Rs. 24,999 may provide 1 CA equivalence in 2 courses.
- Revenue above Rs. 25,000 may be considered for Grade Upgradation
  according to the applicable criteria.

NPTEL / PROCTORED MOOCs / CERTIFICATIONS:
These are structured learning programmes offered by recognized platforms.

Eligibility:
- Course must be completed through a University-approved platform.
- Minimum CGPA 7.0 is required for Complete Course Equivalence.
- No CGPA requirement for Partial Course Equivalence.
- Course content and learning outcomes must be relevant to the mapped course.
- Registration and completion proof must be submitted.
- Course mapping is done by Head of School or designated academic authority.

Benefits may include:
- Complete Course Equivalence.
- Partial Course Equivalence such as CA/MTE/ETE/ETP benefits.

PROJECTS:
A project is an outcome-driven activity to solve a real-world problem,
develop innovation or conduct academic, industry or field research.

Eligibility:
- Minimum CGPA 6.0.
- Minimum 65% attendance is required for Duty Leave benefits.
- Prior approval of Standing Committee is required if project work occurs
  during scheduled class hours.
- Complete documentation must be submitted and verified.

Possible benefits:
- Course Equivalence up to maximum 2 courses.
- 1 or 2 CA Equivalence, up to maximum 3 courses.
- 10% Attendance Relaxation or 30 Hours Duty Leave.

INTERNSHIP BEYOND CURRICULUM:
An internship is a supervised work-based learning experience providing
practical skills and industry exposure.

Eligibility:
- Normally minimum CGPA 6.0.
- Exceptional internships may be considered even if CGPA is below 6.
- Prior Standing Committee approval is required if internship takes place
  during scheduled class hours.
- Minimum 65% attendance is required for Duty Leave benefits.
- Nominations are verified by the Standing Committee.
- Students are advised to undertake internships during breaks,
  off-hours or weekends where possible.

Important:
If total internship stipend exceeds Rs. 1,00,000, the student may be considered
for complete course waiver against a course approved by the Standing Committee.

Benefits depend on:
- Internship duration
- Monthly stipend
- Type and level of organization

Benefits may include:
- Full marks in CA
- Full marks in CA and MTE
- Grade Upgradation
- Course exemption
- Duty Leave

RECOGNITION OF PRIOR LEARNING - RPL:
RPL recognizes knowledge and competencies already acquired through
formal, informal or experiential learning.

Eligibility:
- Student must be an active University student.
- Minimum CGPA 5.0.
- Relevant and verifiable evidence of prior learning is required.
- Where applicable, learning duration should be at least 12 hours.
- Application must normally be submitted before the academic term starts
  or within two weeks from start of classes.
- Maximum two RPL applications can be submitted in one academic term.
- Course exemption may be granted for only one course per academic term.

For complete course waiver:
- RPL application must first be approved.
- Student must appear in RPL examination.
- Student must secure at least B+ grade.

Examples of prior learning:
- IELTS, TOEFL, DELF/DALF, JLPT
- AWS, Azure, Google Cloud, SAP, Cisco, Oracle
- Work experience and internships
- NPTEL/SWAYAM courses
- Professional training and workshops

GRADE UPGRADATION:
Grade Upgradation improves a student's course grade based on eligible
academic, research or co-curricular achievements.

Eligibility:
- Minimum CGPA 5.0.
- Benefit must be claimed before programme completion and before
  final marksheet is issued.
- Benefit is given only in mapped courses approved through the process.

Examples:
Patent:
- Patent Granted -> O Grade, up to maximum 4 credits.
- Patent Published -> Two grades up, maximum A+, up to 4 credits.
- Patent Filed -> One grade up, maximum A, up to 4 credits.

Research Publication:
- Q1 Scopus Publication -> O Grade, up to 4 credits.
- Q2 Publication -> Two grades up, maximum A+, up to 4 credits.
- Q3/Q4/Book Chapter/Conference Paper -> One grade up,
  maximum A, up to 4 credits.

Other eligible categories may include:
- Copyright/Design
- Technical Competitions/Hackathons
- Certifications
- Proctored Certifications
- Recruitment Exams
- Full-Term Paid Internship/Placement
- Industry Grade Assessment

COMMUNITY SERVICE:
Community Service means voluntary and unpaid work for society,
communities, individuals, animals or the environment.

Eligibility:
- Service must be undertaken with an organization/NGO eligible under
  Section 80G or another University-approved organization.
- Minimum 80 hours of community service in a semester/term.
- Activity must be different from work done as part of a credited CDP course.
- Complete documentation and verification are required.

Documents should include:
- Geo-tagged photographs
- Activity details
- Certificate from NGO/organization showing duration and nature of service

Benefits:
- First-Year UG Students:
  Course Equivalence / Exemption in Community Development Project course.
- Other Students:
  One Grade Upgradation in Community Development Project course.

UP TO 10% ATTENDANCE BENEFIT:
Attendance Benefit provides eligible students up to 10% attendance relaxation
for approved academic, professional, recruitment, examination, research,
innovation or entrepreneurship activities.

Eligibility:
- Minimum CGPA 7.5 by end of term.
- Minimum 65% aggregate attendance excluding bonus attendance.
- No record of indiscipline.
- Normally available to pre-final and final-year students for programmes
  longer than three years; otherwise final-year students.

Important:
- Benefit is UP TO 10%; it is not automatically 10%.
- Actual benefit depends on duration, nature and relevance of activity.
- Benefit is credited at the end of the term after verification.
- Student cannot choose the course in which attendance benefit is credited.

DUTY LEAVE:
Duty Leave is attendance relaxation for participation in approved activities
conducted during scheduled class hours.

Eligibility:
- Minimum 60% attendance excluding bonus attendance and Duty Leave.
- No record of indiscipline.
- Recruitment/competitive examination must be relevant to student's programme.
- Supporting documents must be verified.
- Standing Committee approval is required.

Important:
- Applying does not guarantee Duty Leave.
- Final decision rests with the Standing Committee.
- For approved recruitment/competitive examinations, Duty Leave may cover
  examination and travelling days subject to valid proof.
- Maximum 3 days Duty Leave may be granted for such examinations.

STANDING COMMITTEE:
The Head of School constitutes a Standing Committee.

- Normally consists of 5 to 7 members.
- It reviews student nominations.
- It verifies supporting documents.
- It assesses eligibility.
- It recommends appropriate academic benefits.
- Decisions should maintain transparency, consistency and fairness.
"""

SYSTEM_INSTRUCTION = """
You are the EDU Revolution Assistant for Lovely Professional University (LPU).

Answer student questions using only the EDU Revolution guide provided in the
conversation. Be accurate, clear, practical, and student-friendly.

Rules:
1. Treat the supplied guide as the primary source of truth. Do not invent
   university policies, eligibility rules, deadlines, benefits, forms, or contacts.
2. If the guide does not contain the answer, say that the information is not
   specified in the available guide and recommend confirming it with the
   EDU-Revolution Query and Assistance Zone, Block 38-205B, or the relevant
   University authority.
3. Distinguish between "may be eligible" and "is guaranteed". Benefits require
   verification and/or approval where the guide says so.
4. When answering eligibility questions, list all relevant conditions,
   attendance/CGPA requirements, documentation, approvals, and deadlines.
5. If a student's situation is missing key details, ask concise follow-up
   questions instead of assuming.
6. For numerical thresholds, reproduce the values accurately and explain
   boundary conditions carefully. If the guide contains overlapping,
   inconsistent, or unclear ranges, point out the ambiguity rather than
   silently resolving it.
7. Do not claim to submit applications, verify documents, or make official
   decisions. You provide guidance only.
8. Prefer short headings and bullet points. Give a direct answer first.
9. If asked about topics unrelated to EDU Revolution, politely explain that
   this assistant is designed to answer EDU Revolution questions.
"""

# -----------------------------
# Gemini client
# -----------------------------
api_key = get_api_key()

st.title("🎓 EDU Revolution Assistant")
st.caption("Your LPU guide to eligibility, applications, academic benefits and documentation.")

with st.sidebar:
    st.header("About this assistant")
    st.write(
        "Ask questions about EDU Revolution using the information in the "
        "included LPU guide."
    )
    st.divider()
    st.info(
        "This chatbot provides guidance, not official approval. Confirm "
        "your case with the University before relying on a benefit."
    )
    if st.button("Clear conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

if not api_key or api_key == "PASTE_YOUR_GEMINI_API_KEY_HERE":
    st.error(
        "Gemini API key not configured. Open `.streamlit/secrets.toml` and "
        "replace the placeholder with your API key, then restart the app."
    )
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Render previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask about EDU Revolution…")

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Checking the EDU Revolution guide..."):
            try:
                client = genai.Client(api_key=api_key)

                # Keep the current conversation for context, while attaching
                # the official guide and instructions to each request.
                conversation = []
                for item in st.session_state.messages:
                    role = "user" if item["role"] == "user" else "model"
                    conversation.append(
                        types.Content(
                            role=role,
                            parts=[types.Part.from_text(text=item["content"])],
                        )
                    )

                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=conversation,
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_INSTRUCTION
                        + "\n\nKNOWLEDGE BASE:\n"
                        + MANUAL,
                        temperature=0.2,
                    ),
                )

                answer = response.text or (
                    "I couldn't generate a text response. Please try asking "
                    "your question in a different way."
                )
            except Exception as exc:
                answer = (
                    "Sorry, I couldn't connect to Gemini. Check your API key, "
                    "internet connection, model availability, and installed "
                    "package version.\n\n"
                    f"Technical detail: `{type(exc).__name__}: {exc}`"
                )

        st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

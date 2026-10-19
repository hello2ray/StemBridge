import streamlit as st
from datetime import date
from html import escape

st.set_page_config(page_title='StemBridge | Patient Journey', page_icon='💙', layout='wide', initial_sidebar_state='expanded')
st.markdown('''<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Outfit:wght@400;500;600;700;800&display=swap');
:root{--teal:#067f83;--navy:#18354a;--muted:#66798a}
html,body,[class*="css"],.stApp{font-family:'DM Sans',sans-serif}
.stApp{background:linear-gradient(120deg,#f5fbfc 0%,#f8fafc 55%,#f4f4ff 100%);color:#18354a}
.block-container{max-width:1160px;padding-top:1.7rem;padding-bottom:2rem}
h1,h2,h3{font-family:'Outfit',sans-serif!important;color:#18354a!important;letter-spacing:-.025em}
h1{font-weight:800!important}h3{font-weight:700!important}
[data-testid="stSidebar"]{background:linear-gradient(175deg,#103c51,#115e69 75%,#177f80)}
[data-testid="stSidebar"] *{color:#f4fbff!important}
[data-testid="stSidebar"] button{background:rgba(255,255,255,.08)!important;border:1px solid rgba(255,255,255,.16)!important;text-align:left}
[data-testid="stSidebar"] button:hover{background:rgba(255,255,255,.20)!important}
[data-testid="stSidebar"] [data-testid="stAlert"]{background:rgba(255,255,255,.10)!important}
.stButton>button[kind="primary"],button[data-testid="stBaseButton-primary"]{background:linear-gradient(110deg,#078b8e,#13a99d)!important;border:0!important;color:white!important;box-shadow:0 5px 15px #0b939226}
.stButton>button{border-radius:13px!important;min-height:43px;font-weight:700;border:1px solid #d8e8ea;background:#fff;color:#184559}
.stButton>button:hover{border-color:#0b9d9b;color:#087e83}
[data-testid="stMetric"]{border-radius:17px;background:#fff;padding:18px;border:1px solid #e6edf1;box-shadow:0 8px 24px #174a5610}
[data-testid="stMetricValue"]{color:#067f83;font-family:'Outfit',sans-serif}
[data-testid="stVerticalBlockBorderWrapper"]{border-radius:16px}
[data-testid="stForm"]{border-radius:17px;background:#fff;border:1px solid #e1ebed}
.hero{padding:33px 34px;border-radius:24px;background:linear-gradient(112deg,#113e53 0%,#096b75 65%,#0b9c91 100%);color:white;box-shadow:0 18px 35px #0a697528;margin-bottom:22px;position:relative;overflow:hidden}
.hero:after{content:'✦';position:absolute;right:55px;top:-50px;font-size:190px;opacity:.08}
.hero h1,.hero h2,.hero h3,.hero p{color:white!important;margin:0 0 10px}
.hero h1{font-size:2.6rem}.hero p{max-width:690px;line-height:1.65;opacity:.92}
.eyebrow{font-size:.73rem;letter-spacing:.15em;text-transform:uppercase;font-weight:800;color:#0a9090;margin-bottom:9px}
.hero .eyebrow{color:#b6f6e9}
.tile{background:white;border:1px solid #e4ecef;border-radius:19px;padding:21px;min-height:124px;box-shadow:0 8px 22px #123a4a0b;margin:4px 0 12px}
.tile .symbol{font-size:1.6rem;margin-bottom:9px}.tile h4{font-family:'Outfit',sans-serif;font-size:1.12rem;color:#18354a;margin:0 0 5px}.tile p{color:#65798a;font-size:.89rem;line-height:1.5;margin:0}
.section-intro{color:#6c8090;margin-top:-8px;margin-bottom:19px}
.soft-banner{background:#e9f7f5;border:1px solid #ccebe5;border-radius:16px;padding:15px 20px;margin:15px 0;color:#176a69}
.tag{display:inline-block;padding:6px 12px;border-radius:50px;background:#e6f6f3;color:#0b817d;font-size:.77rem;font-weight:800}
.campaign{border:1px solid #d7eae9;border-radius:20px;padding:23px;background:linear-gradient(130deg,#fff,#eefbf8)}
.campaign h3{margin-top:6px}.campaign p{color:#566e7a}
.small-note{font-size:.82rem;color:#71818e}
[data-testid="stTabs"] button{font-weight:700}
</style>''',unsafe_allow_html=True)

# Fictional patient profiles for classroom demonstration only.
DEMO_PATIENTS = {
    'Alex Morgan': {'id':'SB-1001','age':38,'type':'Allogeneic (donor)','condition':'Acute leukemia (fictional)','stage':'Pre-transplant evaluation','day':'Before Day 0','caregiver':'Jordan Morgan','completed':11,'visit':'Thursday, 2:00 PM','status':'Preparing for transplant'},
    'Priya Shah': {'id':'SB-1002','age':46,'type':'Autologous (own cells)','condition':'Multiple myeloma (fictional)','stage':'Conditioning & admission','day':'Before Day 0','caregiver':'Sam Shah','completed':14,'visit':'Friday, 10:30 AM','status':'Conditioning stage'},
    'Daniel Brooks': {'id':'SB-1003','age':52,'type':'Allogeneic (donor)','condition':'Myelodysplastic syndrome (fictional)','stage':'Engraftment & early recovery','day':'Day +18 (example)','caregiver':'Taylor Brooks','completed':19,'visit':'Monday, 9:00 AM','status':'Early recovery'},
    'Maya Chen': {'id':'SB-1004','age':29,'type':'Autologous (own cells)','condition':'Lymphoma (fictional)','stage':'Follow-up & long-term recovery','day':'Day +110 (example)','caregiver':'Lee Chen','completed':23,'visit':'Wednesday, 11:00 AM','status':'Follow-up stage'},
}

# Fictional login credentials for a local classroom demonstration only.
# Do not use these hardcoded credentials or Streamlit session state for real health data.
DEMO_ACCOUNTS = {
    'alex': ('Alex Morgan', 'Alex2026!'),
    'priya': ('Priya Shah', 'Priya2026!'),
    'daniel': ('Daniel Brooks', 'Daniel2026!'),
    'maya': ('Maya Chen', 'Maya2026!'),
}

def reset_patient_session():
    # Prevent another demo account from seeing notes, tasks, chat or journey state.
    for key in list(st.session_state.keys()):
        if key not in ('page', 'logged_in'):
            del st.session_state[key]
    st.session_state.logged_in = False
    st.session_state.page = 'Login'

def selected_patient():
    return DEMO_PATIENTS[st.session_state.patient_name]

def patient_banner():
    p=selected_patient()
    st.markdown(f'<div class="soft-banner"><b>👤 {escape(st.session_state.patient_name)}</b> &nbsp; · &nbsp; {escape(p["type"])} &nbsp; · &nbsp; {escape(p["stage"])} &nbsp; · &nbsp; {escape(p["day"])}</div>',unsafe_allow_html=True)

PAGES=['Today','Journey','My Care','Chat','Caregiver','Finance','Match Finder','Support']
def init(key,value):
    if key not in st.session_state: st.session_state[key]=value
init('page','Login');init('role','Patient');init('logged_in',False);init('patient_journey_data',{})
init('tasks',{'Review appointment questions':False,'Check travel arrangements':False,'Prepare insurance documents':False})
init('questions',['What should I ask at my next appointment?']);init('symptoms',[]);init('chat',[])
init('permission',True)
init('finance',{'Check insurance coverage':'Not started','Collect assistance documents':'In progress','Ask about travel support':'Not started'})
init('campaigns',[]);init('demo_pledges',{})

def go(page):st.session_state.page=page;st.rerun()
def hero(title,subtitle,eyebrow='YOUR STEMBRIDGE SPACE'):
    st.markdown(f'<div class="hero"><div class="eyebrow">{escape(eyebrow)}</div><h1>{escape(title)}</h1><p>{escape(subtitle)}</p></div>',unsafe_allow_html=True)
def tile(icon,title,body):
    st.markdown(f'<div class="tile"><div class="symbol">{icon}</div><h4>{escape(title)}</h4><p>{escape(body)}</p></div>',unsafe_allow_html=True)
def heading(title,sub=''):
    st.title(title)
    if sub:st.markdown(f'<div class="section-intro">{escape(sub)}</div>',unsafe_allow_html=True)
def task_editor(prefix):
    for i,(task,done) in enumerate(list(st.session_state.tasks.items())):
        st.session_state.tasks[task]=st.checkbox(task,value=done,key=f'{prefix}task{i}')
    with st.form(prefix+'addtask',clear_on_submit=True):
        t=st.text_input('Add a task',placeholder='e.g., Arrange a ride')
        if st.form_submit_button('Add task') and t.strip():st.session_state.tasks[t.strip()]=False;st.rerun()

with st.sidebar:
    st.markdown('## 💠 StemBridge')
    st.caption('ONE COORDINATED TRANSPLANT JOURNEY')
    if st.session_state.logged_in:
        st.markdown(f'**👤 {st.session_state.patient_name}**')
        st.caption('Fictional demo profile')
        st.caption('Your private patient view (demo only)')
        st.markdown('##### EXPLORE THE APP')
        icons={'Welcome':'🏠','Today':'☀️','Journey':'🧭','My Care':'💗','Chat':'💬','Caregiver':'🤝','Finance':'💳','Match Finder':'🔎','Support':'🌿'}
        for p in PAGES:
            if st.button(f'{icons[p]}  {p}',use_container_width=True,key='nav_'+p,type='primary' if st.session_state.page==p else 'secondary'):go(p)
        st.divider()
        if st.button('🚪 Log out',use_container_width=True):
            reset_patient_session();st.rerun()
    else:
        st.caption('Sign in with your own fictional demo account.')
    st.divider()
    st.caption('✦ Interactive concept • Fictional data')
    st.caption('Classroom demo only. Login is not production-grade security; never enter real patient data.')

page=st.session_state.page
if page=='Login':
    hero('Welcome to StemBridge','Sign in to see only your own transplant journey and tasks.','PATIENT LOGIN • FICTIONAL DEMO')
    left,right=st.columns([1.3,1],gap='large')
    with left:
        with st.form('patient_sign_in'):
            st.subheader('🔒 Sign in to my journey')
            username=st.text_input('Username',placeholder='Your demo username').strip().lower()
            password=st.text_input('Password',type='password',placeholder='Your demo password')
            submitted=st.form_submit_button('Sign in →',type='primary',use_container_width=True)
            if submitted:
                account=DEMO_ACCOUNTS.get(username)
                if account and password==account[1]:
                    reset_patient_session()
                    st.session_state.patient_name=account[0]
                    st.session_state.logged_in=True
                    st.session_state.role='Patient'
                    st.session_state.page='Today'
                    st.rerun()
                else:
                    st.error('Incorrect username or password.')
        st.info('Demo accounts: alex / Alex2026!  •  priya / Priya2026!  •  daniel / Daniel2026!  •  maya / Maya2026!')
    with right:
        tile('🧭','Your journey only','After sign-in, you see your own stage, milestones and remaining steps. No other patient profiles are shown.')
        tile('🛡️','Prototype privacy','Fictional accounts and sample records only. Real use needs secure authentication, database-level access controls and a privacy review.')
elif not st.session_state.logged_in:
    st.session_state.page='Login';st.rerun()
elif page=='Welcome':
    hero('Your journey. A little clearer.','A calm place to organize transplant milestones, care tasks, caregiver help, donor-search questions, and financial support.','WELCOME TO STEMBRIDGE')
    a,b,c=st.columns(3)
    with a:tile('🧭','Know what comes next','Follow the journey and keep track of daily priorities.')
    with b:tile('🤝','Stay connected','Coordinate with caregivers while keeping control of sharing.')
    with c:tile('💚','Find practical support','Organize financial needs and prepare a demo support campaign.')
    if st.button('Explore my dashboard  →',type='primary'):go('Today')
    st.caption('Designed for early usability testing. No real patient information or integrations.')
elif page=='Today':
    hero(f'Hello, {st.session_state.patient_name.split()[0]} 👋','Here are your next steps. One thing at a time.','TODAY • FICTIONAL PATIENT')
    patient_banner()
    a,b,c=st.columns(3)
    with a:st.metric('Tasks remaining',sum(not x for x in st.session_state.tasks.values()))
    with b:st.metric('Next visit',selected_patient()['visit'].split(',')[0])
    with c:st.metric('Current stage',selected_patient()['stage'])
    st.markdown('### Your priorities')
    left,right=st.columns([1.4,1],gap='large')
    with left:
        with st.container(border=True):task_editor('today_')
    with right:
        tile('📅','Care-team review',selected_patient()['visit']+' • Example appointment')
        tile('💡','A helpful reminder','Your care team is responsible for medical decisions.')
    st.markdown('### Quick access')
    cols=st.columns(4)
    for col,p in zip(cols,['Journey','Caregiver','Finance','Match Finder']):
        with col:
            if st.button(icons[p]+' '+p+' →',use_container_width=True,key='quick_'+p):go(p)
elif page=='Journey':
    hero('Your transplant journey', 'Follow the steps, see what is done, and know what may come next.', 'JOURNEY TRACKER • EXAMPLE ONLY')
    patient_banner()
    st.info('This example shows a possible **blood-forming stem cell transplant (HSCT)** journey. The exact steps and timing depend on the diagnosis, transplant type, and care team. This is not a medical checklist or treatment plan.')

    journey = [
        ('1. Consultation & decision', 'Meet the transplant team and understand the plan', [
            ('Initial transplant consultation','Discuss goals, options, and risks with the care team'),
            ('Review medical history and diagnosis','Confirm the condition and prior treatment with clinicians'),
            ('Discuss transplant type','Autologous (own cells) or allogeneic (donor cells), as applicable'),
            ('Discuss consent and care plan','Ask questions and review the informed-consent process')]),
        ('2. Donor / cell-source planning', 'Confirm where the stem cells will come from', [
            ('Identify stem-cell source','Bone marrow, peripheral blood, or cord blood, as appropriate'),
            ('Donor search and HLA typing (if needed)','For donor transplants, the clinical team manages matching'),
            ('Confirm collection plan','The team arranges donor or patient cell collection')]),
        ('3. Pre-transplant evaluation', 'Prepare for treatment and practical needs', [
            ('Pre-transplant tests','Care team may order blood tests, heart/lung tests, and infection screening'),
            ('Medication and infection-prevention review','Review current medicines and the center’s guidance'),
            ('Caregiver and transport plan','Identify help with visits, transport, and daily needs'),
            ('Insurance and financial review','Check coverage, lodging, and assistance options'),
            ('Admission and schedule review','Confirm where and when care will take place')]),
        ('4. Conditioning & admission', 'Prepare the body for transplant', [
            ('Admission or outpatient setup','Follow the center’s specific care plan'),
            ('Conditioning treatment','Chemotherapy and sometimes radiation, depending on the plan'),
            ('Supportive care planning','Discuss nausea prevention, infection precautions, and monitoring')]),
        ('5. Transplant day (Day 0)', 'Stem cells are infused', [
            ('Stem-cell infusion','The care team administers the collected cells'),
            ('Infusion monitoring','The team monitors for reactions and provides supportive care')]),
        ('6. Engraftment & early recovery', 'Wait for new blood cells to recover', [
            ('Blood-count monitoring','The team tracks blood-cell recovery and transfusion needs'),
            ('Infection and complication monitoring','The team checks for fever and other complications'),
            ('Engraftment assessment','Clinicians determine when blood-cell recovery is established'),
            ('Discharge preparation','Review medicines, warning signs, and follow-up instructions')]),
        ('7. Follow-up & long-term recovery', 'Continue recovery with the care team', [
            ('Early follow-up visits','Attend scheduled checks after discharge'),
            ('Medication and symptom review','Follow the center’s instructions and report concerns'),
            ('Day +30 / +100 reviews (if scheduled)','Common review milestones at some centers, not universal'),
            ('Long-term monitoring','Discuss immune recovery, vaccines, late effects, and survivorship'),
            ('GVHD monitoring (donor transplant only)','Watch for graft-versus-host disease as directed by clinicians')])
    ]
    profile=selected_patient()
    if profile['type'].startswith('Autologous'):
        journey=[(stage,summary,[(title,desc) for title,desc in steps if title not in ('Donor search and HLA typing (if needed)','GVHD monitoring (donor transplant only)')]) for stage,summary,steps in journey]
    all_titles=[title for _,_,steps in journey for title,_ in steps]
    # Demo progress is profile-specific and held separately for each sample patient.
    profile_progress=st.session_state.patient_journey_data
    if st.session_state.patient_name not in profile_progress:
        profile_progress[st.session_state.patient_name]=all_titles[:profile['completed']]
    st.session_state.journey_done=profile_progress[st.session_state.patient_name]
    init('journey_notes', {})
    all_steps = [(stage, title, desc) for stage, _, steps in journey for title, desc in steps]
    done = set(st.session_state.journey_done)
    completed = sum(title in done for _, title, _ in all_steps)
    total = len(all_steps)
    remaining = total - completed
    stage_complete = [sum(title in done for title, _ in steps) for _, _, steps in journey]
    current_idx = next((i for i, (_, _, steps) in enumerate(journey) if any(title not in done for title, _ in steps)), len(journey)-1)

    a, b, c, d = st.columns(4)
    with a: st.metric('Completed', f'{completed} / {total}')
    with b: st.metric('Remaining', remaining)
    with c: st.metric('Example progress', f'{round(100*completed/total)}%')
    with d: st.metric('Current stage', f'{current_idx+1} of {len(journey)}')
    st.progress(completed/total)
    st.caption('Progress counts the example checklist only. It does not measure medical recovery or readiness.')
    st.markdown('### Patient status')
    st.write(f'**Patient:** {st.session_state.patient_name} · **Demo ID:** {profile["id"]} · **Age:** {profile["age"]}')
    st.write(f'**Transplant:** {profile["type"]} · **Current status:** {profile["status"]}')
    st.write(f'**Caregiver:** {profile["caregiver"]} · **Next example appointment:** {profile["visit"]}')
    st.markdown('### Journey stages')
    for i, (stage, summary, steps) in enumerate(journey):
        n=stage_complete[i]
        label = '✓' if n==len(steps) else '●' if n else '○'
        with st.expander(f'{label}  {stage}   •   {n}/{len(steps)} complete', expanded=(i==current_idx)):
            st.caption(summary)
            st.progress(n/len(steps))
            for title, desc in steps:
                checked = st.checkbox(title, value=(title in done), key='journey_'+str(i)+'_'+str(steps.index((title,desc))), help=desc)
                if checked: done.add(title)
                else: done.discard(title)
                st.caption('↳ '+desc)
    if done != set(st.session_state.journey_done):
        st.session_state.journey_done=list(done)
        st.session_state.patient_journey_data[st.session_state.patient_name]=list(done)
        st.rerun()
    st.divider()
    st.markdown('### What is next?')
    next_steps=[(stage,title) for stage,title,_ in all_steps if title not in done]
    if next_steps:
        for stage,title in next_steps[:3]:
            st.write(f'☐ **{title}**  ·  {stage}')
    else:
        st.success('All example items are checked. Your clinical team decides your actual follow-up plan.')
    left,right=st.columns(2)
    with left:
        if st.button('💗 Open My Care', use_container_width=True):go('My Care')
    with right:
        if st.button('🔎 Open Match Finder', use_container_width=True):go('Match Finder')
    st.warning('If you have fever or other urgent symptoms during transplant care, follow your transplant center’s urgent-contact instructions. This demo cannot assess medical risk.')
    st.caption('Optional steps differ: donor search and GVHD monitoring mainly concern allogeneic transplant. Autologous transplants use the patient’s own cells. Checkboxes are for demonstration and can be changed manually.')
elif page=='My Care':
    heading('💗 My Care','Appointments, notes, and questions—together in one place.')
    t1,t2,t3=st.tabs(['📅 Appointments','📝 Symptoms / notes','❓ Care-team questions'])
    with t1:
        tile('🩺','Transplant care-team review','Thursday • 2:00 PM • Demo appointment')
        st.write('Bring your question list and any documents your care team requested.')
    with t2:
        with st.form('symptom_form',clear_on_submit=True):
            d=st.date_input('Date',value=date.today());note=st.text_area('Note for your care team')
            if st.form_submit_button('Save note') and note.strip():st.session_state.symptoms.append((str(d),note.strip()));st.rerun()
        for d,n in reversed(st.session_state.symptoms):st.write(f'**{d}:** {n}')
        st.warning('This app cannot assess symptoms. For urgent concerns, contact your care team or emergency services.')
    with t3:
        for q in st.session_state.questions:st.write('• '+q)
        with st.form('q_form',clear_on_submit=True):
            q=st.text_input('Add a question')
            if st.form_submit_button('Save question') and q.strip():st.session_state.questions.append(q.strip());st.rerun()
elif page=='Chat':
    heading('💬 Ask StemBridge','A friendly demo guide for general questions. No real AI or medical advice.')
    st.info('Try asking about appointments, caregivers, the journey, donor registries, or financial support.')
    answers={'caregiver':'A caregiver can help with rides, daily tasks, and reminders. You decide what to share.','appointment':'Write down questions and confirm details with your care team.','donor':'Your transplant team and authorized registries manage donor searches. This demo does not match donors.','match':'Only authorized professionals can assess donor suitability. Use Match Finder to organize questions.','campaign':'The Finance page lets you draft a sample support campaign. It does not publish a fundraiser or collect money.','financial':'Use Finance to track coverage questions, paperwork, and a sample support campaign.','insurance':'Ask your insurer or financial navigator to confirm coverage and requirements.','journey':'The Journey page shows a sample timeline. Your care team determines your treatment plan.'}
    for role,msg in st.session_state.chat:
        with st.chat_message(role):st.write(msg)
    prompt=st.chat_input('Ask a general question…')
    if prompt:
        st.session_state.chat.append(('user',prompt))
        reply=next((v for k,v in answers.items() if k in prompt.lower()),'I can help organize questions and guide you to the right page. Please ask your care team for medical advice.')
        st.session_state.chat.append(('assistant',reply));st.rerun()
elif page=='Caregiver':
    heading('🤝 Caregiver coordination','Share practical tasks while keeping patient choice at the center.')
    if st.session_state.role=='Patient':
        st.session_state.permission=st.toggle('Allow caregiver to see shared tasks',value=st.session_state.permission)
        st.caption('Demonstration only; this is not a real identity or access-control system.')
    elif not st.session_state.permission:st.warning('Caregiver task sharing is off in this demo.')
    if st.session_state.role=='Patient' or st.session_state.permission:
        with st.container(border=True):task_editor('care_')
    st.caption('No donor identities or private medical records are shown to caregivers.')
elif page=='Finance':
    hero('Finance & support','Keep paperwork organized and explore ways family and friends might help.','PRACTICAL SUPPORT')
    tab1,tab2=st.tabs(['📋 Coverage & assistance','💚 Support campaign'])
    with tab1:
        st.markdown('### Your finance checklist')
        options=['Not started','In progress','Submitted','Waiting for response','Completed']
        for i,(item,status) in enumerate(list(st.session_state.finance.items())):
            a,b=st.columns([3,2]);a.write('**'+item+'**')
            st.session_state.finance[item]=b.selectbox('Status',options,index=options.index(status),key=f'fin{i}',label_visibility='collapsed')
        st.markdown('### Questions for a financial navigator')
        st.write('• Which costs may be covered?  \n• What documents are needed?  \n• Is help available for travel or lodging?')
        st.warning('Submitted does not mean approved. Coverage and financial assistance are not guaranteed.')
    with tab2:
        st.markdown('### Create a support campaign')
        st.write('Draft a simple fundraising page for practical needs such as travel, temporary housing, or other expenses. **This is a private demo preview, not a real fundraiser.**')
        with st.form('campaign_form',clear_on_submit=True):
            title=st.text_input('Campaign title',placeholder='Help with travel and temporary housing')
            purpose=st.selectbox('What is the support for?',['Travel and transportation','Temporary housing','Meals and daily needs','Other practical expenses'])
            goal=st.number_input('Target amount (USD, example only)',min_value=100,max_value=100000,step=100,value=2500)
            story=st.text_area('Short message to supporters',placeholder='Explain the practical need without sharing private medical details.',height=110)
            consent=st.checkbox('I understand this is a demo. I will not enter real patient details or payment information.')
            submitted=st.form_submit_button('Create demo campaign',type='primary')
            if submitted:
                if not title.strip() or not story.strip():st.error('Please enter a title and short message.')
                elif not consent:st.error('Please confirm the demo-only notice.')
                else:
                    st.session_state.campaigns.append({'id':len(st.session_state.campaigns)+1,'title':title.strip(),'purpose':purpose,'goal':int(goal),'story':story.strip()})
                    st.success('Campaign preview created locally in this demo. Nothing has been published.')
        if st.session_state.campaigns:
            st.markdown('### Your campaign previews')
            for campaign in reversed(st.session_state.campaigns):
                cid=campaign['id'];raised=st.session_state.demo_pledges.get(cid,0)
                with st.container(border=True):
                    st.markdown('<span class="tag">DRAFT • NOT PUBLIC</span>',unsafe_allow_html=True)
                    st.subheader('💚 '+campaign['title'])
                    st.caption(campaign['purpose'])
                    st.write(campaign['story'])
                    a,b=st.columns(2)
                    with a:st.metric('Sample support',f'${raised:,}')
                    with b:st.metric('Example goal',f"${campaign['goal']:,}")
                    st.progress(min(raised/campaign['goal'],1.0))
                    st.caption('Sample amounts only. No payments, pledges, donors, or transfers are recorded.')
                    if st.button('Simulate $50 of support',key=f'pledge_{cid}'):
                        st.session_state.demo_pledges[cid]=raised+50;st.rerun()
                    if st.button('Remove draft',key=f'remove_{cid}'):
                        st.session_state.campaigns=[x for x in st.session_state.campaigns if x['id']!=cid];st.session_state.demo_pledges.pop(cid,None);st.rerun()
        st.info('A real fundraising feature would need patient consent, privacy review, identity verification, secure payment processing, fraud safeguards, and clear terms before launch.')
elif page=='Match Finder':
    hero('Donor-search guide','Know which questions to ask and where to find trusted answers.','MATCH FINDER • GUIDANCE ONLY')
    st.warning('This prototype cannot search registries, rank donors, or determine compatibility. Only authorized transplant professionals can do that.')
    for title,detail in [('01  Talk with your transplant team','Ask whether a donor search is part of the treatment plan.'),('02  Understand registry coordination','The transplant team may work with authorized donor registries.'),('03  Track questions and updates','Write down follow-up questions without collecting donor identities.'),('04  Review next steps','Discuss decisions and timelines directly with the clinical team.')]:
        with st.expander(title):st.write(detail)
    with st.form('match_questions',clear_on_submit=True):
        q=st.text_input('Question for your transplant coordinator')
        if st.form_submit_button('Save to My Care') and q.strip():st.session_state.questions.append(q.strip());st.success('Saved in My Care → Questions')
elif page=='Support':
    heading('🌿 Support resources','Organize practical questions and find the right people to ask.')
    for name,desc in [('Care team','Keep questions and appointment reminders together.'),('Travel and lodging','List travel needs and ask your center about available options.'),('Financial navigator','Prepare coverage and assistance questions.'),('Emotional support','Ask your transplant center about counseling and support groups.')]:
        with st.expander(name):st.write(desc)
    if st.button('Explore Finance & campaigns →',type='primary'):go('Finance')
st.divider()
st.caption('StemBridge • Clickable concept prototype • Fictional data • No clinical advice, real fundraising, payment processing, donor matching, or live integrations. Data entered is for the current demo session only.')

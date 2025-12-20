!streamlit run app.py &>/content/logs.txt &
from pyngrok import ngrok

ngrok.set_auth_token("377DEdvwxa6aYUKO3MF8B7Dti24_3WpHr26DMXPtBQqz3fiYU")
public_url = ngrok.connect(8501)
print(public_url)
import pandas as pd
!nohup streamlit run app.py &
from pyngrok import ngrok
# Purane connections band karne ke liye
ngrok.kill() 
# Naya tunnel start karein (Port 8501 Streamlit ka default hai)
public_url = ngrok.connect(8501)
print("Aapki Website Link Yeh Hai:", public_url)
!pkill streamlit
!pkill ngrok
%%writefile app.py
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Smart Library", layout="wide")
st.title("📚 Smart College Library Intelligence System")
st.success("Website successfully connect ho gayi hai!")

# Sample data dikhane ke liye
data = {"Book Name": ["Python Guide", "Data Science"], "Status": ["Available", "Issued"]}
df = pd.DataFrame(data)
st.table(df)
!nohup streamlit run app.py &
from pyngrok import ngrok
# Aapka Auth Token yahan hona chahiye agar manga jaye
public_url = ngrok.connect(8501)
print("Is NAYE link par click karein:", public_url)
!curl ipv4.icanhazip.com
%%writefile app.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Smart Library", layout="wide")

# Sidebar for Navigation
st.sidebar.title("📌 Menu")
page = st.sidebar.radio("Go to", ["Dashboard", "Book Search", "Fine Calculator"])

st.title("📚 Smart College Library Intelligence System")

# 1. Dashboard Page
if page == "Dashboard":
    st.subheader("📊 Library Analytics")
    
    # Sample Data (Isse aap apni CSV file se replace kar sakte hain)
    data = {
        'Category': ['Computer Science', 'Mathematics', 'Physics', 'Literature'],
        'Books Count': [150, 80, 65, 120],
        'Issued': [45, 20, 15, 30]
    }
    df = pd.DataFrame(data)
    
    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.bar(df, x='Category', y='Books Count', title="Books by Category", color='Category')
        st.plotly_chart(fig1)
    with col2:
        fig2 = px.pie(df, values='Issued', names='Category', title="Books Issued Distribution")
        st.plotly_chart(fig2)

# 2. Book Search Page
elif page == "Book Search":
    st.subheader("🔍 Search for Books")
    search_query = st.text_input("Enter Book Name or Author")
    if search_query:
        st.write(f"Searching for: {search_query}")
        # Yahan hum filtering logic daal sakte hain
        st.info("Searching functionality connected!")

# 3. Fine Calculator
elif page == "Fine Calculator":
    st.subheader("💰 Calculate Overdue Fine")
    days = st.number_input("Days Overdue", min_value=0, step=1)
    fine_rate = 5 # 5 Rupees per day
    total_fine = days * fine_rate
    if st.button("Calculate"):
        st.warning(f"Total Fine: ₹{total_fine}")
%%writefile app.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Smart Library", layout="wide")

# --- SMART DATABASE (In-built Data) ---
@st.cache_data
def load_data():
    data = {
        'Book_ID': [1001, 1002, 1003, 1004, 1005],
        'Title': ['Python Programming', 'Data Structures', 'Smart AI', 'Machine Learning', 'Discrete Maths'],
        'Author': ['Guido van Rossum', 'Narasimha Karumanchi', 'Sam Altman', 'Andrew Ng', 'Kenneth Rosen'],
        'Category': ['CS', 'CS', 'AI', 'AI', 'Maths'],
        'Status': ['Available', 'Issued', 'Available', 'Issued', 'Available'],
        'Issued_To': ['None', 'Rahul Sharma', 'None', 'Priya Patel', 'None']
    }
    return pd.DataFrame(data)

df = load_data()

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("📚 Library Menu")
menu = st.sidebar.radio("Navigate", ["📊 Dashboard", "🔍 Book Search", "⚖️ Fine Calculator"])

st.title("🏛️ Smart College Library Intelligence System")

# --- 1. DASHBOARD ---
if menu == "📊 Dashboard":
    st.subheader("Library Analytics")
    
    # Quick Stats
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Books", len(df))
    c2.metric("Issued Books", len(df[df['Status']=='Issued']))
    c3.metric("Available", len(df[df['Status']=='Available']))
    
    # Visuals
    col_a, col_b = st.columns(2)
    with col_a:
        fig1 = px.bar(df['Category'].value_counts(), title="Books by Department", labels={'value':'Count', 'index':'Dept'})
        st.plotly_chart(fig1)
    with col_b:
        fig2 = px.pie(df, names='Status', title="Book Availability Status", hole=0.4)
        st.plotly_chart(fig2)

# --- 2. BOOK SEARCH ---
elif menu == "🔍 Book Search":
    st.subheader("Smart Search Engine")
    search = st.text_input("Enter Book Name or Author Name")
    
    if search:
        results = df[df['Title'].str.contains(search, case=False) | df['Author'].str.contains(search, case=False)]
        st.table(results)
    else:
        st.dataframe(df, use_container_width=True)

# --- 3. FINE CALCULATOR ---
elif menu == "⚖️ Fine Calculator":
    st.subheader("Library Fine Management")
    days = st.number_input("How many days late?", min_value=0)
    if st.button("Calculate Fine"):
        fine = days * 10 # 10 Rupees per day
        st.error(f"Total Fine to be paid: ₹{fine}")
!pip install qrcode[pil]
import qrcode
from PIL import Image

# Apni website ki link yahan paste karein
my_link = "https://yahan-apni-link-daalein.localtunnel.me" 

# QR Code banana
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(my_link)
qr.make(fit=True)

# Image ko save aur display karna
img = qr.make_image(fill_color="black", back_color="white")
img.save("tgpcet_qr.png")

# Screen par dikhane ke liye
display(Image.open("tgpcet_qr.png"))
print("✅ TGPCET Smart Library QR Code taiyar hai!")
print("Ise apne phone ke camera se scan karein.")
%%writefile app.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Smart Library", layout="wide")

# Session State for Data (Taaki data refresh na ho jaye)
if 'library_data' not in st.session_state:
    st.session_state.library_data = pd.DataFrame({
        'Book_ID': [1001, 1002],
        'Title': ['Python Programming', 'Machine Learning'],
        'Author': ['Guido van Rossum', 'Andrew Ng'],
        'Category': ['CS', 'AI'],
        'Status': ['Available', 'Available']
    })

df = st.session_state.library_data

st.sidebar.title("🏛️ Library Control")
menu = st.sidebar.selectbox("Select Page", ["📊 Dashboard", "➕ Add/Issue Book", "🔍 Search"])

if menu == "📊 Dashboard":
    st.title("Smart Library Dashboard")
    # Graphs and Stats
    c1, c2 = st.columns(2)
    c1.metric("Total Books", len(df))
    c2.metric("Available", len(df[df['Status']=='Available']))
    
    fig = px.pie(df, names='Category', title="Department wise Books")
    st.plotly_chart(fig)

elif menu == "➕ Add/Issue Book":
    st.subheader("Librarian Portal")
    
    # Add New Book Form
    with st.expander("Add New Book to Inventory"):
        b_id = st.number_input("Book ID", min_value=1000)
        b_title = st.text_input("Book Title")
        b_author = st.text_input("Author")
        b_cat = st.selectbox("Category", ["CS", "AI", "Maths", "Physics"])
        if st.button("Add Book"):
            new_row = {'Book_ID':b_id, 'Title':b_title, 'Author':b_author, 'Category':b_cat, 'Status':'Available'}
            st.session_state.library_data = pd.concat([st.session_state.library_data, pd.DataFrame([new_row])], ignore_index=True)
            st.success("Book Added Successfully!")

    # Issue/Return Section
    st.divider()
    st.subheader("Issue / Return Book")
    selected_book = st.selectbox("Select Book", df['Title'].tolist())
    action = st.radio("Action", ["Issue", "Return"])
    if st.button("Update Status"):
        idx = df[df['Title'] == selected_book].index[0]
        st.session_state.library_data.at[idx, 'Status'] = 'Issued' if action == "Issue" else 'Available'
        st.success(f"Book {action}d successfully!")

elif menu == "🔍 Search":
    st.subheader("Quick Search")
    q = st.text_input("Search by Name or ID")
    if q:
        match = df[df['Title'].str.contains(q, case=False)]
        st.table(match)
    else:
        st.dataframe(df, use_container_width=True)
%%writefile app.py
import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(page_title="TGPCET Smart Library", page_icon="🎓", layout="wide")

# --- CUSTOM CSS FOR TGPCET BRANDING ---
st.markdown("""
    <style>
    .stApp {
        background-color: #f4f7f9;
    }
    .main-title {
        font-size: 45px;
        color: #1E3A8A;
        font-weight: bold;
        text-align: center;
        margin-bottom: 0px;
        text-shadow: 2px 2px 4px #d1d1d1;
    }
    .sub-title {
        font-size: 20px;
        color: #5C5C5C;
        text-align: center;
        margin-bottom: 30px;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border-left: 8px solid #1E3A8A;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown("<div class='main-title'>🏛️ TGPCET Smart Library</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Intelligence System for Modern Education</div>", unsafe_allow_html=True)

# --- DATA SETUP ---
if 'lib_data' not in st.session_state:
    st.session_state.lib_data = pd.DataFrame({
        'Book_ID': [101, 102, 103, 104],
        'Title': ['Python Basics', 'Advanced AI', 'Data Structures', 'Engineering Maths'],
        'Usage': [120, 95, 80, 60],
        'Status': ['Available', 'Issued', 'Available', 'Available']
    })

# --- SIDEBAR ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2232/2232688.png", width=80)
st.sidebar.header("TGPCET Portal")
menu = st.sidebar.selectbox("Select Menu", ["📊 Dashboard", "🔍 Book Search", "🤖 AI Predictions", "📑 Fine & Reports"])

# --- 1. DASHBOARD ---
if menu == "📊 Dashboard":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='card'><b>Total Books</b><br><h2>1,250</h2></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='card'><b>Students Registered</b><br><h2>850</h2></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='card'><b>Issued Today</b><br><h2>45</h2></div>", unsafe_allow_html=True)

    st.write("###")
    
    # Graphs
    c_left, c_right = st.columns(2)
    with c_left:
        fig = px.bar(st.session_state.lib_data, x='Title', y='Usage', color='Title', 
                     title="Most Used Books in TGPCET")
        st.plotly_chart(fig, use_container_width=True)
    
    with c_right:
        busy_data = pd.DataFrame({'Slot': ['Morning', 'Lunch', 'Evening'], 'Crowd': [40, 95, 30]})
        fig2 = px.line(busy_data, x='Slot', y='Crowd', title="Library Peak Hours", markers=True)
        st.plotly_chart(fig2, use_container_width=True)

# --- 2. SEARCH ---
elif menu == "🔍 Book Search":
    st.header("Find Your Resource")
    query = st.text_input("Search by Book Name...")
    if query:
        res = st.session_state.lib_data[st.session_state.lib_data['Title'].str.contains(query, case=False)]
        st.dataframe(res, use_container_width=True)

# --- 3. AI PREDICTIONS ---
elif menu == "🤖 AI Predictions":
    st.header("Library Intelligence")
    st.success("🚀 AI Prediction: Exams are coming! Demand for 'Engineering Maths' will increase by 40%.")
    st.info("💡 Insight: Most students visit library between 12:30 PM to 1:30 PM.")

# --- 4. FINE & REPORTS ---
elif menu == "📑 Fine & Reports":
    st.header("Late Return Records")
    late_data = pd.DataFrame({
        'Student ID': ['TGP001', 'TGP045'],
        'Name': ['Amit R.', 'Snehal P.'],
        'Days Late': [4, 2],
        'Fine (₹)': [40, 20]
    })
    st.table(late_data)
%%writefile app.py
import streamlit as st
import pandas as pd
import plotly.express as px
import random

st.set_page_config(page_title="Smart Library AI", layout="wide")

st.title("🏛️ Smart Library Intelligence System")

# --- SYMBOLIC SMART DATA ---
# Yeh data aapke sawalon ke jawab dene ke liye banaya gaya hai
usage_data = pd.DataFrame({
    'Book_Title': ['Python Programming', 'Machine Learning', 'Data Science', 'Discrete Maths', 'Physics-I'],
    'Usage_Count': [85, 70, 65, 40, 30],
    'Future_Demand_Score': [95, 88, 92, 45, 38]
})

busy_hours = pd.DataFrame({
    'Time_Slot': ['8AM-10AM', '10AM-12PM', '12PM-2PM', '2PM-4PM', '4PM-6PM'],
    'Student_Count': [20, 55, 90, 40, 25]
})

late_returners = pd.DataFrame({
    'Student_Name': ['Rahul S.', 'Anjali K.', 'Vikas M.', 'Sneha P.'],
    'Times_Late': [5, 3, 2, 2],
    'Total_Fine': [500, 300, 200, 200]
})

# --- SIDEBAR ---
menu = st.sidebar.selectbox("Smart Insights", ["📈 Usage Trends", "⏰ Busy Hours", "👤 Late Returners", "🔮 Future Demand"])

# 1. Kaunsi books sabse zyada use hoti hain?
if menu == "📈 Usage Trends":
    st.header("Top Used Books")
    fig = px.bar(usage_data, x='Book_Title', y='Usage_Count', color='Usage_Count', title="Most Borrowed Books")
    st.plotly_chart(fig)
    st.info("💡 Python Programming library mein sabse zyada popular hai.")

# 2. Kaunse time library sabse busy hoti hai?
elif menu == "⏰ Busy Hours":
    st.header("Peak Library Hours")
    fig2 = px.line(busy_hours, x='Time_Slot', y='Student_Count', markers=True, title="Crowd Analysis")
    st.plotly_chart(fig2)
    st.warning("⚠️ 12PM se 2PM ke beech library sabse zyada busy rehti hai.")

# 3. Kaunse students late books return karte hain?
elif menu == "👤 Late Returners":
    st.header("Student Behavior (Late Returns)")
    st.table(late_returners)
    st.error("Rahul S. ne sabse zyada baar books late return ki hain.")

# 4. Future me kaunsi books ki demand hogi? (AI Prediction)
elif menu == "🔮 Future Demand":
    st.header("AI Demand Prediction")
    st.write("Hamara AI model suggest karta hai ki agle mahine in subjects ki demand badhegi:")
    fig3 = px.scatter(usage_data, x='Book_Title', y='Future_Demand_Score', size='Future_Demand_Score', color='Book_Title')
    st.plotly_chart(fig3)
    st.success("🚀 Prediction: 'Smart AI' aur 'Machine Learning' ki demand 20% badhne wali hai.")
%%writefile app.py
import streamlit as st
import pandas as pd
import plotly.express as px

# Page config ko aur sundar banayein
st.set_page_config(page_title="Smart Library AI", page_icon="📚", layout="wide")

# --- CUSTOM CSS (Website ko attractive banane ke liye) ---
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    h1 {
        color: #1E3A8A;
        text-align: center;
        font-family: 'Segoe UI', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# Title with Emoji
st.markdown("<h1>🏛️ Smart College Library Intelligence System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>AI-Powered Management & Analytics</p>", unsafe_allow_html=True)

# --- SMART DATA ---
usage_data = pd.DataFrame({
    'Book_Title': ['Python', 'AI/ML', 'Data Science', 'Physics', 'Maths'],
    'Usage': [85, 70, 65, 40, 30]
})

# --- SIDEBAR (Custom Styling) ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3429/3429149.png", width=100)
st.sidebar.title("Navigation")
menu = st.sidebar.selectbox("Go to:", ["📊 Dashboard", "🔍 Smart Search", "💡 Future Insights", "⚙️ Admin Access"])

# --- 1. DASHBOARD (Visual Appeal) ---
if menu == "📊 Dashboard":
    # 3-Column Metrics
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric(label="Total Books", value="1,240", delta="12 New")
    with m2:
        st.metric(label="Active Users", value="450", delta="5% Increase")
    with m3:
        st.metric(label="Fine Collected", value="₹4,200", delta="-200", delta_color="normal")

    st.divider()
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("📈 Popularity Trend")
        fig = px.area(usage_data, x='Book_Title', y='Usage', title="Usage Analysis", 
                      color_discrete_sequence=['#1E3A8A'])
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🕒 Library Traffic")
        busy_data = pd.DataFrame({'Hour': ['Morning', 'Afternoon', 'Evening'], 'Crowd': [30, 90, 45]})
        fig2 = px.bar(busy_data, x='Hour', y='Crowd', color='Hour')
        st.plotly_chart(fig2, use_container_width=True)

# --- 2. SEARCH (Clean UI) ---
elif menu == "🔍 Smart Search":
    st.subheader("Quick Book Finder")
    search = st.text_input("Enter keywords (e.g. 'Machine Learning')...")
    if search:
        st.balloons() # Thoda animation ke liye
        st.success(f"Found 3 books related to '{search}'")
        # Dummy table
        st.table(usage_data)

# --- 3. FUTURE INSIGHTS (AI/Analytics) ---
elif menu == "💡 Future Insights":
    st.subheader("AI Prediction: Next Month Demand")
    st.info("Based on exam schedules, 'Data Science' books will be in high demand.")
    
    # Advanced Graph
    fig3 = px.pie(usage_data, values='Usage', names='Book_Title', hole=.6, title="Predicted Resource Allocation")
    st.plotly_chart(fig3)

# --- 4. ADMIN ACCESS ---
elif menu == "⚙️ Admin Access":
    st.subheader("Librarian Login")
    user = st.text_input("Username")
    pw = st.text_input("Password", type="password")
    if st.button("Login"):
        st.error("Invalid Credentials! Try again.")



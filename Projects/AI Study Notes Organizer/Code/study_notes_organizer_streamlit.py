import streamlit as st
import google.generativeai as genai
import json
import os
from datetime import datetime
from typing import List, Dict
import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure page
st.set_page_config(
    page_title="AI Study Notes Organizer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Configure Gemini API
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    st.error(
        "❌ GOOGLE_API_KEY not found in environment variables. Please set it in your .env file."
    )
    st.stop()

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

# File path for storing data
JSON_FILE_PATH = "notes_data.json"

# Initialize session state
if "processed_notes" not in st.session_state:
    st.session_state.processed_notes = []


def load_from_json() -> List[Dict]:
    """Load saved notes data from JSON file"""
    try:
        if os.path.exists(JSON_FILE_PATH):
            with open(JSON_FILE_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        return []
    except Exception as e:
        st.error(f"Error loading JSON file: {e}")
        return []


def save_to_json(note_data: Dict):
    """Save note data to JSON file"""
    try:
        existing_data = load_from_json()
        existing_data.append(note_data)

        with open(JSON_FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(existing_data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        st.error(f"Error saving to JSON: {e}")


def parse_uploaded_file(uploaded_file) -> str:
    """Parse uploaded text file and return content"""
    try:
        if uploaded_file is not None:
            return uploaded_file.getvalue().decode("utf-8")
        return ""
    except Exception as e:
        st.error(f"Error reading file: {e}")
        return ""


def generate_title(text: str, max_words: int = 8) -> str:
    """Generate a title from the first few words of the text"""
    words = text.strip().split()
    title_words = words[:max_words]
    title = " ".join(title_words)
    if len(words) > max_words:
        title += "..."
    return title


def summarize_notes(text: str) -> str:
    """Use Gemini Pro to summarize notes"""
    try:
        with st.spinner("🤖 Generating summary..."):
            prompt = f"""
            Please provide a concise 3-5 sentence summary of the following study notes. 
            Focus on the main concepts and key points:
            
            {text}
            
            Summary:
            """

            response = model.generate_content(prompt)
            return response.text.strip()
    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg or "quota" in error_msg.lower():
            return "⚠️ API quota exceeded. Please wait a moment and try again, or check your API key usage at https://makersuite.google.com/app/apikey"
        elif "401" in error_msg or "unauthorized" in error_msg.lower():
            return (
                "❌ Invalid API key. Please check your GOOGLE_API_KEY in the .env file"
            )
        else:
            return f"Error generating summary: {error_msg}"


def extract_keywords(text: str) -> List[str]:
    """Use Gemini Pro to extract keywords from notes"""
    try:
        with st.spinner("🔍 Extracting keywords..."):
            prompt = f"""
            Please extract 5-10 relevant keywords or topic tags from the following study notes. 
            Return only the keywords separated by commas, no explanations:
            
            {text}
            
            Keywords:
            """

            response = model.generate_content(prompt)
            keywords_text = response.text.strip()

            # Clean and split keywords
            keywords = [kw.strip() for kw in keywords_text.split(",")]
            keywords = [kw for kw in keywords if kw and len(kw) > 0]

            return keywords[:10]  # Limit to 10 keywords
    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg or "quota" in error_msg.lower():
            return [
                "⚠️ API quota exceeded. Please wait a moment and try again, or check your API key usage at https://makersuite.google.com/app/apikey"
            ]
        elif "401" in error_msg or "unauthorized" in error_msg.lower():
            return [
                "❌ Invalid API key. Please check your GOOGLE_API_KEY in the .env file"
            ]
        else:
            return [f"Error extracting keywords: {error_msg}"]


def process_notes(text_input: str, uploaded_file, task: str) -> tuple:
    """Main processing function"""
    # Get text from either input or file
    if uploaded_file is not None:
        text = parse_uploaded_file(uploaded_file)
    else:
        text = text_input.strip()

    if not text:
        return "Please provide text or upload a file.", "", "", ""

    # Generate title
    title = generate_title(text)

    # Process based on selected task
    if task == "Summarize Notes":
        result = summarize_notes(text)
        result_type = "Summary"
    elif task == "Extract Keywords":
        keywords = extract_keywords(text)
        result = ", ".join(keywords)
        result_type = "Keywords"
    else:
        return "Please select a valid task.", "", "", ""

    # Save to JSON
    note_data = {
        "title": title,
        "original_notes": text,
        "result": result,
        "task": task,
        "result_type": result_type,
        "timestamp": datetime.now().isoformat(),
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    save_to_json(note_data)

    return result, title, note_data["date"], text


def display_history():
    """Display history in a nice format"""
    data = load_from_json()
    if not data:
        st.info("📚 No saved notes yet. Process some notes to see them here!")
        return

    # Sort by timestamp (newest first)
    data.sort(key=lambda x: x.get("timestamp", ""), reverse=True)

    # Create a DataFrame for better display
    df_data = []
    for entry in data:
        df_data.append(
            {
                "Date": entry.get("date", "Unknown"),
                "Title": entry.get("title", "Untitled"),
                "Task": entry.get("task", ""),
                "Result": (
                    entry.get("result", "")[:100] + "..."
                    if len(entry.get("result", "")) > 100
                    else entry.get("result", "")
                ),
                "Full Result": entry.get("result", ""),
                "Original Notes": entry.get("original_notes", ""),
            }
        )

    df = pd.DataFrame(df_data)

    # Display with expandable sections
    for idx, row in df.iterrows():
        with st.expander(f"📝 {row['Title']} - {row['Date']}", expanded=False):
            col1, col2 = st.columns([1, 1])

            with col1:
                st.markdown(f"**Task:** {row['Task']}")
                st.markdown(f"**Date:** {row['Date']}")
                st.markdown("**Result:**")
                st.text_area(
                    "Result",
                    value=row["Full Result"],
                    height=150,
                    disabled=True,
                    key=f"result_{idx}",
                    label_visibility="collapsed",
                )

            with col2:
                st.markdown("**Original Notes:**")
                st.text_area(
                    "Original Notes",
                    value=row["Original Notes"],
                    height=150,
                    disabled=True,
                    key=f"notes_{idx}",
                    label_visibility="collapsed",
                )


def clear_history():
    """Clear the history JSON file"""
    try:
        if os.path.exists(JSON_FILE_PATH):
            os.remove(JSON_FILE_PATH)
        st.success("🗑️ History cleared successfully!")
        st.rerun()
    except Exception as e:
        st.error(f"Error clearing history: {str(e)}")


# Main app
def main():
    st.title("🧠 AI-Powered Study Notes Organizer")
    st.markdown(
        "Upload your study notes or paste text, then choose to summarize or extract keywords using AI."
    )

    # Sidebar for history
    with st.sidebar:
        st.header("📚 Study History")

        if st.button("🔄 Refresh History", use_container_width=True):
            st.rerun()

        if st.button("🗑️ Clear History", use_container_width=True, type="secondary"):
            clear_history()

        st.markdown("---")
        display_history()

    # Main content area
    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("📝 Input Your Notes")

        # Input method selection
        input_method = st.radio(
            "Choose input method:", ["📝 Paste Text", "📁 Upload File"], horizontal=True
        )

        if input_method == "📝 Paste Text":
            text_input = st.text_area(
                "Enter your study notes:",
                placeholder="Paste your study notes here...",
                height=200,
                help="Type or paste your study notes in this text area",
            )
            uploaded_file = None
        else:
            uploaded_file = st.file_uploader(
                "Upload a .txt file:",
                type=["txt"],
                help="Upload a text file containing your study notes",
            )
            text_input = ""

        # Task selection
        task = st.selectbox(
            "Select processing task:",
            ["Summarize Notes", "Extract Keywords"],
            help="Choose what you want to do with your notes",
        )

        # Process button
        if st.button("🚀 Process Notes", type="primary", use_container_width=True):
            if not text_input and not uploaded_file:
                st.error("❌ Please provide text or upload a file.")
            else:
                result, title, date, original_text = process_notes(
                    text_input, uploaded_file, task
                )

                # Store in session state for display
                st.session_state.processed_notes.append(
                    {
                        "result": result,
                        "title": title,
                        "date": date,
                        "original_text": original_text,
                        "task": task,
                    }
                )

                st.success("✅ Processing complete!")

    with col2:
        st.header("📊 Results")

        # Display latest result
        if st.session_state.processed_notes:
            latest = st.session_state.processed_notes[-1]

            st.markdown(f"**Title:** {latest['title']}")
            st.markdown(f"**Date:** {latest['date']}")
            st.markdown(f"**Task:** {latest['task']}")

            st.markdown("**Result:**")
            st.text_area(
                "Result",
                value=latest["result"],
                height=200,
                disabled=True,
                label_visibility="collapsed",
            )

            # Show original text in expander
            with st.expander("📄 View Original Notes"):
                st.text_area(
                    "Original Notes",
                    value=latest["original_text"],
                    height=150,
                    disabled=True,
                    label_visibility="collapsed",
                )

        # Statistics
        st.markdown("---")
        st.subheader("📈 Statistics")
        data = load_from_json()
        if data:
            st.metric("Total Notes Processed", len(data))

            # Task breakdown
            task_counts = {}
            for entry in data:
                task = entry.get("task", "Unknown")
                task_counts[task] = task_counts.get(task, 0) + 1

            for task, count in task_counts.items():
                st.metric(f"{task}", count)
        else:
            st.info("No notes processed yet.")

    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #666;'>
        <p>Powered by Google Gemini Pro AI • Built with Streamlit</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()

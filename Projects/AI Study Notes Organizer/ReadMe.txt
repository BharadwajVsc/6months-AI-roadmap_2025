# 🧠 AI-Powered Study Notes Organizer

A complete Gradio-based web application that uses Google's Gemini Pro AI to help organize and process your study notes. The app can summarize notes and extract keywords, with automatic saving to a local JSON file.

## ✨ Features

- **📝 Text Input & File Upload**: Paste notes directly or upload `.txt` files
- **🤖 AI Processing**: Uses Gemini Pro for intelligent note processing
- **📊 Two Processing Options**:
  - **Summarize Notes**: Generate 3-5 sentence summaries
  - **Extract Keywords**: Extract 5-10 relevant keywords/tags
- **💾 Automatic Saving**: All processed notes are saved to `notes_data.json`
- **📚 History Management**: View, refresh, and clear your study history
- **📱 Mobile-Friendly**: Clean, responsive Gradio interface
- **🎨 Modern UI**: Soft theme with intuitive design

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up Your API Key

Create a `.env` file in the project directory:

```bash
# .env
GOOGLE_API_KEY=your_gemini_api_key_here
```

**To get your Gemini API key:**

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the key and paste it in your `.env` file

### 3. Run the Application

```bash
python study_notes_organizer.py
```

The app will be available at: **http://localhost:7860**

## 📖 How to Use

### Input Your Notes

1. **Text Input**: Paste your study notes directly into the text box
2. **File Upload**: Upload a `.txt` file containing your notes

### Process Your Notes

1. **Select Task**: Choose between "Summarize Notes" or "Extract Keywords"
2. **Click Process**: Hit the "🚀 Process Notes" button
3. **View Results**: See the AI-generated summary or keywords

### Manage History

- **View History**: All processed notes appear in the sidebar
- **Refresh**: Click "🔄 Refresh History" to update the display
- **Clear**: Click "🗑️ Clear History" to delete all saved data

## 🏗️ Architecture

### Core Functions

- `summarize_notes(text: str) -> str`: Uses Gemini Pro to generate summaries
- `extract_keywords(text: str) -> List[str]`: Extracts relevant keywords
- `save_to_json(note_data: dict)`: Saves processed notes to JSON
- `load_from_json() -> List[dict]`: Loads saved notes from JSON
- `parse_uploaded_file(file) -> str`: Processes uploaded text files

### Data Structure

Each saved note contains:

```json
{
  "title": "Auto-generated title",
  "original_notes": "Original text content",
  "result": "AI-generated summary or keywords",
  "task": "Summarize Notes or Extract Keywords",
  "result_type": "Summary or Keywords",
  "timestamp": "ISO timestamp",
  "date": "Human-readable date"
}
```

## 🔧 Technical Details

- **Framework**: Gradio 4.0+
- **AI Model**: Google Gemini Pro
- **Data Storage**: Local JSON file (`notes_data.json`)
- **Environment**: Python 3.8+
- **Dependencies**: See `requirements.txt`

## 🛠️ Customization

### Modify Processing Options

Edit the prompts in `summarize_notes()` and `extract_keywords()` functions to customize AI behavior.

### Change UI Theme

Modify the theme in the Gradio interface:

```python
with gr.Blocks(title="AI-Powered Study Notes Organizer", theme=gr.themes.Soft()) as demo:
```

### Adjust File Paths

Change `JSON_FILE_PATH` to store data in a different location.

## 🐛 Troubleshooting

### API Key Issues

- Ensure your `.env` file exists and contains the correct API key
- Verify the API key is valid and has sufficient quota
- Check that `python-dotenv` is installed

### File Upload Issues

- Ensure uploaded files are `.txt` format
- Check file encoding (UTF-8 recommended)
- Verify file permissions

### Memory Issues

- Large text files may cause processing delays
- Consider breaking very long notes into smaller chunks

## 📝 Example Usage

### Sample Input

```
Machine Learning Fundamentals

Machine learning is a subset of artificial intelligence that enables computers to learn and improve from experience without being explicitly programmed. It involves algorithms that can identify patterns in data and make predictions or decisions based on that data.

Key concepts include supervised learning, unsupervised learning, and reinforcement learning. Supervised learning uses labeled training data, unsupervised learning finds hidden patterns in unlabeled data, and reinforcement learning learns through interaction with an environment.
```

### Sample Output (Summarize)

```
Machine learning is a subset of AI that enables computers to learn from experience without explicit programming. It uses algorithms to identify data patterns and make predictions. The field includes supervised learning with labeled data, unsupervised learning for hidden patterns, and reinforcement learning through environment interaction.
```

### Sample Output (Keywords)

```
Machine Learning, Artificial Intelligence, Algorithms, Data Patterns, Predictions, Supervised Learning, Unsupervised Learning, Reinforcement Learning, Training Data, Environment Interaction
```

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

This project is open source and available under the MIT License.

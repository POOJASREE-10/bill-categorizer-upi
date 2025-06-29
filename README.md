# Emotion Support Chatbot with Whisper

A Flask-based web application that provides emotional support through a conversational chatbot interface. The application features both text and voice input capabilities using OpenAI's Whisper for local speech-to-text transcription, with intelligent emotion detection and supportive responses.

## Features

- 🤗 **Emotional Support**: Provides empathetic responses based on detected emotions
- 🎤 **Voice Input**: Local speech-to-text using OpenAI Whisper (no internet required)
- 🔊 **Text-to-Speech**: Bot responses are spoken aloud for accessibility
- 📱 **Responsive Design**: Works on desktop and mobile devices
- 🎨 **Modern UI**: Beautiful gradient design with smooth animations
- 🧠 **Emotion Detection**: Recognizes various emotional states (sad, angry, anxious, happy, stressed, lonely)
- 🔒 **Privacy-First**: All voice processing happens locally on your machine

## Supported Emotions

The chatbot can detect and respond to:
- **Sadness**: sad, depressed, down, blue, unhappy, miserable, hopeless
- **Anger**: angry, mad, furious, irritated, frustrated, annoyed, rage
- **Anxiety**: anxious, worried, nervous, scared, afraid, fear, panic
- **Happiness**: happy, joy, excited, thrilled, delighted, great, wonderful
- **Stress**: stressed, overwhelmed, tired, exhausted, burned out
- **Loneliness**: lonely, alone, isolated, abandoned, left out

## Prerequisites

### 1. Install FFmpeg
Whisper requires FFmpeg for audio processing. Install it based on your operating system:

**Windows:**
```bash
# Using Chocolatey
choco install ffmpeg

# Using Scoop
scoop install ffmpeg

# Or download from https://ffmpeg.org/download.html
```

**macOS:**
```bash
# Using Homebrew
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install ffmpeg
```

**Linux (CentOS/RHEL):**
```bash
sudo yum install ffmpeg
```

### 2. Verify FFmpeg Installation
```bash
ffmpeg -version
```

## Installation

1. **Clone or download** this project to your local machine

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

## Usage

### Text Input
- Type your message in the input field
- Press Enter or click the "Send" button
- The chatbot will analyze your message and provide an appropriate response

### Voice Input
- Click the microphone button to start recording
- Speak your message clearly
- Click the microphone button again to stop recording
- The audio will be processed locally using Whisper
- Your transcribed message will appear in the input field and be sent automatically

### Features
- **Typing Indicator**: Shows when the bot is processing your message
- **Auto-scroll**: Chat automatically scrolls to show new messages
- **Speech Synthesis**: Bot responses are spoken aloud
- **Error Handling**: Graceful handling of recording and transcription errors
- **Status Indicators**: Visual feedback for recording and processing states

## Browser Compatibility

### Audio Recording
- ✅ Chrome (recommended)
- ✅ Edge
- ✅ Firefox
- ✅ Safari

### Speech Synthesis
- ✅ Chrome
- ✅ Edge
- ✅ Firefox
- ✅ Safari

## Technical Details

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Speech Recognition**: OpenAI Whisper (local)
- **Speech Synthesis**: Web Speech API
- **Audio Recording**: MediaRecorder API
- **Styling**: Custom CSS with gradients and animations

## Project Structure

```
voiceinput/
├── app.py              # Main Flask application with Whisper integration
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── templates/
    └── index.html     # Main HTML template with audio recording
```

## Customization

### Adding New Emotions
To add support for new emotions, edit the `emotion_keywords` dictionary in `app.py`:

```python
emotion_keywords = {
    'your_emotion': ['keyword1', 'keyword2', 'keyword3'],
    # ... existing emotions
}
```

### Adding New Responses
To add new response templates, edit the `emotion_responses` dictionary in `app.py`:

```python
emotion_responses = {
    'your_emotion': [
        "Response 1",
        "Response 2",
        "Response 3"
    ],
    # ... existing responses
}
```

### Whisper Model Size
You can change the Whisper model size in `app.py` for different accuracy/speed trade-offs:

```python
# Options: "tiny", "base", "small", "medium", "large"
model = whisper.load_model("base")  # Default: good balance
```

- **tiny**: Fastest, least accurate
- **base**: Good balance (default)
- **small**: Better accuracy, slower
- **medium**: High accuracy, slower
- **large**: Best accuracy, slowest

## Troubleshooting

### FFmpeg Not Found
If you get an error about FFmpeg not being found:
1. Make sure FFmpeg is installed
2. Ensure it's in your system PATH
3. Restart your terminal/command prompt

### Audio Recording Issues
- Check microphone permissions in your browser
- Ensure your microphone is working and not muted
- Try refreshing the page if permissions were denied

### Whisper Model Loading
- The first run will download the Whisper model (~150MB for base model)
- Ensure you have a stable internet connection for the initial download
- Subsequent runs will use the cached model

## Performance Tips

- Use the "base" model for good balance of speed and accuracy
- Close other applications using the microphone
- Speak clearly and at a normal pace
- Ensure good microphone quality for better transcription

## Safety Notice

This chatbot is designed for emotional support and conversation practice. It is not a substitute for professional mental health care. If you're experiencing severe emotional distress, please contact a mental health professional or crisis hotline.

## License

This project is open source and available under the MIT License. 
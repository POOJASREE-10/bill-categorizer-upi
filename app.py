# Flask: Emotion Support Chatbot
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import random
import re

app = Flask(__name__)
CORS(app)

# Emotion support responses
emotion_responses = {
    'sad': [
        "I'm sorry you're feeling sad. It's okay to feel this way sometimes. Would you like to talk about what's bothering you?",
        "I hear that you're feeling down. Remember that difficult emotions are temporary and you're not alone in feeling this way.",
        "It sounds like you're going through a tough time. Sometimes just acknowledging our feelings can help us feel a bit better."
    ],
    'angry': [
        "I can sense that you're feeling angry. It's natural to feel this way when things don't go as expected. What triggered this feeling?",
        "Anger is a valid emotion, but it can be overwhelming. Taking deep breaths can sometimes help us think more clearly.",
        "I understand you're frustrated. Sometimes talking about what's making us angry can help us process these feelings."
    ],
    'anxious': [
        "Anxiety can be really challenging to deal with. Remember to breathe deeply and know that this feeling will pass.",
        "It sounds like you're feeling anxious. Sometimes focusing on the present moment can help ground us.",
        "I hear your anxiety. It's okay to feel this way. What would help you feel more comfortable right now?"
    ],
    'happy': [
        "I'm so glad you're feeling happy! It's wonderful to hear about positive moments in your life.",
        "That's fantastic! Happiness is such a beautiful emotion to experience and share.",
        "Your happiness is contagious! It's great that you're feeling good today."
    ],
    'stressed': [
        "Stress can be really overwhelming. Remember to take things one step at a time.",
        "I understand you're feeling stressed. Sometimes breaking tasks into smaller pieces can help.",
        "Stress is a natural response, but it's important to find ways to manage it. What usually helps you relax?"
    ],
    'lonely': [
        "Feeling lonely can be really difficult. Remember that you're not truly alone, even when it feels that way.",
        "I hear that you're feeling lonely. Sometimes reaching out to others, even in small ways, can help.",
        "Loneliness is a common human experience. It's okay to feel this way, and it won't last forever."
    ]
}

# General supportive responses
general_responses = [
    "I'm here to listen and support you. How are you feeling today?",
    "Thank you for sharing that with me. I want you to know that your feelings are valid.",
    "I appreciate you opening up to me. Is there anything specific you'd like to talk about?",
    "I'm here for you. Sometimes just talking about our feelings can help us feel better.",
    "You're doing great by reaching out. How can I best support you right now?"
]

def detect_emotion(message):
    """Simple emotion detection based on keywords"""
    message_lower = message.lower()
    
    emotion_keywords = {
        'sad': ['sad', 'depressed', 'down', 'blue', 'unhappy', 'miserable', 'hopeless'],
        'angry': ['angry', 'mad', 'furious', 'irritated', 'frustrated', 'annoyed', 'rage'],
        'anxious': ['anxious', 'worried', 'nervous', 'scared', 'afraid', 'fear', 'panic'],
        'happy': ['happy', 'joy', 'excited', 'thrilled', 'delighted', 'great', 'wonderful'],
        'stressed': ['stressed', 'overwhelmed', 'tired', 'exhausted', 'burned out'],
        'lonely': ['lonely', 'alone', 'isolated', 'abandoned', 'left out']
    }
    
    for emotion, keywords in emotion_keywords.items():
        if any(keyword in message_lower for keyword in keywords):
            return emotion
    
    return None

def generate_response(message):
    """Generate an appropriate response based on the user's message"""
    emotion = detect_emotion(message)
    
    if emotion and emotion in emotion_responses:
        return random.choice(emotion_responses[emotion])
    else:
        return random.choice(general_responses)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    
    if not user_message.strip():
        return jsonify({'reply': 'Please say something so I can help you.'})
    
    print(f"💬 User message: '{user_message}'")
    bot_response = generate_response(user_message)
    print(f"🤖 Bot response: '{bot_response}'")
    
    return jsonify({'reply': bot_response})

if __name__ == "__main__":
    print("🚀 Starting Emotion Support Chatbot...")
    app.run(debug=True, host='0.0.0.0', port=5000) 
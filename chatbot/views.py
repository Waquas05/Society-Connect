from django.shortcuts import render
from django.http import JsonResponse
from app1.models import Society, Event
import google.generativeai as genai
from django.conf import settings

# Create your views here.

genai.configure(api_key=settings.GEMINI_API_KEY)

# def chatbot_response(request):
#     user_input=request.GET.get("message", "")
#     societies=Society.objects.all()
#     events=Event.objects.all()

#     prompt = f"""
#     You are an AI student guide for Society Connect website. Have a nice conversation with the student. 
#     The student said: "{user_input}".
#     Here are available societies and events:
#     {', '.join([s.name for s in societies])}, {', '.join([e.name for e in events])}.
#     Suggest a suitable society or event as asked by the student and explain why in 2 lines. """

#     try:
#         model = genai.GenerativeModel("gemini-1.5-flash")
#         response = model.generate_content(prompt)
#         bot_reply = response.text
#     except Exception as e:
#         bot_reply = "Sorry, I couldn’t process your request right now."

#     return JsonResponse({"response": bot_reply})

def chatbot_interface(request):
    return render(request, 'chatbot/chatbot_page.html')


def chatbot_response(request):
    user_input = request.GET.get("message", "")
    societies = Society.objects.all()
    events = Event.objects.all()

    # Initialize conversation history in session
    if "chat_history" not in request.session:
        request.session["chat_history"] = []

    chat_history = request.session["chat_history"]

    # Combine previous chat history
    history_text = "\n".join(
        [f"User: {h['user']}\nBot: {h['bot']}" for h in chat_history]
    )

    # Create contextual prompt
    prompt = f"""
    You are an AI student guide for the Society Connect website.
    Here’s the previous conversation:
    {history_text}

    The student said: "{user_input}"
    Available societies: {', '.join([s.name for s in societies])}
    Available events: {', '.join([e.title for e in events])}

    Respond naturally and in short to help the student choose societies/events that match their interests.Talk naturally even if the topic is beyond societies.
    """

    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)
        bot_reply = response.text
    except Exception as e:
        print("Chatbot Error:", str(e))
        bot_reply = "Sorry, I couldn’t process your request right now."

    # Save the new conversation turn to session
    chat_history.append({"user": user_input, "bot": bot_reply})
    request.session["chat_history"] = chat_history

    return JsonResponse({"response": bot_reply})
import streamlit as st
import datetime
from assistant import Assistant
from weather_service import get_weather
from search_service import search_web
import os

st.set_page_config(
    page_title="AI Assistant Builder",
    page_icon="🤖",
    layout="wide"
)

if "assistant" not in st.session_state:
    st.session_state.assistant = Assistant("Assistant", "I'm a helpful AI assistant.")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "setup_complete" not in st.session_state:
    st.session_state.setup_complete = False
if "api_keys" not in st.session_state:
    st.session_state.api_keys = {
        "OPENAI_API_KEY": os.environ.get("OPENAI_API_KEY", ""),
        "WEATHER_API_KEY": os.environ.get("WEATHER_API_KEY", ""),
        "SERPAPI_KEY": os.environ.get("SERPAPI_KEY", "")
    }
if "show_api_settings" not in st.session_state:
    st.session_state.show_api_settings = False


def handle_user_message(user_input):
    """Process user input and generate assistant response"""
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    input_lower = user_input.lower()
    
    with st.spinner("Thinking..."):
        if "time" in input_lower and ("what" in input_lower or "tell" in input_lower or "current" in input_lower):
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
            response = f"The current time is {current_time} on {current_date}."
        
        elif ("weather" in input_lower or "temperature" in input_lower) and ("what" in input_lower or "how" in input_lower):
            location = extract_location(input_lower)
            if location:
                weather_data = get_weather(location)
                if "error" in weather_data:
                    response = f"I couldn't get the weather information for {location}. {weather_data['error']}"
                else:
                    response = f"In {weather_data['location']}, it's currently {weather_data['temperature']}°C with {weather_data['description']}. The humidity is {weather_data['humidity']}%."
            else:
                response = "I need a location to check the weather. Please ask about the weather in a specific city."
        
        elif "search" in input_lower or "find" in input_lower or "look up" in input_lower:
            query = extract_search_query(user_input)
            if query:
                search_results = search_web(query)
                if search_results:
                    response = f"Here's what I found about '{query}':\n\n"
                    for idx, result in enumerate(search_results[:3], 1):
                        response += f"{idx}. {result['title']}\n{result['snippet']}\n{result['link']}\n\n"
                else:
                    response = f"I couldn't find any results for '{query}'."
            else:
                response = "I need a search query. Could you please specify what you'd like me to search for?"
        
        else:
            response = st.session_state.assistant.respond_to_query(user_input)
    
    st.session_state.chat_history.append({"role": "assistant", "content": response})


def extract_location(text):
    """Extract location from a weather query."""
    common_weather_phrases = [
        "weather in ", "weather for ", "temperature in ", 
        "temperature at ", "weather at ", "how's the weather in ",
        "what's the weather in ", "what is the weather in "
    ]
    
    for phrase in common_weather_phrases:
        if phrase in text.lower():
            location = text.lower().split(phrase)[1].strip()
            location = location.replace("?", "").replace(".", "").strip()
            return location
    
    words = text.lower().split()
    if "in" in words:
        idx = words.index("in")
        if idx + 1 < len(words):
            return words[idx + 1].replace("?", "").replace(".", "").strip()
    
    return None


def extract_search_query(text):
    """Extract search query from user input."""
    search_indicators = [
        "search for ", "search about ", "find information on ", 
        "look up ", "find out about ", "search ", "find "
    ]
    
    for indicator in search_indicators:
        if indicator in text.lower():
            query = text.lower().split(indicator)[1].strip()
            query = query.replace("?", "").replace(".", "").strip()
            return query
    
    return None


def customize_assistant():
    """Update assistant name and personality based on user input"""
    name = st.session_state.assistant_name
    personality = st.session_state.assistant_personality
    
    if name and personality:
        st.session_state.assistant = Assistant(name, personality)
        st.session_state.setup_complete = True
        st.session_state.chat_history = []
        st.session_state.chat_history.append({
            "role": "assistant", 
            "content": f"Hello! I'm {name}. My job: {personality} \n How can I help you today?"
        })
        st.success(f"Your assistant '{name}' has been configured!")
    else:
        st.error("Please provide both a name and personality for your assistant.")


def update_api_keys():
    """Update API keys in the environment variables from session state"""
    os.environ["OPENAI_API_KEY"] = st.session_state.api_keys["OPENAI_API_KEY"]
    os.environ["WEATHER_API_KEY"] = st.session_state.api_keys["WEATHER_API_KEY"]
    os.environ["SERPAPI_KEY"] = st.session_state.api_keys["SERPAPI_KEY"]
    
    if st.session_state.setup_complete:
        current_name = st.session_state.assistant.name
        current_personality = st.session_state.assistant.personality
        st.session_state.assistant = Assistant(current_name, current_personality)
    
    if not os.environ["OPENAI_API_KEY"]:
        st.warning("OpenAI API key is not set. The assistant will have limited functionality.")
    else:
        st.success("API keys updated successfully!")


def toggle_api_settings():
    """Toggle the API settings visibility"""
    st.session_state.show_api_settings = not st.session_state.show_api_settings


st.title("🤖 AI Personal Assistant Builder")

if not st.session_state.setup_complete:
    st.markdown("### Create Your Own AI Assistant")
    st.markdown("""
    Customize your personal AI assistant by giving it a name and defining its personality.
    Once configured, you can chat with your assistant and ask it to:
    
    - Answer general knowledge questions
    - Check the current time
    - Get weather updates for a location
    - Perform web searches
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.text_input("Assistant Name", key="assistant_name", 
                     placeholder="e.g., Aurora, Max, Jarvis")
    
    with col2:
        st.text_area("Personality Description", key="assistant_personality", 
                    placeholder="e.g., Friendly and helpful with a touch of humor")
    
    st.button("Create My Assistant", on_click=customize_assistant)
    st.markdown("---")
    st.markdown("### API Configuration")
    st.markdown("""
    Configure API keys to enable additional features. These settings are optional but recommended for the best experience.
    """)
    
    st.text_input(
        "OpenAI API Key", 
        value=st.session_state.api_keys["OPENAI_API_KEY"], 
        type="password",
        help="Required for the assistant to respond to questions. Get it from openai.com",
        key="openai_key_input",
        on_change=lambda: st.session_state.api_keys.update({"OPENAI_API_KEY": st.session_state.openai_key_input})
    )
    
    st.text_input(
        "Weather API Key (OpenWeatherMap)", 
        value=st.session_state.api_keys["WEATHER_API_KEY"], 
        type="password",
        help="Required for weather information. Get a free API key from openweathermap.org",
        key="weather_key_input",
        on_change=lambda: st.session_state.api_keys.update({"WEATHER_API_KEY": st.session_state.weather_key_input})
    )
    
    st.text_input(
        "SerpAPI Key", 
        value=st.session_state.api_keys["SERPAPI_KEY"], 
        type="password",
        help="Required for web search capability. Get it from serpapi.com",
        key="serpapi_key_input",
        on_change=lambda: st.session_state.api_keys.update({"SERPAPI_KEY": st.session_state.serpapi_key_input})
    )
    
    if st.button("Save API Keys"):
        update_api_keys()

else:
    st.subheader(f"Chat with {st.session_state.assistant.name}")
    
    with st.sidebar:
        st.markdown(f"### {st.session_state.assistant.name}")
        st.markdown(f"*{st.session_state.assistant.personality}*")
        
        st.markdown("### Features")
        st.markdown("""
        - Answer questions
        - Check the time
        - Get weather updates
        - Perform web searches
        """)
        
        if st.button("API Settings"):
            toggle_api_settings()
            st.rerun()
            
        if st.button("Reset Assistant"):
            st.session_state.setup_complete = False
            st.session_state.assistant = Assistant("Assistant", "I'm a helpful AI assistant.")
            st.session_state.chat_history = []
            st.rerun()
    
    if st.session_state.show_api_settings:
        with st.expander("API Settings", expanded=True):
            st.markdown("### Configure API Keys")
            st.markdown("""
            These keys enable additional features for your assistant. All keys are stored securely in your session.
            """)
            
            st.text_input(
                "OpenAI API Key", 
                value=st.session_state.api_keys["OPENAI_API_KEY"], 
                type="password",
                help="Required for the assistant to respond to questions. Get it from openai.com",
                key="openai_key_chat",
                on_change=lambda: st.session_state.api_keys.update({"OPENAI_API_KEY": st.session_state.openai_key_chat})
            )
            
            st.text_input(
                "Weather API Key (OpenWeatherMap)", 
                value=st.session_state.api_keys["WEATHER_API_KEY"], 
                type="password",
                help="Required for weather information. Get a free API key from openweathermap.org",
                key="weather_key_chat",
                on_change=lambda: st.session_state.api_keys.update({"WEATHER_API_KEY": st.session_state.weather_key_chat})
            )
            
            st.text_input(
                "SerpAPI Key", 
                value=st.session_state.api_keys["SERPAPI_KEY"], 
                type="password",
                help="Required for web search capability. Get it from serpapi.com",
                key="serpapi_key_chat",
                on_change=lambda: st.session_state.api_keys.update({"SERPAPI_KEY": st.session_state.serpapi_key_chat})
            )
            
            col1, col2 = st.columns([1, 3])
            with col1:
                if st.button("Save Keys"):
                    update_api_keys()
            with col2:
                if st.button("Close", key="close_api_settings"):
                    toggle_api_settings()
                    st.rerun()
    
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.chat_history:
            if message["role"] == "user":
                st.markdown(f"**You:** {message['content']}")
            else:
                st.markdown(f"**{st.session_state.assistant.name}:** {message['content']}")
    
    user_input = st.chat_input("Type your message here...")
    if user_input:
        handle_user_message(user_input)
        st.rerun()

if st.session_state.setup_complete and len(st.session_state.chat_history) == 0:
    st.session_state.chat_history.append({
        "role": "assistant", 
        "content": f"Hello! I'm {st.session_state.assistant.name}. {st.session_state.assistant.personality} How can I help you today?"
    })
    st.rerun()

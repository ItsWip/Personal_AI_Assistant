import os
import json
from openai import OpenAI

class Assistant:
    def __init__(self, name, personality):
        """
        Initialize the Assistant with a name and personality.
        
        Args:
            name (str): The name of the assistant
            personality (str): Description of the assistant's personality
        """
        self.name = name
        self.personality = personality
        api_key = os.environ.get("OPENAI_API_KEY")
        self.openai = None
        if api_key:
            try:
                self.openai = OpenAI(api_key=api_key)
            except Exception:
                self.openai = None
    
    def respond_to_query(self, query):
        """
        Generate a response to the user's query using the OpenAI API.
        
        Args:
            query (str): The user's question or input
            
        Returns:
            str: The assistant's response
        """
        if not self.openai:
            return ("I need an OpenAI API key to generate intelligent responses. "
                    "Please set your API key in the API Settings section.")
        
        try:
            # the newest OpenAI model is "gpt-4o" which was released May 13, 2024.
            # do not change this unless explicitly requested by the user
            response = self.openai.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "system", 
                        "content": f"You are {self.name}, an AI assistant with the following personality: {self.personality}. "
                                  f"Provide helpful, accurate, and engaging responses while staying true to your personality. "
                                  f"Keep responses concise and conversational."
                    },
                    {"role": "user", "content": query}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"I apologize, but I'm having trouble processing your request right now. Error: {str(e)}"

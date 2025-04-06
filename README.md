Personalized AI Assistant BuilderThis project empowers you to create your own AI assistant with customized behavior by integrating your own API keys for OpenAI, SerpAPI, and OpenWeatherMap. This approach grants you control over service usage and costs, and enables you to tailor the assistant's capabilities to your specific requirements.FeaturesPersonalized API Key Integration:OpenAI: Integrate the core language model for text generation, question answering, and more.SerpAPI: Enable web search capabilities for up-to-date information retrieval and contextual awareness.OpenWeatherMap: Incorporate weather data into the assistant's responses.Modular Design:app.py: Main application entry point.assistant.py: Core AI assistant logic.search_service.py: Handles SerpAPI interactions.weather_service.py: Manages OpenWeatherMap API communication.web_scraper.py: (Potentially) Extracts information from websites..env Configuration: Securely stores API keys and sensitive information.requirements.txt: Lists project dependencies for easy setup..gitignore: Specifies untracked files (e.g., .env, __pycache__).Getting StartedPrerequisitesPython 3.xAPI Keys:OpenAISerpAPIOpenWeatherMapInstallationClone the repository:git clone [<repository_url>](https://github.com/ItsWip/Personal_AI_Assistant.git)
Create a virtual environment:python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
Install dependencies:pip install -r requirement.txt
Configure API Keys:When you run the program, separate text inputs will be provided for you to enter your API keys.Enter your API keys for OpenAI, SerpAPI, and OpenWeatherMap into the appropriate fields within the application's interface.Important: The application will securely store the keys within your session.  You do not need to create or edit a .env file.Running the Assistantpython app.py
Project Structure.
├── .env
├── .gitignore
├── app.py
├── assistant.py
├── requirement.txt
├── search_service.py
├── weather_service.py
└── web_scraper.py
UsageInteract with the assistant through the application's interface. Capabilities include:AI-powered responses (OpenAI)Web search (SerpAPI)Weather information (OpenWeatherMap)CustomizationModify the Python files to tailor the assistant's behavior:assistant.py: Adjust prompts, logic, and service interactions.search_service.py: Refine SerpAPI queries.weather_service.py: Customize weather data retrieval.app.py: Change the user interface.ContributingFork the repository.Create a new branch.Commit your changes.Push to your fork.Submit a pull request.

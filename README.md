# **Personalized AI Assistant Builder**

This project empowers you to create your own AI assistant with customized behavior by integrating your own API keys for OpenAI, SerpAPI, and OpenWeatherMap. This approach grants you control over service usage and costs, and enables you to tailor the assistant's capabilities to your specific requirements.

## **Features**

* **Personalized API Key Integration:**  
  * **OpenAI:** Integrate the core language model for text generation, question answering, and more.  
  * **SerpAPI:** Enable web search capabilities for up-to-date information retrieval and contextual awareness.  
  * **OpenWeatherMap:** Incorporate weather data into the assistant's responses.  
* **Modular Design:**  
  * app.py: Main application entry point.  
  * assistant.py: Core AI assistant logic.  
  * search\_service.py: Handles SerpAPI interactions.  
  * weather\_service.py: Manages OpenWeatherMap API communication.  
  * web\_scraper.py: *(Potentially)* Extracts information from websites.  
* **.env Configuration**: Securely stores API keys and sensitive information.  
* requirements.txt: Lists project dependencies for easy setup.  
* .gitignore: Specifies untracked files (e.g., .env, \_\_pycache\_\_).

## **Getting Started**

### **Prerequisites**

* Python 3.x  
* API Keys:  
  * OpenAI  
  * SerpAPI  
  * OpenWeatherMap

### **Installation**

1. Clone the repository:  
   git clone \<repository\_url\>  
   cd \<project\_directory\>

2. Create a virtual environment:  
   python \-m venv venv  
   source venv/bin/activate  \# Linux/macOS  
   venv\\Scripts\\activate  \# Windows

3. Install dependencies:  
   pip install \-r requirements.txt

4. Configure API Keys:  
   * When you run the program, separate text inputs will be provided for you to enter your API keys.  
   * Enter your API keys for OpenAI, SerpAPI, and OpenWeatherMap into the appropriate fields within the application's interface.  
   * **Important:** The application will securely store the keys within your session. You do not need to create or edit a .env file.

### **Running the Assistant**

python app.py

## **Project Structure**

.  
├── .env  
├── .gitignore  
├── app.py  
├── assistant.py  
├── requirements.txt  
├── search\_service.py  
├── weather\_service.py  
└── web\_scraper.py

## **Usage**

Interact with the assistant through the application's interface. Capabilities include:

* AI-powered responses (OpenAI)  
* Web search (SerpAPI)  
* Weather information (OpenWeatherMap)

## **Customization**

Modify the Python files to tailor the assistant's behavior:

* assistant.py: Adjust prompts, logic, and service interactions.  
* search\_service.py: Refine SerpAPI queries.  
* weather\_service.py: Customize weather data retrieval.  
* app.py: Change the user interface.

## **Contributing**

1. Fork the repository.  
2. Create a new branch.  
3. Commit your changes.  
4. Push to your fork.  
5. Submit a pull request.
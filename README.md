# Healthcare Chatbot Code
This code sets up a healthcare chatbot assistant using Streamlit and Azure OpenAI. It provides a user-friendly interface where users can input their symptoms or health-related questions and receive responses from an AI assistant. The assistant uses the GPT model deployed on Azure OpenAI.

**Requirements**
- Azure Open AI Key and Endpoint
- dotenv
- streamlit
- openai==0.28
- decouple

Snapshot of this program 

![2024-06-27_15h50_33](https://github.com/alyxxxv/azure_open_ai_chat/assets/87213160/8ec26104-648a-4826-bb45-e619786fef2e)

![2024-06-27_15h51_45](https://github.com/alyxxxv/azure_open_ai_chat/assets/87213160/28e62549-3a53-492a-94dc-6060896cde03)

![2024-06-27_15h52_18](https://github.com/alyxxxv/azure_open_ai_chat/assets/87213160/e846b608-3bfa-40c1-bc53-06417a34a392)


**Summary**
- Custom CSS enhances the UI for a better user experience.
- Session state is used to maintain conversation context and user information across interactions.
- Chat history display function formats and displays messages in a chat bubble style.
- User input handling includes capturing the user's name and processing health-related queries.
- OpenAI integration uses the Azure deployment to generate responses from the AI assistant.
- This code sets up a basic but polished healthcare chatbot assistant that can be further expanded with additional features and improvements.



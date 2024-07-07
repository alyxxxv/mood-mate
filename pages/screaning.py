
import streamlit as st

def screaning():
  # Streamlit app title
  st.title('Health Bot - Screener :stethoscope:')
  st.write('Assist you in screening your mental health issues and giving first aid solution.')

  # Embed the chatbot using an iframe
  html_code = """
  <!DOCTYPE html>
  <html>
    <head>
      <title>Azure Health Bot</title>
      <style>
        html, body {
          height: 100%;
          margin: 0;
          display: flex;
          justify-content: center;
          align-items: center;
          background-color: #0E1117; /* Set a light background color */
        }
        #webchat-container {
          height: 80vh; /* Adjust the height of the chat window */
          width: 80vh; /* Adjust the width of the chat window to 95% of the viewport */
          max-width: 1200px; /* Limit the maximum width of the chat window */
          border: 2px solid #3498db; /* Blue border */
          border-radius: 20px; /* Rounded corners */
          overflow: hidden; /* Hide overflow content */
          box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* Add a subtle shadow */
        }
        #webchat {
          height: 100%;
          width: 100%;
        }
      </style>
      <script src="https://cdn.botframework.com/botframework-webchat/latest/webchat.js"></script>
    </head>
    <body>
      <div id="webchat-container">
        <div id="webchat" role="main"></div>
      </div>
      <script>
        (async function() {
          const res = await fetch('https://directline.botframework.com/v3/directline/tokens/generate', {
            method: 'POST',
            headers: {
              'Authorization': `Bearer 0-mmmfQalrc.UNeg6TnvVAlFFSBcbS5kmYMiq4KmdQMweaBwUBo9Pmk` //WEBCHAT_SECRET
            }
          });
          const { token } = await res.json();

          window.WebChat.renderWebChat(
            {
              directLine: window.WebChat.createDirectLine({ token }),
              userID: 'user1',
              username: 'User'
            },
            document.getElementById('webchat')
          );
        })();
      </script>
    </body>
  </html>
  """

  st.components.v1.html(html_code, height=800)

import openai
import os
from smolagents.agents import ChatMessage 

class OpenAIModel:
    def __init__(self, model_name="gpt-4o", temperature=0.7):
        self.model_name = model_name
        self.temperature = temperature
        self.client = openai.OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY")
        )

    def generate(self, prompt, stop_sequences=None):
        """
        Send a prompt to OpenAI API and return the completion text,
        wrapped in a smolagents.ChatMessage object.
        """
        try:
            messages_list = []
            if isinstance(prompt, str):
                messages_list = [{"role": "user", "content": prompt}]
            elif isinstance(prompt, list):
                # Ensure each item in the list is a dict for OpenAI API
                messages_list = [
                    {"role": msg.role, "content": msg.content} if hasattr(msg, 'role') and hasattr(msg, 'content') else msg
                    for msg in prompt
                ]
            elif isinstance(prompt, dict) and "messages" in prompt:
                messages_list = prompt["messages"]
            else:
                # Fallback for unexpected prompt types, or raise an error
                raise ValueError(f"Unexpected prompt type: {type(prompt)}. Expected str, list, or dict.")


            completion_args = {
                "model": self.model_name,
                "messages": messages_list,
                "temperature": self.temperature,
            }

            if stop_sequences:
                completion_args["stop"] = stop_sequences

            response = self.client.chat.completions.create(**completion_args)
            
            # Extract the assistant's reply text
            assistant_reply_text = response.choices[0].message.content

            # *** THIS IS THE CRUCIAL CHANGE ***
            # Return a ChatMessage object with the role and content
            return ChatMessage(role="assistant", content=assistant_reply_text)

        except openai.APIStatusError as e:
            print(f"OpenAI API Error: {e.status_code} - {e.response}")
            # Even in error, it might be good to return a ChatMessage with error info
            return ChatMessage(role="system", content=f"An OpenAI API error occurred: {e.message}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return ChatMessage(role="system", content=f"An unexpected error occurred: {e}")
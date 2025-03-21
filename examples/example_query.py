#!/usr/bin/env python3
"""
Example script showing how to interact with the LM Studio Bridge directly.
This is just for testing purposes - normally you would use the bridge via Claude's MCP.
"""

import requests
import json

# Update this URL if your LM Studio is running on a different port
LMSTUDIO_URL = "http://localhost:1234/v1/chat/completions"

def query_local_model(prompt, system_prompt="", temperature=0.7, max_tokens=1024):
    """
    Send a query to the local LM Studio model.
    
    Args:
        prompt (str): The user's message/query
        system_prompt (str): Optional system instructions
        temperature (float): Controls randomness (0.0 to 1.0)
        max_tokens (int): Maximum number of tokens to generate
        
    Returns:
        str: The model's response
    """
    # Build the messages array
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})
    
    # Build the request payload
    payload = {
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    
    try:
        # Send the request to LM Studio
        response = requests.post(LMSTUDIO_URL, json=payload)
        
        # Check for errors
        if response.status_code != 200:
            return f"Error: LM Studio returned status code {response.status_code}"
        
        # Parse the response
        response_json = response.json()
        choices = response_json.get("choices", [])
        if not choices:
            return "Error: No response generated"
        
        # Extract the content
        message = choices[0].get("message", {})
        content = message.get("content", "")
        
        if not content:
            return "Error: Empty response from model"
        
        return content
    
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    # Example usage
    user_prompt = input("Enter your prompt: ")
    
    # Optional: Add a system prompt
    system_prompt = "You are a helpful assistant. Answer concisely and accurately."
    
    # Get the response
    response = query_local_model(user_prompt, system_prompt)
    
    # Print the response
    print("\nModel response:")
    print("--------------")
    print(response)

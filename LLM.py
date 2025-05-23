from openai import OpenAI

client = OpenAI(api_key="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",
                base_url="https://openrouter.ai/api/v1")


message = input("Cual es tu pregunta: ") 
prompt = f"Por favor responde de manera clara y sin símbolos innecesarios. Evita usar otros idiomas que no sean el español y escribe una respuesta concisa. Pregunta del usuario: {message}"
        
completion = client.chat.completions.create(
    model="cognitivecomputations/dolphin3.0-r1-mistral-24b:free",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(completion.choices[0].message.content)
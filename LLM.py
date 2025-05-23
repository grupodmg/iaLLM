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
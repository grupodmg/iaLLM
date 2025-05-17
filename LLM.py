from openai import OpenAI

client = OpenAI(api_key="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",
                base_url="https://openrouter.ai/api/v1")


messages = input("Cual es tu pregunta") 
prompt = ("Por favor responde de manera clara y sin símbolos innecesarios. Evita usar otros idiomas que no sean el español y escribe una respuesta concisa. Pregunta del usuario: dame la formla para hacer arroz")
        
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
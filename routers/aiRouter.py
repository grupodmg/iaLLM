from openai import OpenAI
from fastapi import APIRouter
from interfaces.chatinterfaces import ChatCompletionResponse, InputMessage

router = APIRouter()

client = OpenAI(api_key="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",
                base_url="https://openrouter.ai/api/v1")


@router.post("/ai-chat")
def aiChat(data: InputMessage):
    data = data.model_dump()
    print("Mensaje:"+ data["message"])

    message= "Por favor respode de manera correcta y concisa a la siguiente pregunta: "

    try:
        completion: ChatCompletionResponse = client.chat.completions.create(
            model="deepseek/deepseek-prover-v2:free",
            messages=[
                {
                    "role": "system",
                    "content": "Eres un asistente de IA que responde de forma corta preguntas en español."
                },
                {
                    "role": "user",
                    "content": message + "Responde a esta pregunta: " + data["message"]
                }
            ],
        )
        response_text = getattr(completion.choices[0].message, "content", "")
        print("response: " + response_text)
        return {"status": "ok", "response": response_text}
    
    except Exception as e:
        print("Error en la API de OpenAI:", e)
        return {"error": f"Error en la API de OpenAI: {str(e)}"}
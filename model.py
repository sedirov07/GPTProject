import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


class AIModel:
    def __init__(self):
        if torch.cuda.is_available():
            self.device = torch.device("cuda")
        else:
            self.device = torch.device("cpu")

        self.model = AutoModelForCausalLM.from_pretrained(
            "microsoft/phi-2",
            torch_dtype="auto",
            trust_remote_code=True
        ).to(self.device)

        self.tokenizer = AutoTokenizer.from_pretrained(
            "microsoft/phi-2",
            trust_remote_code=True
        )

    def generate_response(self, input_text):
        inputs = self.tokenizer(input_text, return_tensors="pt", return_attention_mask=False).to(self.device)
        outputs = self.model.generate(**inputs, max_length=200)
        return self.tokenizer.batch_decode(outputs)[0]

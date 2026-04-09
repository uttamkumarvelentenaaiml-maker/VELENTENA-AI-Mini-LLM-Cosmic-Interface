from transformers import pipeline

print("_____ Loading Mini LLM model____")

# Use supported task
generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

print(" Model loaded successfully!")


def generate_text(prompt):
    try:
        print(f" Generating for: {prompt}")

        result = generator(
            prompt,
            max_length=100,
            do_sample=True,
            temperature=0.7
        )

        return result[0]['generated_text'].strip()

    except Exception as e:
        return f"Error: {str(e)}"
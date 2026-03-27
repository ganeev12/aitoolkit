def summarize(text):
    return text[:120] + "..."

if __name__ == "__main__":
    sample = "This is a simple demo showing how a summarization tool might work using basic logic."
    print(summarize(sample))

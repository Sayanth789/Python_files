import spacy 

nlp = spacy.load("en_core_web_sm")

def extract_numbers(doc):
    nums = [] 
    for token in doc:
        if token.like_num:
            nums.append(float(token.text))
    return nums 

def detect_intent(text):
    text = text.lower()

    if "into" in text or "multiply" in text or "times" in text:
        return "mul"

    if "percent" in text or "%" in text:
        return "percent"
    elif "earned" in text and "spent" in text:
        return "savings"
    elif "minus" in text or "subtract" in text:
        return "subtract"
    elif "add" in text:
        return "add"
    return "unknown"

def solve(text):
    doc = nlp(text)
    nums = extract_numbers(doc)
    intent = detect_intent(text)

    if intent == "savings" and len(nums) >= 2:
        return nums[0] - nums[1]
    
    if intent == "percent" and len(nums) >= 2:
        return nums[0] *  nums[1] / 100
    
    if intent == "mul" and len(nums) >= 2:
        return nums[0] * nums[1]
    
    return "Cannot solve yet."

# test 
print(solve("I earned 30000 and spent 12000"))
print(solve("What is 10 percent of 5000"))
    
print(solve("what is 12 into 1000"))


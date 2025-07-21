import wikipedia
topic = input("Enter a topic to search on Wikipedia: ")
try:
    summary = wikipedia.summary(topic, sentences=5)
    print("\n🔎 Summary:")
    print(summary)

except wikipedia.exceptions.DisambiguationError as e:
    print("❗Your search was too broad. Suggestions:")
    print(e.options)

except wikipedia.exceptions.PageError:
    print("❌ No matching page found.")

except Exception as e:
    print("Something went wrong:", e)
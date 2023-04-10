import re

def read_template(filepath):
    with open(filepath) as f:
        return f.read().strip()

def parse_template(template: str):
    stripped = re.sub(r"{(.+?)}", '{}', template)
    parts = re.findall(r"{(.+?)}", template)
    return stripped, tuple(parts)

def merge(stripped_template, parts):
    return stripped_template.format(*parts)

def main():
    print("Welcome to Madlib! We'll need a few words from you to make a story.")

    filepath = "assets/make_me_a_video_game.txt"
    template = read_template(filepath)
    stripped_template, parts = parse_template(template)

    user_inputs = []
    for part in parts:
        user_input = input(f"Please give me a {part}: ")
        user_inputs.append(user_input)

    completed_madlib = merge(stripped_template, user_inputs)

    print(completed_madlib)

    with open("assets/completed_madlib.txt", "w") as f:
        f.write(completed_madlib)

if __name__ == "__main__":
    main()
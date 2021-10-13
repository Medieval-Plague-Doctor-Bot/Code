from datetime import datetime

async def time_formatter(obj):
    timestamp = datetime.timestamp(obj)
    return f"<t:{round(timestamp)}:R>"

def clean_code(content):
    if content.startswith("```") and content.endswith("```"):
      return "\n".join(content.split("\n")[1:])[:-3]
    else:
      return content


def indent(text, prefix, predicate=None):
    if predicate is None:
      def predicate(line):
        return line.strip()
    def prefixed_lines():
      for line in text.splitlines(True):
        yield (prefix + line if predicate(line) else line)
    return "".join(prefixed_lines())

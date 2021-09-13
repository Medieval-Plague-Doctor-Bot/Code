from datetime import datetime

async def time_formatter(obj):
    timestamp = datetime.timestamp(obj)
    return f"<t:{round(timestamp)}:R>"

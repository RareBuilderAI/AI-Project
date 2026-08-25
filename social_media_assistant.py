class SocialMediaAssistant:

    def __init__(self):
        self.contents = []


    def create_content(self, platform, content_type, topic, idea, caption):

        content = {
            "platform": platform,
            "content_type": content_type,
            "topic": topic,
            "idea": idea,
            "caption": caption
        }

        self.contents.append(content)

        return "Content created successfully!"


    def show_content(self):

        if not self.contents:
            return "No content created yet."

        result = "📱 Content Library:\n\n"

        for index, content in enumerate(self.contents, start=1):

            result += (
                f"{index}. Platform: {content['platform']}\n"
                f"Type: {content['content_type']}\n"
                f"Topic: {content['topic']}\n"
                f"Idea: {content['idea']}\n"
                f"Caption: {content['caption']}\n\n"
            )

        return result


    def search_content(self, keyword):

        results = []

        for content in self.contents:

            if (
                keyword.lower() in content["platform"].lower()
                or keyword.lower() in content["topic"].lower()
                or keyword.lower() in content["idea"].lower()
            ):
                results.append(content)


        if not results:
            return "No matching content found."


        message = "🔎 Search Results:\n\n"

        for index, content in enumerate(results, start=1):

            message += (
                f"{index}. {content['platform']} - {content['topic']}\n"
                f"Idea: {content['idea']}\n"
                f"Caption: {content['caption']}\n\n"
            )

        return message


    def edit_content(self, number, new_caption):

        if 1 <= number <= len(self.contents):

            self.contents[number - 1]["caption"] = new_caption

            return "✏️ Content updated successfully!"

        return "Invalid content number."


    def delete_content(self, number):

        if 1 <= number <= len(self.contents):

            removed = self.contents.pop(number - 1)

            return f"🗑️ Deleted: {removed['idea']}"

        return "Invalid content number."
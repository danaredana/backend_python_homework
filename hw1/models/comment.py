from datetime import datetime


class Comment:
    def __init__(self, author_id: str, text: str) -> None:
        self.author_id = author_id
        self.text = text
        self.create_data = datetime.now()
        self.update_data = self.create_data
        self.like_count = 0

    def edit_comment(self, new_text: str) -> None:
        self.text = new_text
        self.update_data = datetime.now()

    def like(self) -> None:
        self.like_count += 1

    def dislike(self) -> None:
        self.like_count -= 1

    def __repr__(self) -> str:
        is_changed = (self.update_data != self.create_data)
        edited_str = f"\nEdited at: {self.update_data}" if is_changed else ""
        return f"Comment from {self.author_id}: {self.text}, likes={self.like_count}\nPosted at: {self.create_data}{edited_str}"

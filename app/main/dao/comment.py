# Класс абстракции комментария
class Comment:
    def __init__(self,
                 pk=0,
                 post_id=0,
                 commenter_name="",
                 comment="",
                 ):
        self.pk = pk
        self.post_id = post_id
        self.commenter_name = commenter_name
        self.comment = comment

    def __repr__(self):
        return f"Comment(" \
               f"{self.pk}," \
               f"{self.post_id}," \
               f"{self.commenter_name}," \
               f"{self.comment}," \
               f")"

    def as_dict(self):
        dict_data = {
            "post_id": self.post_id,
            "commenter_name": self.commenter_name,
            "comment": self.comment,
            "pk": self.pk
        }

        return dict_data

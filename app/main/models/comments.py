class Comment:

    all_comments = []

    def __init__(self,comment):
        self.comment


    def save_comment(self):
        Comment.all_comments.append(self)


    @classmethod
    def clear_commentscls):
        Comments.all_comments.clear()


    @classmethod
    def get_pitches(cls,id):

        response = []

        for comment in cls.all_comments:
            response.append(comment)
            
            return response   
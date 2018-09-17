class Blog:

    all_blogs = []

    def __init__(self,blog):
        self.blog


    def save_blog(self):
        Blog.all_blogs.append(self)


    @classmethod
    def clear_blogs(cls):
        Blog.all_blogs.clear()


    @classmethod
    def get_blogs(cls,id):

        response = []

        for blog in cls.all_blogs:
            response.append(blog)
            
            return response     
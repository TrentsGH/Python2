from PIL import ImageTk, Image
def upload(path):
    return ImageTk.PhotoImage(Image.open(path))
    

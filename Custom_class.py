class Rectangle:
    def __init__(self,length:int,width:int):
        self.length=length
        self.width=width
    def print_attribute(self):
        attr={"length":self.length,"width":self.width}
        for key,value in attr.items():
            print({key:value})

rect=Rectangle(4,6)
rect.print_attribute()

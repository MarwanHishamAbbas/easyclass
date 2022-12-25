# easyclass

## Customize the form input using the **init** and for loop

    def __init__(self):
            super().__init_)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'input-field'
                visible.field.widget.attrs['required'] = True

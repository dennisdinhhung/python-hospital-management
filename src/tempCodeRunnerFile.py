def changeColor(button, colorEntry, colorLeave):
        button.bind("<Enter>", func=lambda e: button.config(background=colorEntry))
        button.bind("<Leave>", func=lambda e: button.config(background=colorLeave))
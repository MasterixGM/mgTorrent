# Function to load the stylesheet
def load_stylesheet(self, filepath):
    try:
        with open(filepath, "r") as f:
            stylesheet = f.read()
            self.setStyleSheet(stylesheet)
    except:
        print("Error Loading the StyleSheet")       
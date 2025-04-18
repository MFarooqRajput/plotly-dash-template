from server import app
from layouts.main import main_layout

# Include layout
app.layout = main_layout

# Include callbacks (Needs to be assigned after setting layout up)
from callbacks.main import *

# Initializing app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

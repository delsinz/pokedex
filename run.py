# The driver for the application
from app import app
import sys
# Change default encoding to properly display some symbols..
reload(sys)
sys.setdefaultencoding('utf8')

app.run(debug=True)
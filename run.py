import os
import sys
from app import create_app

if sys.argv:
        #set environment from command line argument
        os.environ['ENV'] =  str(sys.argv[1])
        #create app
        app = create_app()
        #run app
        if __name__ == '__main__':
           port = int(os.environ.get("PORT", 5000))
           app.run(host='0.0.0.0', port=port, debug=True)
else:
    print('Enviroment missing in startup command')

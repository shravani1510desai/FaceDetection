from flask import *
from imgrender import *
import os
app = Flask(__name__,static_url_path='/static')


@app.route('/',methods=['GET','POST'])
def show_index():
    fileloc = request.args.get('renderedimage',default=None,type=str)
    numfaces = request.args.get('numfaces',default=None,type=int)
    if fileloc == 'error':
        error = 'You did not pass any file'
    else:
        error = False
    #print(fileloc)
    return render_template('index.html',fileloc = fileloc,error=error,numfaces=numfaces)

@app.route('/renderimage',methods=['POST'])
def render_image_now():
    files = request.files
    #print(files)
    #print(dir(files))
    cwd = os.getcwd()
    try:
        file = files['imagetorender']
        name = file.filename
        image_loc = f"static/images/{name}"
        file.save(image_loc)
        try:
            rendered = render_image(image_loc)
        except:
            rendered = False
        if rendered != False:
            return redirect(f'/?renderedimage={image_loc}&numfaces={rendered}')
            #return redirect(url_for(show_index,renderedimage=image_loc))
        else:
            return redirect(f'/?renderedimage=error')
    except:
        return redirect(f'/?renderedimage=error')

app.run(debug=True,port=8000)
def fill_page(my_list):
    template = '''<!DOCTYPE html>
    <html>
    <head>
    <title>EditPage</title>
    </head>

    <h1>
    <textarea rows="1" cols="30" %s>
    %s
    </textarea>
    </h1>

    <body>
    <textarea name="texta" rows="10" cols="30" %s>
    %s
    </textarea><br>
    </body>

    <button onclick="location.href='%s'">
        %s</button>

    </html>''' %(my_list[0], my_list[1], my_list[2], my_list[3], my_list[4], my_list[5])

    return template


if __name__ == '__main__':
    with open('frontPage.html', 'w') as f:
        f.write(fill_page(['disabled', 'Title FRONT','disabled', 'Text FRONT', '/home/likewise-open/3PILLAR/oratiu/work/workspace/Workspace/site/editPage.html', 'EDIT']))
    with open('editPage.html', 'w') as f:
        f.write(fill_page(['', 'Title EDIT','' , 'Text EDIT', '/home/likewise-open/3PILLAR/oratiu/work/workspace/Workspace/site/frontPage.html', 'SAVE']))


   

#182..../ -> /FrontPage/
#182..../<page>/
#182..../edit/<page>/
#182..../save/<page>/ -> /<page>/

edit_page_template = """
<!DOCTYPE html>
<html>
    <head>
        <title>Edit %(page_name)s</title>
    </head>
    <body>
        <form method="post" action="/save/%(page_name)s/">
            <h1>%(page_name)s</h1>
            <div>
                <label for="contentid">Content</label>
                <textarea id="contentid" name="content" rows="10" cols="30">%(page_content)s</textarea>
            </div>
            <div>
                <input type="submit" value="SAVE" />
                <a href="/%(page_name)s/">Cancel</a>
            </div>
        </form>
    </body>
</html>
"""

def render_edit_page(page_name, page_content):
    return edit_page_template % {'page_name': page_name, 'page_content': page_content}


view_page_template = """
<!DOCTYPE html>
<html>
    <head>
        <title>%(page_name)s</title>
    </head>

    <body>
        <h1>%(page_name)s</h1>
        <p>%(page_content)s</p>
        <a href="/edit/%(page_name)s">Edit</a>
    </body>
</html>
"""

def render_view_page(page_name, page_content):
    return view_page_template % {'page_name': page_name, 'page_content': page_content}
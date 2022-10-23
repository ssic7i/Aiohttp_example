from views import index, add_data, get_all, get_one


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/add', add_data)
    app.router.add_get('/show', get_all)
    app.router.add_get('/get/{doc_id}', get_one)

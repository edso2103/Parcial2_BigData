from noticias import download_page

def test_obtenerNoticias():
    assert download_page('https://www.eltiempo.com', 'bucket-news21','elTiempo-')==None

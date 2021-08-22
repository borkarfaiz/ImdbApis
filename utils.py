

def generate_url(urls_list):
    return '/' + '/'.join(url.strip('/') for url in urls_list)
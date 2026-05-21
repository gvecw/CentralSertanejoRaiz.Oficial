from pywebcopy import save_webpage

url = 'https://sertanejoraizoficial.vercel.app/'
download_folder = 'c:/Users/Pichau/OneDrive/PENDRIVERS/google ads/'

kwargs = {
    'bypass_robots': True,
    'project_name': 'sertanejoraiz'
}

save_webpage(url, download_folder, **kwargs)

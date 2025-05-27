import os
import requests
import tarfile

def ffmpeg_download(dest_folder='.'):

    ffmpeg_path=os.path.join(dest_folder,'ffmpeg')
    if os.path.isfile(ffmpeg_path) and os.access(ffmpeg_path,os.X_OK):
        return

    url="https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-i686-static.tar.xz"
    archive_path="ffmpeg.tar.xz"

    with requests.get(url,stream=True) as r:
        r.raise_for_status()
        with open(archive_path,'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    with tarfile.open(archive_path,'r:xz') as tar:
        for member in tar.getmembers():
            #if os.path.basename(member.name)=='ffmpeg':
                #member.name='ffmpeg'
                #tar.extract(member,path=dest_folder)
                #os.chmod(os.path.join(dest_folder,'ffmeg'),0o755)
            
            if member.isfile() and os.path.basename(member.name)=="ffmpeg":
                extracted_file=tar.extractfile(member)
                with open(ffmpeg_path,'wb') as out:
                    out.write(extracted_file.read())
                #extracted_path=os.path.join(dest_folder,member.name)
                #final_path=os.path.join(dest_folder,'ffmpeg')
                #os.rename(extracted_path,final_path)
                os.chmod(ffmpeg_path,0o755)
                break

    os.remove(archive_path)

#ffmpeg_download()
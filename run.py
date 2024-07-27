import os

in_dir_glb = "/home/duc/Documents/model"
os.system(f"docker run --name convert_usdz -v {in_dir_glb}:/tmp vto/convert")

out_dir_usdz = "/home/duc/Documents/model"
os.system(f"docker cp convert_usdz:/tmp/avatar.usdz {out_dir_usdz}/avatar.usdz")
os.system("docker rm convert_usdz")
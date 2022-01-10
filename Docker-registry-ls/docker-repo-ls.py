#!/usr/bin/env python3 
import requests
from rich.console import Console
from rich.table import Table
import sys

repo_url = "localhost:5000"
if len(sys.argv) == 2:
    repo_url = sys.argv[1]

try:
    images= requests.get(f"http://{repo_url}/v2/_catalog")
    if images.status_code == 200:
        table = Table(title=f"ALL Images List in Docker Repo at {repo_url} ",title_style="bold turquoise2", header_style="bold deep_sky_blue2 ",style="bold red",min_width=80)
        table.add_column("Repositories",justify="left",overflow="crop", style="magenta")
        table.add_column("Tags",style="green",overflow="crop")
        images =images.json()
        try:
            for i in images['repositories']:
                tag = requests.get(f"http://{repo_url}/v2/{i}/tags/list").json()
                bb = f' {" "*2}||{" "*2} '.join(tag['tags'])
                table.add_row(str(i),str(bb))
            
            console = Console()
            console.print(table)
        except:
            print("Problem in Tag")
except:
    print(f"NO Repositories Found at {repo_url} ")









set Docker local registry
```bash
 docker run -d -p 5000:5000 --restart=always --name registry registry:2

```
install pkg

```bash
pip3 install requests rich
```
- make excutale py script
- mv scrpit to `~/.local/bin/`


```bash
 docker-repo-ls

 docker-repo-ls <registry-address>
```
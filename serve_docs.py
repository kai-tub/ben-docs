from livereload import Server, shell

server = Server()
run_cmd = shell("just build")
for watch_dir in [
    "docs/*.py",
    "docs/*.rst",
    "docs/*.md",
    "docs/*.py",
    "docs/*.yml",
    "docs/*.ipynb",
]:
    server.watch(watch_dir, run_cmd)

server.serve(root="docs/_build/")

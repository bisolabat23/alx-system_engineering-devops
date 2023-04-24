#!/usr/bin/env python3
# Fabfile defining functions to pack, deploy, and clean the
# current directory to a remote server.
from fabric import task


@task
def pack(c):
    """Create a tar gzipped archive of the current directory."""
    c.run("touch alxonwebapp.tar.gz")
    c.run("tar --exc‚Ålude='*.tar.gz' -cvzf alxonwebapp.tar.gz .")


@task
def deploy(c):
    """Upload the archive to the remote server in the /tmp/ directory."""
    c.user = "ubuntu"
    c.put("alxonwebapp.tar.gz", "/tmp")
    c.run("mkdir /tmp/alxonwebapp")
    c.run("tar -C /tmp/alxonwebapp -xzvf /tmp/alxonwebapp.tar.gz")


@task
def clean(c):
    """Deletes alxonwebapp.tar.gz on the local machine."""
    c.run("rm alxtonwebapp.tar.gz")

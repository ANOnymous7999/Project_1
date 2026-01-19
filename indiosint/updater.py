import subprocess
import os
from .utils import print_info, print_success, print_error, print_warning

def check_for_updates():
    """Checks if the local repository is behind the remote."""
    if not os.path.exists(".git"):
        print_error("Not a Git repository. Update feature is disabled.")
        return False

    print_info("Checking for updates...")
    try:
        # Fetch the latest changes from the remote
        subprocess.run(["git", "fetch"], check=True, capture_output=True)

        # Check if upstream exists
        upstream = subprocess.run(["git", "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}"], capture_output=True, text=True)
        if upstream.returncode != 0:
            print_warning("No upstream branch configured. Cannot check for updates.")
            return False

        # Compare local HEAD with remote HEAD
        local_hash = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()
        remote_hash = subprocess.check_output(["git", "rev-parse", "@{u}"]).decode().strip()

        if local_hash != remote_hash:
            print_warning("A new version is available on GitHub!")
            return True
        else:
            print_success("IndiOSINT is up to date.")
            return False
    except subprocess.CalledProcessError:
        print_error("Failed to check for updates. Ensure you are in a Git repository.")
    except Exception as e:
        print_error(f"An error occurred during update check: {e}")
    return False

def perform_update():
    """Performs a git pull to update the tool."""
    print_info("Updating IndiOSINT...")
    try:
        result = subprocess.run(["git", "pull"], check=True, capture_output=True, text=True)
        print_success("Successfully updated to the latest version!")
        print_info(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print_error(f"Update failed: {e.stderr}")
    except Exception as e:
        print_error(f"An error occurred during update: {e}")
    return False

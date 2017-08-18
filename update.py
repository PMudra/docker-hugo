#!/usr/bin/env python
import json
import sys
import urllib.request
import re
import subprocess

bearer = sys.argv[1]

graphql = """
query { 
  repository(owner: "gohugoio", name: "hugo") {
    releases(last: 1) {
      nodes {
        name
        releaseAssets(first: 1, name: "hugo_checksums.txt") {
          nodes {
            url
          }
        }
      }
    }
  }
}
"""

request = urllib.request.Request("https://api.github.com/graphql", json.dumps({"query": graphql}).encode(),
                                 {"Authorization": "bearer " + bearer, "User-Agent": "docker-hugo-update"}, method="POST")

response = json.loads(urllib.request.urlopen(request).read().decode())
release = response["data"]["repository"]["releases"]["nodes"][0]
checksum_file_url = release["releaseAssets"]["nodes"][0]["url"]
version = release["name"].replace("v", "")
print("new version: " + version)

checksum_file = urllib.request.urlopen(checksum_file_url).read().decode()
checksum_new = re.search("(?P<checksum>[a-f0-9]+)\s{2}.*Linux-64bit.tar.gz", checksum_file).group("checksum")

print("new checksum: " + checksum_new)

content = open("Dockerfile").read()
content_new = re.sub("HUGO_VERSION [0-9.]+", "HUGO_VERSION " + version, content)
content_new = re.sub("HUGO_SHA [a-f0-9]+", "HUGO_SHA " + checksum_new, content_new)
open("Dockerfile", "w").write(content_new)

subprocess.call(["git", "commit", "-am", "Update to Hugo version " + version])
subprocess.call(["git", "checkout", "-b", version])

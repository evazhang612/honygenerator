# https://api.tumblr.com/v2/blog/humansofnewyork.tumblr.com/posts/photo?api_key=Q6vHoaVm5L1u2ZAW1fqv3Jw48gFzYVg9P0vH0VHl3GVy6quoGV

import urllib, urllib.request, json
# https://api.tumblr.com/v2/blog/humansofnewyork.tumblr.com/posts/photo?api_key=Q6vHoaVm5L1u2ZAW1fqv3Jw48gFzYVg9P0vH0VHl3GVy6quoGV&offset=20

output_file=open('corpus.txt', 'w', encoding="utf-8")
post_counter = 0
while True:
    print(post_counter)
    url2 = "https://api.tumblr.com/v2/blog/humansofnewyork.tumblr.com/posts/photo?api_key=Q6vHoaVm5L1u2ZAW1fqv3Jw48gFzYVg9P0vH0VHl3GVy6quoGV&offset=" + str(post_counter)
    with urllib.request.urlopen(url2) as url:
        data = json.loads(url.read().decode())
        arrayOfPosts = data['response']['posts']
        if len(arrayOfPosts) == 0:
            break
        for post in arrayOfPosts:
            content = post['caption']
            if content[-9:] == "<br/></p>":
                content = content[:-10] # rip out ”<br/></p>
            if content[-4:] == "</p>":
                content = content[:-5] # rip out ”</p>"
            content = content[4:] # rip out <p>“
            if content[-4:] == "<br/": # rip out ”<br/><br/
                content = content[:-10]
            if content[:10] == "oday in mi": # oday in microfashion&hellip
                continue
            output_file.write(content + '\n')
    post_counter += 20

output_file.close()

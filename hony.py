# https://api.tumblr.com/v2/blog/humansofnewyork.tumblr.com/posts/photo?api_key=Q6vHoaVm5L1u2ZAW1fqv3Jw48gFzYVg9P0vH0VHl3GVy6quoGV

import urllib, urllib.request, json
# https://api.tumblr.com/v2/blog/humansofnewyork.tumblr.com/posts/photo?api_key=Q6vHoaVm5L1u2ZAW1fqv3Jw48gFzYVg9P0vH0VHl3GVy6quoGV&offset=20

output_file=open('corpus2.txt', 'w', encoding="utf-8")
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

            output_file.write(content + '\n')
    post_counter += 20

output_file.close()

import requests

class PostHandeler:
    def part_one(): # Get the details for the first post in the DB
        r = requests.get("https://jsonplaceholder.typicode.com/posts/")
        response = r.json() # Parse the response as json
        first_post = response[0] # Returns the "0" index post
        firstPost_details = [*first_post][:4] # Return all the 4 json values in "0" index
        print(firstPost_details)

        for detail in firstPost_details: # detail = userId, id, title, body
            print(f"{detail}: {first_post[detail]}")
            print("----------------------")
    
    def part_two(): # Fetch all comments from the first post
        r = requests.get("https://jsonplaceholder.typicode.com/posts/1/comments")
        response = r.json()

        index_value_comments = 0
        
        while index_value_comments < 6: # Because there are 5 index values 
            try: # Fail-safe for the "out of range" error
                comments = response[index_value_comments] # Return all index's for comments
            except:
                pass
            comments_details = [*comments][:4] # fetch all the details for a specific comment
            for comment_detail in comments_details: # same mechanism as "part_one" detail fetch
                print(f"{comment_detail}: {comments[comment_detail]}")
                print("--------------------------")
            index_value_comments += 1 # Increment the value to change comment index
    
    def part_three(): # creates a new post
        payload = {'title':'@5kyw41k3r', 'body':'FOO', 'userId':1}
        r = requests.post("https://jsonplaceholder.typicode.com/posts/", data=payload)
        print(r.status_code)
    def part_four(): # Updates the body of first post
        payload = {'id':1, 'title':'I am the first post', 'body':'I am the first post', 'userId':1}
        r = requests.put("https://jsonplaceholder.typicode.com/posts/1/", data=payload)
        print(r.status_code)
    
    def part_five(): # Deletes the 10th post
        r = requests.delete("https://jsonplaceholder.typicode.com/posts/10")
        print(r.status_code)

#####################################
print("First post:")
print("=============")
PostHandeler.part_one()
print("All comments from the 1st post")
print("======================================")
PostHandeler.part_two()
print("Create Post")
print("========================")
PostHandeler.part_three()
print("Update body and title of first post:")
print("=====================================")
PostHandeler.part_four()
print("Delete post 10 from DB:")
print("=============================")
PostHandeler.part_five()

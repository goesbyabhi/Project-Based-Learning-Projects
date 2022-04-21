import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from time import sleep

# Set scopes
scopes = ["https://www.googleapis.com/auth/youtube",
          "https://www.googleapis.com/auth/youtube.force-ssl",
          "https://www.googleapis.com/auth/youtube.readonly",
          "https://www.googleapis.com/auth/youtubepartner"]


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YOUR-SECRET-CLIENT-ID.json" # Your secret client id name.json comes here 

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    
    while(True):
        request = youtube.videos().list(
            part="snippet,  statistics",
            id="KFvHjIuSfDE"  # Change the video id from here
        )
        response = request.execute()

        data = response["items"][0]
        vid_snippet = data["snippet"]
        title = vid_snippet["title"]

        likes = str(data["statistics"]["likeCount"])

        print(" ")
        print("The title of the video: " + title)
        print("Number of likes on the video: " + likes)

        change = (likes not in title)

        if(change):
            title_updt = "I don't know why this video has " + likes + " likes"
            vid_snippet["title"] = title_updt

            request = youtube.videos().update(
                part="snippet",
                body={
                    "id": "KFvHjIuSfDE",
                    "snippet": vid_snippet
                }
            )
            response = request.execute()

            print("Chek the title");
        
        sleep(300);


if __name__ == "__main__":
    main()

#input("Press Enter to exit")

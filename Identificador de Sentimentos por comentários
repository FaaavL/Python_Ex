import facebook
import matplotlib.pyplot as plt
from textblob import TextBlob


def saveResult(data):
  with open('result.txt', 'w') as file:
    file.write(data)

def parseTextBlob(text):

  blob = TextBlob(text)

  if blob.sentiment.polarity > 0:
    return {
      "text": f"[pos|{blob.sentiment.polarity}] {text}",
      "polarity": blob.sentiment.polarity,
    }
  elif blob.sentiment.polarity < 0:
    return {
      "text": f"[neg|{blob.sentiment.polarity}] {text}",
      "polarity": blob.sentiment.polarity,
    }
  else:
    return {
      "text": f"[neu|{blob.sentiment.polarity}] {text}",
      "polarity": blob.sentiment.polarity,
    }

# 'POC' - Proof Of Concept(Prova De Conceito)
# If do you have a facebook access token you can use the funcion below
# to get the posts from a user
# https://developers.facebook.com/docs/facebook-login/guides/access-tokens/#apptokens
# IMPORTANT: Your app needs to be approved by facebook to get the posts from a user
# https://developers.facebook.com/docs/facebook-login/permissions/#reference-default

def getFacebookPosts():  
  access_token = "642728230797218|bw-v4K_idgDoG9DLX_Y4GXR_J3A"
  user = input("Qual id de perfil você quer pesquisar: ")

  graph = facebook.GraphAPI(access_token)
  profile = graph.get_object(user)
  profile_id = profile['id']
  posts = graph.get_connections(profile_id, 'posts')

  post_result = []
  post_result_polarity = []
  for post in posts['data']:
    message = post['message']
    try:
      parsedTextBlob = parseTextBlob(message)
      post_result.append(parsedTextBlob['text'])
      post_result_polarity.append(parsedTextBlob['polarity'])
    except:
      pass
  
  saveResult(''.join(post_result))
  plotGraph(post_result_polarity)

# getFacebookPosts()



# If you do not have a facebook access token you can use the function below
# to get the posts from a file

def getMockPostsComentaries():
  with open('comments.txt', 'r') as file:
    comments = file.readlines()
    comments_result = []
    comments_result_polarity = []

    for comment in comments:
      parsedTextBlob = parseTextBlob(comment)
      
      comments_result.append(parsedTextBlob['text'])
      comments_result_polarity.append(parsedTextBlob['polarity'])
    
    saveResult(''.join(comments_result))
    plotGraph(comments_result_polarity)
    print("Resultado gerado com sucessso!")


def plotGraph(numbers):
  plt.boxplot([numbers], labels=['Relação'], notch=True, patch_artist=True, boxprops=dict(facecolor='lightblue'))
  plt.title('Relação boxplot dos sentimentos')

  plt.savefig('graph.png')

getMockPostsComentaries()

json.extract! newsarticle, :id, :title, :content, :tag, :url, :launchdate, :website, :imgurl, :created_at, :updated_at
json.url newsarticle_url(newsarticle, format: :json)
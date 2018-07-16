json.extract! news, :id, :title, :date, :link, :share, :preText, :tag, :brand, :created_at, :updated_at
json.url news_url(news, format: :json)

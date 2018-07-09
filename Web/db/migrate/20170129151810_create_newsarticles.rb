class CreateNewsarticles < ActiveRecord::Migration[5.0]
  def change
    create_table :newsarticles do |t|
      t.string :title
      t.string :content
      t.string :tag
      t.string :url
      t.date :launchdate
      t.string :website
      t.string :imgurl

      t.timestamps
    end
  end
end

class CreateNews < ActiveRecord::Migration[5.0]
  def change
    create_table :news do |t|
      t.string :title
      t.string :date
      t.string :link
      t.string :share
      t.string :preText
      t.string :tag
      t.string :brand

      t.timestamps
    end
  end
end

# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20180716020836) do

  create_table "articles", force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=utf8mb4" do |t|
    t.string "title",   limit: 200
    t.string "date",    limit: 45
    t.string "link",    limit: 200
    t.string "share",   limit: 45
    t.string "preText", limit: 2000
    t.string "tag",     limit: 105
    t.string "brand",   limit: 45
  end

  create_table "news", force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=utf8mb4" do |t|
    t.string   "title"
    t.string   "date"
    t.string   "link"
    t.string   "share"
    t.string   "preText"
    t.string   "tag"
    t.string   "brand"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

end

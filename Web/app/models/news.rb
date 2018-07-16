class News < ApplicationRecord
    scope :inside, -> { where( :brand => 'inside' ) }
    scope :technews, -> { where( :brand => 'technews' ) }
    scope :techorange, -> { where( :brand => 'techorange' ) }
end

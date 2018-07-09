Rails.application.routes.draw do
  resources :newsarticles
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  root "newsarticles#index"

end

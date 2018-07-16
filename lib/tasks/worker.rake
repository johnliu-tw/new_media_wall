namespace :jobs do 
    task :work => [ :environment ] do
        if ENV['RAILS_ENV'] == 'production'
            sh "python crawler_production.py"
        else
            sh "python crawler.py"
        end            
    end
end

namespace :jobs do 
    task :work => [ :environment ] do
        sh "python crawler.py"
    end
end

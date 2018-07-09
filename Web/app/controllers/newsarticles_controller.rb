class NewsarticlesController < ApplicationController
  before_action :set_newsarticle, only: [:show, :edit, :update, :destroy]

  # GET /newsarticles
  # GET /newsarticles.json
  def index
    @newsarticles = Newsarticle.all
    @degitalarticles = @newsarticles.where(website: '數位時代')
    @insightarticles = @newsarticles.where(website: 'Insight')
    @techarticles = @newsarticles.where(website: '科技新報')
    @orangearticles = @newsarticles.where(website: '科技報橘')
  end

  # GET /newsarticles/1
  # GET /newsarticles/1.json
  def show
  end

  # GET /newsarticles/new
  def new
    @newsarticle = Newsarticle.new
  end

  # GET /newsarticles/1/edit
  def edit
  end

  # POST /newsarticles
  # POST /newsarticles.json
  def create
    @newsarticle = Newsarticle.new(newsarticle_params)

    respond_to do |format|
      if @newsarticle.save
        format.html { redirect_to @newsarticle, notice: 'Newsarticle was successfully created.' }
        format.json { render :show, status: :created, location: @newsarticle }
      else
        format.html { render :new }
        format.json { render json: @newsarticle.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /newsarticles/1
  # PATCH/PUT /newsarticles/1.json
  def update
    respond_to do |format|
      if @newsarticle.update(newsarticle_params)
        format.html { redirect_to @newsarticle, notice: 'Newsarticle was successfully updated.' }
        format.json { render :show, status: :ok, location: @newsarticle }
      else
        format.html { render :edit }
        format.json { render json: @newsarticle.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /newsarticles/1
  # DELETE /newsarticles/1.json
  def destroy
    @newsarticle.destroy
    respond_to do |format|
      format.html { redirect_to newsarticles_url, notice: 'Newsarticle was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_newsarticle
      @newsarticle = Newsarticle.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def newsarticle_params
      params.require(:newsarticle).permit(:title, :content, :tag, :url, :launchdate, :website, :imgurl)
    end
end

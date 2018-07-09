require 'test_helper'

class NewsarticlesControllerTest < ActionDispatch::IntegrationTest
  setup do
    @newsarticle = newsarticles(:one)
  end

  test "should get index" do
    get newsarticles_url
    assert_response :success
  end

  test "should get new" do
    get new_newsarticle_url
    assert_response :success
  end

  test "should create newsarticle" do
    assert_difference('Newsarticle.count') do
      post newsarticles_url, params: { newsarticle: { content: @newsarticle.content, imgurl: @newsarticle.imgurl, launchdate: @newsarticle.launchdate, tag: @newsarticle.tag, title: @newsarticle.title, url: @newsarticle.url, website: @newsarticle.website } }
    end

    assert_redirected_to newsarticle_url(Newsarticle.last)
  end

  test "should show newsarticle" do
    get newsarticle_url(@newsarticle)
    assert_response :success
  end

  test "should get edit" do
    get edit_newsarticle_url(@newsarticle)
    assert_response :success
  end

  test "should update newsarticle" do
    patch newsarticle_url(@newsarticle), params: { newsarticle: { content: @newsarticle.content, imgurl: @newsarticle.imgurl, launchdate: @newsarticle.launchdate, tag: @newsarticle.tag, title: @newsarticle.title, url: @newsarticle.url, website: @newsarticle.website } }
    assert_redirected_to newsarticle_url(@newsarticle)
  end

  test "should destroy newsarticle" do
    assert_difference('Newsarticle.count', -1) do
      delete newsarticle_url(@newsarticle)
    end

    assert_redirected_to newsarticles_url
  end
end

import pytest
from selenium.webdriver.common.by import By
import time

# Test 1 to check if the homepage loads successfully
@pytest.mark.usefixtures("setup")
def test_homepage_loads(setup):
    driver = setup
    driver.get("http://127.0.0.1:5000")
    assert "iHeart music homepage" in driver.title

# Test 2 to check if the random artist button is displayed on the homepage
def test_random_artist_button(setup):
    driver = setup
    driver.get("http://127.0.0.1:5000")
    random_artist_button = driver.find_element(By.ID, "randomArtistButton")
    assert random_artist_button.is_displayed()

# Test 3 to check if the artist page loads successfully
def test_artist_page_loads(setup):
    driver = setup
    driver.get("http://127.0.0.1:5000/artist/12/")
    assert "Artist Page" in driver.title

# Test 4 to check if a review submission form is functional on the artist page
def test_review_submission(setup):
    driver = setup
    driver.get("http://127.0.0.1:5000/artist/12/")
    user_name_input = driver.find_element(By.NAME, "user_name")
    review_content_input = driver.find_element(By.NAME, "review_content")
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    user_name_input.send_keys("Test User")
    review_content_input.send_keys("This is a test review.")
    submit_button.click()
    time.sleep(2)  # Add delay to ensure page navigation
    assert "Artist Page" in driver.title

# Test 5 to check if the "Add Artist" page loads successfully
def test_add_artist_page_loads(setup):
    driver = setup
    driver.get("http://127.0.0.1:5000/add_artist")
    assert "add artist" in driver.title

# Test 6 to check if an artist can be successfully added
def test_add_artist_submission(setup):
    driver = setup
    driver.get("http://127.0.0.1:5000/add_artist")
    artist_name_input = driver.find_element(By.NAME, "Artist Name")
    genres_input = driver.find_element(By.NAME, "Genres")
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    artist_name_input.send_keys("Test Artist")
    genres_input.send_keys("Test Genre")
    submit_button.click()
    time.sleep(2)  # Add delay to ensure page navigation
    assert "iHeart music homepage" in driver.title

# Test 7 to check if the "Add Artist" button is displayed on the homepage
def test_add_artist_button_displayed(setup):
    driver = setup
    driver.get("http://127.0.0.1:5000")
    add_artist_button = driver.find_element(By.XPATH, "//a[@href='/add_artist']")
    assert add_artist_button.is_displayed()

# Test 8 to check if the artist page contains an image
def test_artist_page_contains_image(setup):
    driver = setup
    driver.get("http://127.0.0.1:5000/artist/12/")
    artist_image = driver.find_element(By.CSS_SELECTOR, ".artist-image_page img")
    assert artist_image.is_displayed()

# Test 9 to check if the homepage contains artist buttons
def test_homepage_contains_artist_buttons(setup):
    driver = setup
    driver.get("http://127.0.0.1:5000")
    artist_buttons = driver.find_elements(By.CLASS_NAME, "button")
    assert len(artist_buttons) > 0

# Test 10 to check if the review form is displayed on the artist page
def test_review_form_displayed(setup):
    driver = setup
    driver.get("http://127.0.0.1:5000/artist/12/")
    review_form = driver.find_element(By.CLASS_NAME, "review-form")
    assert review_form.is_displayed()

# Test 11 to check if the artist page contains details about the artist
def test_artist_page_contains_details(setup):
    driver = setup
    driver.get("http://127.0.0.1:5000/artist/12/")
    artist_details = driver.find_element(By.CLASS_NAME, "artist-details")
    assert artist_details.is_displayed()

# Test 12 to check if the artist page contains reviews
def test_artist_page_contains_reviews(setup):
    driver = setup
    driver.get("http://127.0.0.1:5000/artist/12/")
    reviews = driver.find_elements(By.CLASS_NAME, "review")
    assert len(reviews) > 0

# Test 13 to check if attempting to access an invalid artist page results in a redirect
def test_invalid_artist_page_redirects(setup):
    driver = setup
    driver.get("http://127.0.0.1:5000/artist/999/")  # Assuming artist with ID 999 doesn't exist
    assert "404 Not Found" in driver.title

# Test 14 to check if the user is redirected to the homepage after adding an artist
def test_add_artist_redirects_after_submission(setup):
    driver = setup
    driver.get("http://127.0.0.1:5000/add_artist")
    artist_name_input = driver.find_element(By.NAME, "Artist Name")
    genres_input = driver.find_element(By.NAME, "Genres")
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    artist_name_input.send_keys("Test Artist")
    genres_input.send_keys("Test Genre")
    submit_button.click()
    time.sleep(2)  # Add delay to ensure page navigation
    assert "iHeart music homepage" in driver.title

# Test 15 to check if clicking the random artist button navigates to an artist page
def test_random_artist_button_navigates(setup):
    driver = setup
    driver.get("http://127.0.0.1:5000")
    random_artist_button = driver.find_element(By.ID, "randomArtistButton")
    random_artist_button.click()
    time.sleep(2)  # Add delay to ensure page navigation
    assert "Artist Page" in driver.title

# Test 16 to check if clicking the "Add Artist" button navigates to the "Add Artist" page
def test_add_artist_button_navigates(setup):
    driver = setup
    driver.get("http://127.0.0.1:5000")
    add_artist_button = driver.find_element(By.XPATH, "//a[@href='/add_artist']")
    add_artist_button.click()
    assert "add artist" in driver.title

# Test 17 to check if the homepage contains a footer
def test_homepage_contains_footer(setup):
    driver = setup
    driver.get("http://127.0.0.1:5000")
    footer = driver.find_element(By.CSS_SELECTOR, "footer")
    assert footer.is_displayed()

# Test 18 to check if the artist page contains a footer
def test_artist_page_contains_footer(setup):
    driver = setup
    driver.get("http://127.0.0.1:5000/artist/12/")
    footer = driver.find_element(By.CSS_SELECTOR, "footer")
    assert footer.is_displayed()

# Test 19 to check if the "Add Artist" page contains a footer
def test_add_artist_page_contains_footer(setup):
    driver = setup
    driver.get("http://127.0.0.1:5000/add_artist")
    footer = driver.find_element(By.CSS_SELECTOR, "footer")
    assert footer.is_displayed()

# Test 20 to check if the homepage contains a header
def test_homepage_contains_header(setup):
    driver = setup
    driver.get("http://127.0.0.1:5000")
    header = driver.find_element(By.XPATH, "//h1[@class='center-heading big-heading']")
    assert header.is_displayed()

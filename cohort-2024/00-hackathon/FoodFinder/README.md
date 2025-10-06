=======
# README for FoodFinder App

## Introduction
Welcome to the FoodFinder App, a comprehensive solution designed to optimize your dining experiences. Whether you're squeezing a meal in between lectures or planning a budget-friendly dinner with friends, this app tailors your meal options to fit your specific scenarios and preferences. Our primary goal is to ensure you never miss a meal, no matter how tight your schedule or budget. The Meal Optimizer App leverages every possible moment of your available time, helping you enjoy quality meals within your budget constraints. With a focus on maximizing user satisfaction, we strive to present options that not only fit your criteria but also boast high ratings on Google.

## Scenarios & Features
- **Single-user sessions:** Tailored to fit the solo diner looking to maximize brief time windows.
- **Budget-conscious dining:** Offers solutions that ensure you stay within your financial limits without compromising on taste.
- **Preference-based filtering:** Whether it's a spicy kick or a low-calorie dish, find meals that cater exactly to your taste and dietary requirements.
- **Time Management:** The app assesses your free time, estimated waiting and travel times to restaurants, and aligns them with business hours to ensure you get served without rush.
- **Distance and Travel:** Utilize our dynamic radius search to find eateries within an optimal distance, estimated to ensure you spend more time dining and less time commuting.
- **Budget Adjustment:** Stay on top of your finances with tailored dining suggestions that keep you within a preset spending limit, allowing for both economical and occasional lavish dining choices.
- **Diverse Dining Types:** Whether you're in the mood for fast food, crave a fine dining experience, or just need to swing by a supermarket for a quick bite, our app sorts and prioritizes dining establishments based on your current needs.
- **Payment Flexibility:** Enjoy the convenience of filtering restaurants based on accepted payment methods, ensuring seamless transactions.

## Preference Customization
Powered by a sophisticated language model, the app allows you to set and adjust food preferences such as:
- **Spice Level:** From mild to fiery, indicate your tolerance and love for spice.
- **Allergy Information:** Input your dietary restrictions to avoid allergens.
- **Cuisine Style:** Choose from a vast array of culinary traditions, whether Eastern or Western.
- **Health Conscious Choices:** Filter for low-calorie and low-fat options to adhere to your health goals.
- **Vegetarian and Vegan Options:** Easily find plant-based and animal-free meals that delight.

## Usages
The data containing all the available restaruants (from Google Map) is stored in `all_places_response.json`. We use `vis.py` to vis it and use `get_pandas.py` to turn it to pandas dataframe.

To start the application, ensure you have Flask and the required dependencies installed, then run the following command from the terminal:
```bash
python app.py
```
Navigate to http://localhost:8080 to access the application. 

Before you start searching for restaurants, you need to upload an .ics file that describes your location and schedule. The events in your uploaded .ics file should include a description field containing a **link to Google Maps**, which specifies the exact location of your events (as shown in `example.ics`). This ensures that the app can accurately determine where you will be and at what time, allowing it to provide restaurant recommendations that are timely and conveniently located relative to your scheduled activities.

Then you can follow the on-screen instructions to input your dining preferences and any other necessary details.

### Step-by-Step Workflow

Below is a flowchart that outlines the process from entering your search criteria to selecting a restaurant:

![FoodFinder Workflow](./templates/Flow_chart.png)

#### Entering Search Criteria
1. **Time:** Specify the time you plan to eat.
2. **Location:** Enter your current location or the location where you wish to dine.
3. **Budget:** Set your budget for the meal.

#### Setting Preferences (Optional)
You can further refine your search by specifying:
- **Cuisine:** Choose the type of cuisine you prefer.
- **Allergies:** List any allergies to avoid specific ingredients.
- **Spicy:** Indicate if you prefer spicy food.

#### Filtering Results
The app filters the restaurant options based on the inputs:
- **Time:** Matches your available time with restaurant operating hours.
- **Distance:** Considers how far you are willing to travel.
- **Budget:** Filters options that fit within your budget.
- **Preference:** Ensures the options align with your cuisine and spice preferences.

#### Selection
Review the filtered list showing the distance, cost, type, and rating of each restaurant, and select the best option that meets your criteria.

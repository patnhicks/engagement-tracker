# -*- coding: utf-8 -*-
"""
Jul 14 2025

Author: Pat Hicks
Title:Social media engagement tracker
Summary: This Python script tracks social media engagement (likes and comments) across platforms,
calculates total engagement per platform, identifies the top platform,
and simulates engagement growth over time.
"""
#create the dictionary for engagement tracking numbers
engagement_data = {
    "Instagram": {"likes": 250, "comments": 60},
    "Facebook": {"likes": 200, "comments": 85},
    "Twitter": {"likes": 300, "comments": 75}
    }

#calcule total engagement
def calculate_total_engagement(engagement_data):
    platform_total = {}                                       #Start at 0
    for platform in engagement_data:  
        # Get number of like and comments from dictionary
        likes = engagement_data[platform]["likes"]      
        comments = engagement_data[platform]["comments"]
        
        #Get total by adding likes and comments to counter         
        total = likes + comments
        
        #Place platform total in new dict
        platform_total[platform] = total
        
    #Return the result of total platform engagement calculation    
    return platform_total    

#Identify top platform
def id_top_platform(platform_total):
    top_platform = None  
    top_engagement = 0
    #Loop through previous info in platforma and totals
    for platform, total in platform_total.items():
        #Check if looped platform is higher than current top platform
        if total > top_engagement:
          top_platform = platform  
          top_engagement = total
          
    return top_platform, top_engagement

platform_engagement = calculate_total_engagement((engagement_data))    

for platform, total in platform_engagement.items():
    print(f"Total engagement for {platform}: {total}")
    
#Need a way to compare total to current top engagement.
#Declare curretn top engaement
top_platform, top_engagement = id_top_platform(platform_engagement)
print(f"The top platform is {top_platform} with {top_engagement} engagements.")

#simulate growth over time: every hour, 5% per hour, over 3 hours
def simulate_growth(engagement_data, hours=3, growth_rate=0.05):
    hour = 0
    while hour < hours: 
        platform_total = {}
        for platform in engagement_data:
            # Get number of likes and comments from dictionary
            likes = engagement_data[platform]["likes"]      
            comments = engagement_data[platform]["comments"]
         
            # Growth formulae
            likes = likes * (1 + growth_rate)
            comments = comments * (1 + growth_rate) 
         
            #update the dictionary
            engagement_data[platform]["likes"] = likes
            engagement_data[platform]["comments"] = comments
            
            #total for platforms
            total = likes + comments
            platform_total[platform] = total

        #DIsplay the results
        print(f"\nUpdated total engagement after hour {hour + 1}: ")
        print(f"Instagram: {int(platform_total['Instagram'])}, ")
        print(f"Twitter: {int(platform_total['Twitter'])}, ")
        print(f"Facebook: {int(platform_total['Facebook'])} ")
        print()
        hour += 1

    print(f"\nSimulation complete.  Final totals per platform: ") 
    print(f"Instagram: {int(platform_total['Instagram'])}, ")
    print(f"Twitter: {int(platform_total['Twitter'])}, ")
    print(f"Facebook: {int(platform_total['Facebook'])} ")
    
 #Call the function
simulate_growth(engagement_data, hours=3, growth_rate=0.05)   
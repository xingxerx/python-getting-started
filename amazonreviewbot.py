import json

# Define the JSON structure
data = {
    "AmazonReviewBot": {
        "name": "AmazonReviewBot",
        "description": "Automates Amazon review scripts, FAQs, and unboxing content.",
        "functions": {
            "generate_review_script": {
                "input": ["product_name", "features", "price", "discount"],
                "output": "Structured video script with intro, demo, FAQs, and CTA."
            },
            "faq_responder": {
                "input": ["product_name", "common_questions"],
                "output": "Pre-written FAQ answers for Amazon and YouTube descriptions."
            },
            "pricing_tracker": {
                "input": ["product_url"],
                "output": "Real-time price tracking and discount notifications."
            }
        }
    },
    "PRMarketingBot": {
        "name": "PRMarketingBot",
        "description": "Handles PR, social media promotion, and press outreach.",
        "functions": {
            "create_social_media_post": {
                "input": ["product_name", "review_summary", "hashtags"],
                "output": "Engaging social media captions for Twitter, Instagram, and Facebook."
            },
            "generate_press_release": {
                "input": ["product_name", "features", "market_impact"],
                "output": "Formatted press release for distribution to media outlets."
            },
            "ad_campaign_optimizer": {
                "input": ["budget", "target_audience"],
                "output": "Optimized paid ad strategy for Amazon, YouTube, and Google Ads."
            }
        }
    },
    "CanvaMediaAssetBot": {
        "name": "CanvaMediaAssetBot",
        "description": "Creates media assets for product reviews and marketing.",
        "functions": {
            "generate_graphic_slide": {
                "input": ["product_name", "features"],
                "output": "Pre-designed Canva slide with branding and product highlights."
            },
            "transition_effect_suggester": {
                "input": ["video_style"],
                "output": "List of transition effects for video production."
            },
            "thumbnail_generator": {
                "input": ["product_name", "CTA"],
                "output": "High-quality YouTube thumbnail with bold text and visuals."
            }
        }
    },
    "Integration": {
        "AmazonReviewBot_to_PRMarketingBot": {
            "trigger": "Review Script Completion",
            "action": "Automatically generate and schedule social media posts."
        },
        "AmazonReviewBot_to_CanvaMediaAssetBot": {
            "trigger": "Review Script Finalized",
            "action": "Create branded media assets based on script elements."
        },
        "PRMarketingBot_to_CanvaMediaAssetBot": {
            "trigger": "New PR or Ad Campaign",
            "action": "Generate supporting visual assets for campaign."
        }
    }
}

# Save the JSON file
filename = "amazon_review_bot.json"
with open(filename, "w") as json_file:
    json.dump(data, json_file, indent=4)

print(f"JSON file '{filename}' has been created successfully!")
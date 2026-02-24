from google.ads.googleads.client import GoogleAdsClient
from create_promotion_asset import create_promotion_asset

def main():
    client = GoogleAdsClient.load_from_storage("google-ads.yaml")

    create_promotion_asset(
        client=client,
        customer_id="7296977492",
        promotion_target="Winter Sale",
        money_off_amount=10,     
        promo_code="WINTER10",
        start_date="20260108",
        end_date="20260228"
    )

if __name__ == "__main__":
    main()

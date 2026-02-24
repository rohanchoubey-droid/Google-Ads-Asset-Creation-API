from google.ads.googleads.client import GoogleAdsClient
from unlink_customer_asset import unlink_promotion_from_account
from create_promotion_asset import create_promotion_asset
from link_customer_asset import link_asset_to_customer

def update_promotion():
    customer_id = "7296977492"
    old_asset = "customers/7296977492/assets/321736082553"

    client = GoogleAdsClient.load_from_storage("google-ads.yaml")

    # 1. Unlink old
    unlink_promotion_from_account(customer_id, old_asset)

    # 2. Create new
    new_asset = create_promotion_asset(
        client=client,
        customer_id=customer_id,
        promotion_target="Benjamin Bala Sale",
        money_off_amount=15,          
        promo_code="Summer30",
        start_date="20260301",
        end_date="20260331"
    )

    # 3. Link new
    link_asset_to_customer(client, customer_id, new_asset)

if __name__ == "__main__":
    update_promotion()

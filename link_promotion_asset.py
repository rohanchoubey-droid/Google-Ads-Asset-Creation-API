from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException

def list_promotion_assets(customer_id):
    client = GoogleAdsClient.load_from_storage("google-ads.yaml")
    ga_service = client.get_service("GoogleAdsService")

    query = """
    SELECT
      asset.resource_name,
      asset.id,
      asset.type,
      asset.final_urls,
      asset.promotion_asset.promotion_target,
      asset.promotion_asset.promotion_code,
      asset.promotion_asset.percent_off,
      asset.promotion_asset.money_amount_off.amount_micros,
      asset.promotion_asset.money_amount_off.currency_code,
      asset.promotion_asset.start_date,
      asset.promotion_asset.end_date
    FROM asset
    WHERE asset.type = PROMOTION
    ORDER BY asset.id DESC
    """

    try:
        response = ga_service.search(
            customer_id=customer_id,
            query=query
        )

        found = False
        for row in response:
            found = True
            asset = row.asset
            promo = asset.promotion_asset

            print("=" * 60)
            print(f"Asset ID        : {asset.id}")
            print(f"Resource Name   : {asset.resource_name}")
            print(f"Final URLs      : {list(asset.final_urls)}")
            print(f"Target          : {promo.promotion_target}")
            print(f"Promo Code      : {promo.promotion_code}")

            if promo.percent_off:
                print(f"Percent Off     : {promo.percent_off}%")

            if promo.money_amount_off.amount_micros:
                print(
                    f"Money Off       : "
                    f"{promo.money_amount_off.amount_micros / 1_000_000} "
                    f"{promo.money_amount_off.currency_code}"
                )

            print(f"Start Date      : {promo.start_date}")
            print(f"End Date        : {promo.end_date}")

        if not found:
            print("No promotion assets found.")

    except GoogleAdsException as ex:
        print("Google Ads API error:")
        for error in ex.failure.errors:
            print(error.message)

if __name__ == "__main__":
    list_promotion_assets("7296977492")

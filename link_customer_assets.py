from google.ads.googleads.client import GoogleAdsClient

def link_asset_to_customer(client, customer_id, asset_resource_name):
    service = client.get_service("CustomerAssetService")
    operation = client.get_type("CustomerAssetOperation")

    customer_asset = operation.create

    customer_asset.asset = asset_resource_name
    customer_asset.field_type = client.enums.AssetFieldTypeEnum.PROMOTION

    service.mutate_customer_assets(
        customer_id=customer_id,
        operations=[operation]
    )

    print(f"Promotion linked at ACCOUNT level: {asset_resource_name}")

def main():
    client = GoogleAdsClient.load_from_storage("google-ads.yaml")
    customer_id = "7296977492"

    PROMOTION_ASSETS = [
        # "customers/7296977492/assets/321603889934",
        "customers/7296977492/assets/321736082553",
    ]

    for asset in PROMOTION_ASSETS:
        link_asset_to_customer(client, customer_id, asset)

if __name__ == "__main__":
    main()

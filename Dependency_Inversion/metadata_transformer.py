from typing import Dict, Optional, Any


class MetadataTransformer:

    @staticmethod
    def transform_user_preferences_to_metadata(
        user_preferences: Dict[str, Optional[Any]]
    ) -> tuple[Dict[str, Any], Dict[str, Any]]:

        product_metadata: Dict[str, Any] = {}
        sku_metadata: Dict[str, Any] = {}
        
        for key, value in user_preferences.items():
            if not value:
                continue
                
            if key == "publisher":
                product_metadata["publisher"] = value
            elif key == "billing_cycle":
                sku_metadata["billing_cycle"] = value
            elif key == "price":
                sku_metadata["price"] = value
            elif key == "want_trial":
                sku_metadata["trial_available"] = value
        
        return product_metadata, sku_metadata
    
    @staticmethod
    def build_query_from_preferences(user_preferences: Dict[str, Optional[Any]]) -> str:

        description = user_preferences.get('description', '')
        return f"Find a product matching: {description}"


from typing import Dict

class UsageTracker:
    def __init__(self):
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.total_tokens = 0
        self.api_call_count = 0
        self.cache_read_tokens = 0

    def add_usage(self, usage_metadata: dict):
        if not isinstance(usage_metadata, dict) or not usage_metadata:
            return

        self.api_call_count += 1

        for model, data in usage_metadata.items():
            if not isinstance(data, dict):
                continue

            input_tokens = data.get("input_tokens")
            output_tokens = data.get("output_tokens")
            total_tokens = data.get("total_tokens")

            if isinstance(input_tokens, int):
                self.total_input_tokens += input_tokens

            if isinstance(output_tokens, int):
                self.total_output_tokens += output_tokens

            if isinstance(total_tokens, int):
                self.total_tokens += total_tokens

            input_details = data.get("input_token_details")
            if isinstance(input_details, dict):
                cache_read = input_details.get("cache_read")
                if isinstance(cache_read, int):
                    self.cache_read_tokens += cache_read

    def get_metrics(self) -> Dict[str, int]:
        return {
            "total_input_tokens": self.total_input_tokens,
            "total_output_tokens": self.total_output_tokens,
            "total_tokens": self.total_tokens,
            "api_call_count": self.api_call_count,
            "cache_read_tokens": self.cache_read_tokens,
        }

    def reset(self):
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.total_tokens = 0
        self.api_call_count = 0
        self.cache_read_tokens = 0

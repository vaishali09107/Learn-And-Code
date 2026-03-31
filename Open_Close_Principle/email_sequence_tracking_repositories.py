"""Repository for email_sequence_tracking table operations.

This module handles all database operations related to email
sequence tracking, including paginated retrieval of tracking data.
"""
from typing import Dict, List, Tuple
from src.database.base_repository import BaseRepository
from src.database.validators import validate_pagination
from src.utils.logger import get_logger

logger = get_logger(__name__)

class EmailSequenceTrackingRepository(BaseRepository):
    """Repository for email_sequence_tracking table operations."""

    @staticmethod
    def get_email_tracking_paginated(
        page: int = 1,
        per_page: int = 25
    ) -> Tuple[List[Dict], int]:
        """Get email tracking data with pagination.
        
        Args:
            page: Page number (1-indexed)
            per_page: Number of items per page
            
        Returns:
            Tuple of (list of tracking dictionaries, total count)
        """
        page, per_page, offset = validate_pagination(page, per_page)

        try:
            count_query = "SELECT COUNT(*) FROM email_sequence_tracking"
            total_count = EmailSequenceTrackingRepository._execute_count(
                count_query, operation_name="count_email_tracking"
            )

            query = """
                SELECT est.id, est.lead_id, lt.email, lt.name,
                       est.initial_email_sent_time, est.email_step_number,
                       est.last_email_sent_time
                FROM email_sequence_tracking est
                LEFT JOIN lead_tracking lt ON est.lead_id = lt.lead_id
                ORDER BY est.last_email_sent_time DESC NULLS LAST
                LIMIT %s OFFSET %s
            """

            rows = EmailSequenceTrackingRepository._execute_query(
                query, (per_page, offset), "get_email_tracking_paginated"
            )

            results = [
                {
                    "id": row[0],
                    "lead_id": str(row[1]) if row[1] else None,
                    "email": row[2],
                    "name": row[3],
                    "initial_email_sent_time": row[4],
                    "email_step_number": row[5],
                    "last_email_sent_time": row[6]
                }
                for row in rows
            ]

            return results, total_count

        except Exception as e:
            logger.exception(f"Error getting email tracking: {e}")
            return [], 0


# OCP Extension Example:
# The following methods can be added to extend repository behavior
# without modifying existing functionality.
# This keeps the repository closed for modification but open for extension.
# def get_tracking_by_lead_id(self, lead_id: str):
#     """Extension method to fetch tracking by lead_id (OCP compliant)."""
#     pass

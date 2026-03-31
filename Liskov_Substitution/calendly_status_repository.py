"""Repository for calendly_status table operations.

This module handles all database operations related to Calendly
status tracking, including invite status and booking URLs.
"""
from typing import Dict, List, Tuple
from src.database.base_repository import BaseRepository
from src.database.validators import validate_pagination
from src.utils.logger import get_logger

logger = get_logger(__name__)

class CalendlyStatusRepository(BaseRepository):
    """Repository for calendly_status table operations."""

    @staticmethod
    def get_all_calendly_status() -> List[Dict]:
        """Get all calendly status records.
        
        Returns:
            List of calendly status dictionaries
        """
        query = """
            SELECT cs.id, cs.lead_id, lt.email, lt.name,
                   cs.invite_sent, cs.invite_sent_at, cs.booking_url
            FROM calendly_status cs
            LEFT JOIN lead_tracking lt ON cs.lead_id = lt.lead_id
            ORDER BY cs.invite_sent_at DESC NULLS LAST
        """

        try:
            rows = CalendlyStatusRepository._execute_query(
                query, operation_name="get_all_calendly_status"
            )

            return [
                {
                    "id": row[0],
                    "lead_id": str(row[1]) if row[1] else None,
                    "email": row[2],
                    "name": row[3],
                    "invite_sent": row[4],
                    "invite_sent_at": row[5],
                    "booking_url": row[6]
                }
                for row in rows
            ]

        except Exception as e:
            logger.exception(f"Error getting calendly status: {e}")
            return []

    @staticmethod
    def get_calendly_status_paginated(
        page: int = 1,
        per_page: int = 25
    ) -> Tuple[List[Dict], int]:
        """Get calendly status records with pagination.
        
        Args:
            page: Page number (1-indexed)
            per_page: Number of items per page
            
        Returns:
            Tuple of (list of calendly status dictionaries, total count)
        """
        page, per_page, offset = validate_pagination(page, per_page)

        try:
            count_query = "SELECT COUNT(*) FROM calendly_status"
            total_count = CalendlyStatusRepository._execute_count(
                count_query, operation_name="count_calendly_status"
            )

            query = """
                SELECT cs.id, cs.lead_id, lt.email, lt.name,
                       cs.invite_sent, cs.invite_sent_at, cs.booking_url
                FROM calendly_status cs
                LEFT JOIN lead_tracking lt ON cs.lead_id = lt.lead_id
                ORDER BY cs.invite_sent_at DESC NULLS LAST
                LIMIT %s OFFSET %s
            """

            rows = CalendlyStatusRepository._execute_query(
                query, (per_page, offset), "get_calendly_status_paginated"
            )

            results = [
                {
                    "id": row[0],
                    "lead_id": str(row[1]) if row[1] else None,
                    "email": row[2],
                    "name": row[3],
                    "invite_sent": row[4],
                    "invite_sent_at": row[5],
                    "booking_url": row[6]
                }
                for row in rows
            ]

            return results, total_count

        except Exception as e:
            logger.exception(f"Error getting calendly status paginated: {e}")
            return [], 0

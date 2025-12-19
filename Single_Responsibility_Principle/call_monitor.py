# """
# Call monitoring service - polls call_sessions table to track call status.
# """
# import logging
# import asyncio
# from datetime import datetime
# from typing import Callable
# # from src.database.repositories import CallSessionsRepository
# # from src.config.settings import get_config
# # from src.utils.logger import get_logger

# # logger = get_logger(__name__)


# class CallMonitor:
#     """
#     Service to monitor call status by polling call_sessions database.
    
#     Polls the database every N seconds (configured via CALL_STATUS_POLL_INTERVAL_SECONDS,
#     default 10 seconds, recommended 15 seconds) until call reaches terminal status.
#     """
    
#     def __init__(self):
#         # self.config = get_config()
#         self.poll_interval = self.config.call_status_poll_interval 
#         self.call_timeout = self.config.call_timeout_seconds
    
#     async def monitor_call(self, call_sid: str, status_callback: Callable[[str], None]) -> str:
#         """
#         Monitor a call until it reaches terminal status.
        
#         Args:
#             call_sid: Twilio call identifier
#             status_callback: Callback function(status) to update status
            
#         Returns:
#             Final call status
#         """
#         start_time = datetime.utcnow()
#         last_status = None
        
#         while True:
#             try:
#                 # Get call status from call_sessions table
#                 # call_info = CallSessionsRepository.get_call_status(call_sid)
                
#                 if not call_info:
#                     logger.warning(f"Call {call_sid} not found in call_sessions table")
#                     # Wait a bit and check again
#                     await asyncio.sleep(self.poll_interval)
#                     continue
                
#                 status = call_info['status'].lower()
                
#                 # Update if status changed
#                 if status != last_status:
#                     logger.info(f"Call {call_sid} status: {status}")
#                     last_status = status
#                     status_callback(status)
                
#                 # Check if call reached terminal state
#                 terminal_states = ['completed', 'failed', 'busy', 'no-answer', 'canceled']
#                 if status in terminal_states:
#                     duration = call_info.get('duration_seconds')
#                     logger.info(f"Call {call_sid} completed with status: {status} (duration: {duration}s)")
#                     return status
                
#                 # Check timeout
#                 elapsed = (datetime.utcnow() - start_time).total_seconds()
#                 if elapsed > self.call_timeout:
#                     logger.warning(f"Call {call_sid} timed out after {elapsed}s")
#                     status_callback('failed')
#                     return 'failed'
                
#                 # Wait before next poll
#                 await asyncio.sleep(self.poll_interval)
                
#             except Exception as e:
#                 logger.exception(f"Error monitoring call {call_sid}: {e}")
#                 await asyncio.sleep(self.poll_interval)
                
# # Global instance
# call_monitor = CallMonitor()
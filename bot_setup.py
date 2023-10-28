async def create_active_client():
    import setup_helpers.clients.standard_client.client as client
    active_client = client.Client()
    return active_client

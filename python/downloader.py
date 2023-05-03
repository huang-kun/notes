
import aiohttp
import asyncio
import os

__author__ = 'ChatGPT'


async def aio_download_url(session, url, directory, timeout=None):
    """
    Downloads a single file from the given URL using the given aiohttp.ClientSession.

    Args:
        session (aiohttp.ClientSession): The session to use for the download.
        url (str): The URL to download from.
        directory (str): The directory to save the downloaded file to.

    Returns:
        None
    """
    # Extract the filename from the URL.
    filename = os.path.basename(url)
    # Join the directory and filename to get the full path to the file.
    filepath = os.path.join(directory, filename)
    try:
        # Use the session to download the file.
        async with session.get(url, timeout=timeout) as response:
            # Open a file for writing the downloaded data.
            with open(filepath, 'wb') as f:
                # Read the file in chunks until the end is reached.
                while True:
                    chunk = await response.content.read(1024*1024)
                    if not chunk:
                        break
                    # Write the chunk to the file.
                    f.write(chunk)
        # Print a message indicating that the download is complete.
        print(f"Downloaded {url}")
    except asyncio.TimeoutError:
        print(f"Timed out while downloading {url}")
    except Exception as err:
        print(f"Error: {err}")


async def aio_download_urls(urls, directory, batch_size, timeout=None):
    """
    Downloads a list of files from the given URLs using aiohttp and asyncio.

    Args:
        urls (List[str]): The URLs to download from.
        directory (str): The directory to save the downloaded files to.
        batch_size (int): The maximum number of downloads to perform in parallel.

    Returns:
        None
    """
    # Calculate the connection limit based on the batch size.
    conn_limit = min(len(urls), batch_size)
    # Create a connector with connection pooling and the calculated limit.
    connector = aiohttp.TCPConnector(limit=conn_limit)
    # Create a session to use for all the downloads.
    async with aiohttp.ClientSession(connector=connector) as session:
        # Iterate over the URLs in batches of size batch_size.
        for i in range(0, len(urls), batch_size):
            batch_urls = urls[i:i+batch_size]
            # Create a list of tasks, one for each download in the current batch.
            tasks = [asyncio.ensure_future(aio_download_url(session, url, directory, timeout)) for url in batch_urls]
            # Run all the tasks in parallel.
            await asyncio.gather(*tasks)


def download_urls(urls, to_directory, batch_size=None, timeout=None):
    """
    Downloads a list of files from the given URLs using aiohttp and asyncio.

    Args:
        urls (List[str]): The URLs to download from.
        to_directory (str): The directory to save the downloaded files to.
        batch_size (int): The maximum number of downloads to perform in parallel.

    Returns:
        None
    """
    url_count = len(urls)
    if url_count == 0:
        return
    if batch_size is None or batch_size > url_count:
        batch_size = url_count
    # Create the directory if it doesn't exist.
    if not os.path.exists(to_directory):
        os.makedirs(to_directory)
    # Run the download function using asyncio.
    asyncio.run(aio_download_urls(urls, to_directory, batch_size, timeout))
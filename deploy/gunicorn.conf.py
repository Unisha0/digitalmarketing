import multiprocessing

bind = "unix:/run/gunicorn-trendcrafters/gunicorn.sock"
workers = max(2, min(multiprocessing.cpu_count() * 2 + 1, 3))  # t3.micro has ~1 GB RAM
timeout = 30
graceful_timeout = 30
keepalive = 5
max_requests = 1000
max_requests_jitter = 100
accesslog = "-"
errorlog = "-"

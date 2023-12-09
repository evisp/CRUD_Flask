UPDATE film
SET image_url = "https://fastly.picsum.photos/id/195/768/1024.jpg?hmac=rksrWrgeGQzOdzXlnzsTWy2L2zYq4gQei3TBMWCmXsI"
WHERE film_id % 10 = 9;
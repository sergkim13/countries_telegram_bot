get_rate_cases = [('USD',), ('USD', 'AUD'), ('USqqD',), ('USD', 'AUqqD'), ('', ), (123, ), (0.5, ), ('-',)]
get_fixed_request_name_cases = [
    ('Рос<fix>с</fix>ия', 'Россия'),
    ('М<fix>о</fix>скв<fix>а</fix>', 'Москва'),
    ('Нь<fix>ю</fix>-Йорк', 'Нью-Йорк'),
    ('<fix>В</fix>елик<fix>о</fix>британия', 'Великобритания'),
    ('Санкт-Петербур<fix>г</fix>', 'Санкт-Петербург'),
]

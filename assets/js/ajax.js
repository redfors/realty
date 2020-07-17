$(function () {

    $('.ajax').on('click', function () {
        realization = $('.realization .current').val();
        place = $('.place option').val();
        realty = $('.realty option').val();
        area = $('.area option').val();
        rooms = $('.rooms option').val();
        price = $('.price option:selected ').attr('data');

        data = {
            'realization': realization,
            'place': place,
            'realty': realty,
            'area': area,
            'rooms': rooms,
            'price': price
        }
        console.log(555);
        console.log(data);

        $.ajax({
            url: '/search/',
            method: 'GET',
            data: data,
            success: function () {

                console.log("Ajax is Working!!!")
            },
            error: function () {
                console.log('Error');
            }
        });
    });
});
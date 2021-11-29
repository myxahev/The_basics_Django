window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {
        var t_href = event.target;
        console.log(t_href.name); // basket.id
        console.log(t_href.value); // basket.quantity

        $.ajax({
            url: '/baskets/edit/' + t_href.name + '/' + t_href.value + '/',
            success: function (data) {
                $('.basket_list').html(data.result);
            },
        })
    });

    // $('.product_list').on('click', 'a[type="add_item"]', function () {
    //     var t_href = event.target;
    //     console.log(t_href.href);
    //     console.log('ДО ЗАПРОСА');
    //
    //     $.ajax({
    //         url: t_href.href,
    //         success: function (data) {
    //             $('.product_list').html(data.result);
    //             console.log('после ЗАПРОСА');
    //         },
    //     })
    //     });
}
$(document).ready(function() {
    // تابعی برای افزودن محصول به سبد خرید
    function addToCart(productName, ingredients, price) {
        var newRow = $('<tr>');
        newRow.append('<td>' + productName + '</td>');
        newRow.append('<td>' + ingredients + '</td>');
        newRow.append('<td>1</td>'); // تعداد محصولات به صورت پیش‌فرض ۱ است
        newRow.append('<td>' + price + '</td>');
        newRow.append('<td>' + price + '</td>'); // قیمت کل نیز برابر با قیمت واحد است
        $('#cart-items').append(newRow);
    }

    // فرضیه: تابعی برای بررسی موجودی انبار و اضافه کردن محصول به سبد خرید
    function checkInventoryAndAddToCart(productName, ingredients, price) {
        // بررسی موجودی انبار و اضافه کردن محصول به سبد خرید
        // اگر موجودی کافی بود، با استفاده از تابع addToCart محصول به سبد خرید اضافه می‌شود
        // در غیر این صورت، نمایش پیام خطا به کاربر
        addToCart(productName, ingredients, price);
    }

    // رویداد زمانی که کاربر دکمه اضافه کردن به سبد خرید را فشار می‌دهد
    $('#add-to-cart-btn').click(function() {
        var productName = $('#product-name').val();
        var ingredients = $('#ingredients').val();
        var price = $('#price').val();

        checkInventoryAndAddToCart(productName, ingredients, price);
        Swal.fire({
            icon: 'success',
            title: 'محصول با موفقیت به سبد خرید اضافه شد',
            showConfirmButton: false,
            timer: 1500
        });
    });

    // رویداد زمانی که کاربر دکمه انتقال به صفحه پرداخت را فشار می‌دهد
    $('#checkout-btn').click(function() {
        // ذخیره اطلاعات سفارش در پایگاه داده
        Swal.fire({
            icon: 'success',
            title: 'سفارش با موفقیت ثبت شد',
            showConfirmButton: false,
            timer: 1500
        });
    });
});

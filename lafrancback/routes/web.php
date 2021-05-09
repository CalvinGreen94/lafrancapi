<?php
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\UploadImageController;
use App\Http\Controllers\ImageGalleryController;
use App\Http\Controllers\hardDropZoneFileUploadController;
// use App\Http\Controllers\ImageGalleryController;
use App\Http\Controllers\ImageUploadController;

// use App\Http\Controllers\UploadImageController;
Route::get('image-gallery', [ImageGalleryController::class,'index']);

Route::post('image-gallery', [ImageGalleryController::class,'upload']);

Route::delete('image-gallery/{id}', [ImageGalleryController::class,'destroy']);
// Route::get('upload-image', [UploadImageController::class, 'index']);
// Route::post('save', [UploadImageController::class, 'save']);
  
  
Route::get('image-upload', [ ImageUploadController::class, 'imageUpload' ])->name('image.upload');
Route::post('image-upload', [ ImageUploadController::class, 'imageUploadPost' ])->name('image.upload.post');
Route::post('store-multiple-image','ImageController@store');
Route::get('/sakujoooCloud', function () {
    return view('/sakujoooCloud');
});
// Route::get('/sakujo_adult', function () {
//     return view('/sakujo_adult');
// });
Route::get('/sakujooonsfw', function () {
    return view('sakujooonsfw');
}); //->middleware('auth')

Route::get('sakujo_dashboard',  function () {
    return redirect('http://127.0.0.1:3000/uploads/add');
});
Route::get('/sakujo_dashboard',[DropZoneFileUploadController::class,'index']);
Route::get('/sakujo_adult', [hardDropZoneFileUploadController::class,'index']);
Route::get('/welcome', function () {
    return view('/welcome');
});
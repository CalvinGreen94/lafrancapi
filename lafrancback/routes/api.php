<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\AuthController;
use App\Http\Controllers\DropZoneFileUploadController; 
use App\Http\Controllers\hardDropZoneFileUploadController;
use App\Http\Controllers\ImageGalleryController;
use App\Http\Controllers\UploadImageController;
Route::get('image-gallery', [ImageGalleryController::class,'index']);

Route::post('image-gallery', [ImageGalleryController::class,'upload']);

Route::delete('image-gallery/{id}', [ImageGalleryController::class,'destroy']);
// Route::get('upload-image', [UploadImageController::class, 'index']);
// Route::post('save', [UploadImageController::class, 'save']);
Route::get('image-upload', 'ImageUploadController@imageUpload')->name('image.upload');

Route::post('image-upload', 'ImageUploadController@imageUploadPost')->name('image.upload.post');
Route::post('register', [AuthController::class, 'register']);
Route::post('logout', [AuthController::class, 'logout']);
Route::post('login', [AuthController::class, 'login']);
Route::get('user', [AuthController::class, 'user']);
// Route::post('uploadimage', 'UploadController@image');

// Route::get('index2', [DropZoneFileUploadController::class,'index']);
Route::get('index', [hardDropZoneFileUploadController::class,'index']);

Route::get('/sakujoooCloud', function () {
      return view('/sakujoooCloud');
  });
Route::get('/sakujooonsfw', function () {
      return view('sakujooonsfw');
  });
  // ->middleware('auth')
// Route::get('/welcome', function () {
//     return view('/welcome');
// });
Route::get('/sakujo_dashboard',[DropZoneFileUploadController::class,'index']);
Route::get('/sakujo_adult', [hardDropZoneFileUploadController::class,'index']);
// Route::post('store', [ImageController::class,'store']);
Route::post('store', 'hardDropzoneFileUploadController@uploadImages');

// Route::post('delete', 'DropzoneFileUploadController@deleteImage');
Route::post('delete', 'hardDropzoneFileUploadController@deleteImage')->middleware('auth');

 
// Route::post('uploadImages', ['DropzoneFileUploadController'],'uploadImages');
// Route::post('uploadImages', ['hardDropzoneFileUploadController'],'uploadImages')->middleware('auth');


// Route::post('delete', ['DropzoneFileUploadController'],'deleteImage')->middleware('auth');
// Route::post('delete', ['hardDropzoneFileUploadController'],'deleteImage')->middleware('auth');

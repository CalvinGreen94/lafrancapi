<?php
namespace App\Http\Controllers;
use Illuminate\Http\Request;
use App\ImageUpload;
class hardDropzoneFileUploadController extends Controller
{
    public function index() {
        return view('/sakujo_adult');
    }

// ------------------------ [ Upload Image ] --------------------------

    public function uploadImages(Request $request) {
        $image = $request->file('file');
        $imageName = $image->getClientOriginalName(); //.'.'.$image->extension()
        $image->move(public_path('images/shit/'),$imageName);
        $data  =   ImageUpload::create(['image_name' => $imageName]);
        return response()->json(["status" => "success", "data" => $data]);
    }

// --------------------- [ Delete image ] -----------------------------

    /*
    * Delete images
    *
    * @param Request $request
    *
    * @retun string
    */
    public function deleteImage(Request $request) {
        $image = $request->file('filename');
        $filename =  $request->get('filename').'.jpeg,.jpg,.png,.gif,.mov';
        ImageUpload::where('image_name', $filename)->delete();
        $path = public_path().'images/shit/'.$filename;
        if (file_exists($path)) {
            unlink($path);
        }
        return $filename;
    }
}

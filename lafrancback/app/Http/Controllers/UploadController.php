<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class UploadController extends Controller
{
    public function image(Request $request)
    {
        $request->validate([
            'files'   => ['required', 'array'],
            'files.*' => ['required', 'image','min:5','max:5000']
        ]);

        $uploadedFiles = [];

        foreach ($request->file('files') as $file) {
            $fileName = bcrypt(microtime()) . "." . $file->getClientOriginalExtension();
            $file->move(public_path('/images/'),$fileName);
            array_push($uploadedFiles, "sakujoooCloud");
        }

        return response($uploadedFiles);
    }
}
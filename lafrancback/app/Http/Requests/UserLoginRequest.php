<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;

class UserLoginRequest extends FormRequest
{
    
    public function authorize()
    {
        return true;
    }

    public function rules()
    {
        return  [
            // 'email' => 'required',
            'name' => 'required',
            'password' => 'required|min:6',

    ];
    }
}

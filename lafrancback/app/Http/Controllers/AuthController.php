<?php
namespace App\Http\Controllers;
use App\Http\Requests\UserRegisterRequest;

use App\Http\Requests\UserLoginRequest;
use App\User;
use App\Http\Resources\User as UserResource;
// use GuzzleHttp\Psr7\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Http\Request;

class AuthController extends Controller
{
    public function register(UserRegisterRequest $request)
    {

        $user = User::create([
            // 'email' => $request->email,
            'name' => $request->name,
            'password' => bcrypt($request->password),

        ]);
        if (!$token = Auth::attempt($request->only(['name', 'password']))) {
            return abort(401);
        };

        return (new UserResource($request->user()))->additional(
            [
                'meta' => [
                    'token' => $token,
                ],
            ]
        );
    }


    public function login(UserLoginRequest $request)
    {
        if (!$token = Auth::attempt($request->only(['name', 'password']))) {
            return  response()->json([
                'errors' => [
                    'name' => ['Not found in system'],
                ]
            ], 422);
        };
        return (new UserResource($request->user()))->additional(
            [
                'meta' => [
                    'token' => $token,
                ]
            ]);
    }
    public function user(Request $request)
    {
        return new UserResource(
            $request->user());
    }
    public function logout()
    {
        Auth::logout();
    }
}

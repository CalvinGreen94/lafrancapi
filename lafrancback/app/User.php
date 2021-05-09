<?php

namespace App;
use Illuminate\Support\Facades\Route;
use Tymon\JWTAuth\Contracts\JWTSubject;

use App\Http\Controllers\AuthController;

use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;

class User extends Authenticatable implements JWTSubject
{
    use Notifiable;

    
    protected $fillable = [
        'name',
        // 'email',
        'password',
    ];
    protected $hidden = [
        'password',
        'remember_token',
    ];


    // public function ownsTopic(Topic $topic){
    //     return $this->id ===$topic->user->id;
    // }

    // protected $casts = [
    //     'email_verified_at' => 'datetime',
    // ];

    public function getJWTIdentifier()
    {
        return $this->getKey();
    }


    public function getJWTCustomClaims()
    {
        return [];
    }
}

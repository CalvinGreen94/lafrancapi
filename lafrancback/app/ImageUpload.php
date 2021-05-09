<?php

namespace App;
// use App\Traits\Orderable; 

use Illuminate\Database\Eloquent\Model;

class ImageUpload extends Model
{
    // use Orderable; 
    // protected $fillable = ['title'];
    //     public function user()
    // {
    //     return $this->belongsTo(Address::class);
    // }

    // public function topic()
    // {
    //     return $this->belongsTo(Topic::class);
    // }
    public function image()
    {
        return $this->belongsTo(ImageUpload::class);
    }

}

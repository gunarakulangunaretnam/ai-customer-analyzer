<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class PageController extends Controller
{
    public function ViewIndexPageFunction(){

        return view('index'); 

    }

    public function ViewHomePageFunction(){

        return view('home-page'); 
        
    }
}
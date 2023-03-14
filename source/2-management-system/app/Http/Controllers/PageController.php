<?php

namespace App\Http\Controllers;
use Illuminate\Support\Facades\Session;

use Illuminate\Http\Request;

class PageController extends Controller
{
    public function ViewIndexPageFunction(){

        return view('index'); 

    }

    public function ViewHomePageFunction(){
        
        $login_access_session = Session::get('LoginAccess');

        if($login_access_session == '[TRUE]'){

            return view('home-page',['PageName' => 'Home Page']); 
            
        }else{

            return redirect()->route('IndexPageLink');
            
        }
        
    }


    public function ViewVisionDataFunction(){
        
        $login_access_session = Session::get('LoginAccess');

        if($login_access_session == '[TRUE]'){

            return view('vision-data',['PageName' => 'Vision Data']); 
            
        }else{

            return redirect()->route('IndexPageLink');
            
        }
        
    }
}
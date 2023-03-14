<?php

namespace App\Http\Controllers;


use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Session;
use Illuminate\Support\Facades\Redirect;


class CurdController extends Controller
{

    public function SettingsChangeVoiceFunction(){

        $login_access_session = Session::get('LoginAccess');

        if($login_access_session == '[TRUE]'){

            //return view('home-page',['PageName' => 'Home Page']); 
            
        }else{

            return abort(404);
            
        }
        
        
    }
    
}
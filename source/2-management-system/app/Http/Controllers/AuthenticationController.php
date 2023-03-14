<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class AuthenticationController extends Controller
{
    public function LoginFunction(Request $request){

        $this->validate($request, [
            'username' => 'required',
            'password' => 'required',
        ]);


        $user_entered_username =  $request->username;
        $user_entered_password =  $request->password;

        $username_from_db = "";
        $password_from_db = "";

       
        $user = DB::select('SELECT username, password FROM user');

        foreach($user as $u){

            $username_from_db = $u->username;
            $password_from_db = $u->password;

        }

        echo $username_from_db;
        echo $password_from_db;

         /*
        if($user_entered_username == $username_from_db && Hash::check($user_entered_password, $password_from_db)){

            Session::put('Session_Type', 'Admin');
            Session::put('Session_Value', $username_from_db);

            $session_type = Session::get('Session_Type');
            $session_value = Session::get('Session_Value');


            if($session_type == 'Admin'){

                return Redirect::to("/view_dashboard_home");
            }


        }else{

            return Redirect::to("/")->withErrors(['The username or password is incorrect']);
        }

        */

    }
}
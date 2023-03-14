<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Session;
use Illuminate\Support\Facades\Redirect;

class CurdController extends Controller
{

    public function SettingsChangeVoiceFunction(Request $request)
    {
        $login_access_session = Session::get('LoginAccess');
    
        if ($login_access_session == '[TRUE]') {
            $this->validate($request, [
                'language' => 'required',
            ]);
    
            $selected_language = ucfirst($request->language);
    
            DB::table('setting')
                ->where('_key', 'voice_lang')
                ->update(['_value' => $selected_language]);
    
            // Redirect back to the previous page with a success message
            return redirect()->back()->with('success', 'Language updated successfully.');
        } else {
            return abort(404);
        }
    }
    
}
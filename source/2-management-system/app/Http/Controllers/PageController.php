<?php

namespace App\Http\Controllers;


use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Session;


class PageController extends Controller
{
    public function ViewIndexPageFunction(){

        return view('index'); 

    }

    public function ViewHomePageFunction(string $search_by_month){
        
        $login_access_session = Session::get('LoginAccess');

        if($login_access_session == '[TRUE]'){

            if($search_by_month == '[FALSE]'){

                $current_date = $current_year = date('Y')."-".$current_month = date('m')."-".$current_month = date('d');
                $current_month_customer_traffic_data = DB::select("SELECT DAY(date) AS day, COUNT(*) AS count FROM vision_data WHERE MONTH(date) = MONTH('$current_date') GROUP BY DAY(date) ORDER BY day ASC;");

                return view('home-page',['PageName' => 'Home Page', "YearMonth" => date('Y')."-".date('m'), 'TrafficData' => $current_month_customer_traffic_data]); 
       
            }

            
            
        }else{

            return redirect()->route('IndexPageLink');
            
        }
        
    }


    public function ViewVisionDataFunction(string $search_by_date){
        
        $login_access_session = Session::get('LoginAccess');

        if($login_access_session == '[TRUE]'){

            if($search_by_date == '[FALSE]'){

                $whole_vision_data = DB::select('SELECT * FROM vision_data');
                return view('vision-data',['PageName' => 'Vision Data',"type_of_search" => "[WHOLE_SEARCH]", "vision_data"=>$whole_vision_data]); 

            }else{

                $date_wise_vision_data = DB::select("SELECT * FROM vision_data where date = '$search_by_date'");
                return view('vision-data',['PageName' => 'Vision Data',"type_of_search" => "[DATE_WISE_SEARCH]", "vision_data"=>$date_wise_vision_data]); 
                
            }
            
        }else{

            return redirect()->route('IndexPageLink');
            
        }
        
    }

    public function ViewAudioDataFunction(string $search_by_date){
        
        $login_access_session = Session::get('LoginAccess');

        if($login_access_session == '[TRUE]'){

            if($search_by_date == '[FALSE]'){

                $whole_vision_data = DB::select('SELECT * FROM audio_data');
                return view('audio-data',['PageName' => 'Audio Data',"type_of_search" => "[WHOLE_SEARCH]", "audio_data"=>$whole_vision_data]); 

            }else{

                $date_wise_vision_data = DB::select("SELECT * FROM audio_data where date = '$search_by_date'");
                return view('audio-data',['PageName' => 'Audio Data',"type_of_search" => "[DATE_WISE_SEARCH]", "audio_data"=>$date_wise_vision_data]); 
                
            }
            
        }else{

            return redirect()->route('IndexPageLink');
            
        }
        
    }

    public function ViewSettingsFunction(){
        
        $login_access_session = Session::get('LoginAccess');

        if($login_access_session == '[TRUE]'){

            $current_language = DB::table('setting')->where('_key', 'voice_lang')->value('_value');


            return view('settings', [
                'PageName' => 'Settings',
                'CurrentLanguage' => $current_language
            ]);
            
        }else{

            return redirect()->route('IndexPageLink');
            
        }
        
    }
}
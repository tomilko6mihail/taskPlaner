<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;

class TaskController extends Controller
{
    public function sendTasks(){
        return [
            [
                'id' => 1, 
                'title' => 'do something'
            ],
            [
                'id' => 2, 
                'title' => 'do something'
            ],
            [
                'id' => 3, 
                'title' => 'do something'
            ],
            [
                'id' => 4, 
                'title' => 'do something'
            ],
        ];
    }
    public function id($id){
        return $id;
    }
}

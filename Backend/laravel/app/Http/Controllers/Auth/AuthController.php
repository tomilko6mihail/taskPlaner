<?php

namespace App\Http\Controllers\Auth;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Models\User;
use Illuminate\Support\Facades\DB;

class AuthController extends Controller
{
    public function login(Request $request)
    {
        // Test database connection
        DB::connection()->getPdo();
        $user = new User();
        $user->email = $request->email;
        $user->password = $request->password;
        $user->save();

        return 'ok';
    }
}

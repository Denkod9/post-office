import React, { useState } from 'react';
import { Navigate, useParams } from 'react-router-dom';
import { connect } from 'react-redux';
import { verify } from '../../actions/Authentication/auth';


const Activate = ({ verify }) => {
    const [verified, setVerified] = useState(false);
    const uid = useParams().uid;
    const token = useParams().token;

    const verify_account = e => {


        verify(uid, token);
        setVerified(true);
    };


    if (verified) {
        return <Navigate replace to='/' />
    }

    return (
        <div className='container'>
            <div
                className='d-flex flex-column justify-content-center align-items-center'
                style={{ marginTop: '200px' }}
            >
                <h1>Подтвердите ваш аккаунт:</h1>
                <button
                    onClick={verify_account}
                    style={{ marginTop: '50px' }}
                    type='button'
                    className='btn btn-primary'
                >
                    Подтвердить
                </button>
            </div>
        </div>
    );
};

export default connect(null, { verify })(Activate);
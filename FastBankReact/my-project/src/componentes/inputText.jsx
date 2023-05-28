import React, {Component} from "react";

const InputV = ({placeholder, onChange, type}) => {
    return (
        <div >
            <input type={type != undefined?type:'text'} onChange={onChange}  placeholder={placeholder} className=" m-3  w-4/4  border-b border-white text-slate-800 bg-[#0C633D] outline-none" />
        </div>
    )
}
export default InputV;
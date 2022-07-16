/* ================================================================
 * ecmascript6 by xdf(xudafeng[at]126.com)
 *
 * first created at : Fri Aug 08 2014 17:01:53 GMT+0800 (CST)
 *
 * ================================================================
 * Copyright 2014 xdf
 *
 * Licensed under the MIT License
 * You may not use this file except in compliance with the License.
 *
 * ================================================================ */

'use strict';

var detector = function() {
  try {
    return eval('(function () { const a = 1; return typeof a === "number"; }())');
  } catch (e) {
    return false;
  }
}

module.exports = detector();

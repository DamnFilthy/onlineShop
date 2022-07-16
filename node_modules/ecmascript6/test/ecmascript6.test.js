/* ================================================================
 * ecmascript6 by xdf(xudafeng[at]126.com)
 *
 * first created at : Fri Aug 08 2014 17:01:53 GMT+0800 (CST)
 *
 * ================================================================
 * Copyright 2013 xdf
 *
 * Licensed under the MIT License
 * You may not use this file except in compliance with the License.
 *
 * ================================================================ */

'use strict';

var ecmascript6 = require('..');

describe('/lib/ecmascript6.js', function() {
  describe('main', function() {
    it('should be a boolean', function() {
      ecmascript6.should.be.Boolean;
    });
  });
});

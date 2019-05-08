
window.MobileSelect = (function() {

	function getClass(dom,string) {
		return dom.getElementsByClassName(string);
	}

	function MobileSelect(config) {
		this.mobileSelect;
		this.wheelsData = config.wheels;
	    this.jsonType =  false;
	    this.jsonData = [];
	    this.checkDataType();
		this.renderWheels(this.wheelsData);
	    this.displayJson = []; 
	    this.cascade = false;
	    this.startY;
	    this.moveEndY;
	    this.moveY;
	    this.oldMoveY;
	    this.offset = 0;
	    this.offsetSum = 0;
	    this.oversizeBorder;
	    this.curDistance = [];
	    this.clickStatus = false;
		this.init(config);
	}
	
	MobileSelect.prototype = {
		constructor: MobileSelect,
		init: function(config){
			var _this = this;
			_this.trigger = document.querySelector(config.trigger);
		    _this.wheel = getClass(_this.mobileSelect,'wheel');   //wheel
		    _this.slider = getClass(_this.mobileSelect,'selectContainer'); // slider
			_this.wheels = _this.mobileSelect.querySelector('.wheels');   //wheels
		    _this.liHeight = _this.mobileSelect.querySelector('li').offsetHeight;
		    // _this.ensureBtn = _this.mobileSelect.querySelector('.ensure');
	    	// _this.closeBtn = _this.mobileSelect.querySelector('.cancel');
		    // _this.grayLayer = _this.mobileSelect.querySelector('.grayLayer');
		    _this.popUp = _this.mobileSelect.querySelector('.content');
		    _this.callback = config.callback ? config.callback : function(){};
		    _this.limit = config.limit ? config.limit : function(){};
		    _this.initPosition = config.position ? config.position : [];
		    _this.titleText = config.title ? config.title : '';
			// _this.baseDiv = config.baseDiv ? config.baseDiv : [];
			_this.trigger.readOnly=true;
			_this.trigger.style.cursor='pointer';
			_this.setTitle(_this.titleText);
			_this.checkCascade();

			if (_this.cascade) {
				_this.initCascade();
			}

			if(_this.initPosition.length == 0){
				for(var i=0; i<_this.slider.length; i++){
					_this.initPosition.push(0);
				}
			}

			_this.setCurDistance(_this.initPosition);
			_this.addListenerAll();

			/* ****************************************************** */
			// console.log(this)
		   
			/* ****************************************************** */
			
		    // _this.ensureBtn.addEventListener('click',function(){
		    // 	_this.mobileSelect.classList.remove('mobileSelect-show');
			//     var tempValue ='';
		    // 	for(var i=0; i<_this.wheel.length; i++){
		    // 		i==_this.wheel.length-1 ? tempValue += _this.getValue(i) : tempValue += _this.getValue(i)+' ';
		    // 	}
			// 	_this.trigger.value = tempValue;
		    // 	_this.callback(_this.getIndexArr(),_this.getJson());
			// });

			// speak.addEventListener('click',function(){
		    // 	// _this.mobileSelect.classList.remove('mobileSelect-show');
			//     var tempValue ='';
		    // 	for(var i=0; i<_this.wheel.length; i++){
		    // 		i==_this.wheel.length-1 ? tempValue += _this.getValue(i) : tempValue += _this.getValue(i)+' ';
		    // 	}
			// 	_this.trigger.value = tempValue;
			// });

			_this.mobileSelect.classList.add('mobileSelect-show');
			
		    // _this.trigger.addEventListener('click',function(){
		    // 	_this.mobileSelect.classList.add('mobileSelect-show');
		    // });
		    // _this.grayLayer.addEventListener('click',function(){
		    // 	_this.mobileSelect.classList.remove('mobileSelect-show');
			// });
		
			$('#speak').click(function(){
				var tempValue ='';
		    	for(var i=0; i<_this.wheel.length; i++){
					i==_this.wheel.length-1 ? tempValue += _this.getValue(i) : tempValue += _this.getValue(i)+' ';
		    	}
				// var text = $('#message').val();
				
				var text = tempValue;
				console.log(text);

				var msg = new SpeechSynthesisUtterance();
				var voices = window.speechSynthesis.getVoices();
				// msg.voice = voices[$('#voices').val()];
				// msg.rate = $('#rate').val() / 10;
				// msg.pitch = $('#pitch').val();
				msg.voice = voices[3];
				msg.rate = 1;
				msg.pitch = 1;
				msg.text = text;
		  
				msg.onend = function(e) {
				  console.log('Finished in ' + event.elapsedTime + ' seconds.');
				};
		  
				speechSynthesis.speak(msg);
			});

			
		    _this.popUp.addEventListener('click',function(){
		    	event.stopPropagation(); 
		    });

			_this.fixRowStyle(); //岳���쀦빊
		},

		setTitle: function(string){
			var _this = this;
			_this.titleText = string;
			// _this.mobileSelect.querySelector('.title').innerHTML = _this.titleText;
		},

		renderWheels: function(wheelsData){
			var _this = this;
			_this.mobileSelect = document.createElement("div");
			_this.mobileSelect.className = "mobileSelect";
			_this.mobileSelect.innerHTML = 
		    	// '<div class="grayLayer"></div>'+
		        '<div class="content">'+
		            // '<div class="btnBar">'+
		            //     '<div class="fixWidth">'+
		            //         '<div class="cancel">Cancel</div>'+
		            //         '<div class="title"></div>'+
		            //         '<div class="ensure">Select</div>'+
		            //     '</div>'+
					// '</div>'+
					// '<select id="voices" class="hidden voices"></select> ' +
					// '<input type="hidden" id="rate" min="1" max="100" value="10" />' +
					// '<input type="hidden" id="pitch" min="0" max="2" value="1" />' +
					'<input type="hidden" id="message" placeholder="message" value="Test">' +
					'<div class="caption-bar"><button class="btn btn-custom3 waves-effect waves-light btn" id="speak"><i class="fas fa-volume-up" style="font-size:24px"></i></button></div>' +
		            '<div class="panel">'+
		                '<div class="fixWidth">'+
		                	'<div class="wheels">'+
			                '</div>'+
		                    '<div class="selectLine"></div>'+
		                    '<div class="shadowMask"></div>'+
		                '</div>'+
		            '</div>' +
				'</div>';
		    document.body.appendChild(_this.mobileSelect);

			var tempHTML='';
			for(var i=0; i<wheelsData.length; i++){ 
				tempHTML += '<div class="wheel"><ul class="selectContainer">';
				if(_this.jsonType){
					for(var j=0; j<wheelsData[i].data.length; j++){ 
						tempHTML += '<li data-id="'+wheelsData[i].data[j].id+'">'+wheelsData[i].data[j].value+'</li>';
					}
				}else{
					for(var j=0; j<wheelsData[i].data.length; j++){ 
						tempHTML += '<li>'+wheelsData[i].data[j]+'</li>';
					}
				}
				tempHTML += '</ul></div>';
			}
			_this.mobileSelect.querySelector('.wheels').innerHTML = tempHTML;
		},

		addListenerAll: function(){
			var _this = this;
			for(var i=0; i<_this.slider.length; i++){

				(function (i) {
					_this.addListenerWheel(_this.wheel[i], i);
					_this.addListenerLi(i);
				})(i);
			}
		},

		addListenerWheel: function(theWheel, index){
			var _this = this;
			theWheel.addEventListener('touchstart', function () {
				_this.touch(event, this.firstChild, index);
			},false);
			theWheel.addEventListener('touchend', function () {
				_this.touch(event, this.firstChild, index);
			},false);
			theWheel.addEventListener('touchmove', function () {
				_this.touch(event, this.firstChild, index);
			},false);

			//PC
			theWheel.addEventListener('mousedown', function () {
				_this.dragClick(event, this.firstChild, index);
			},false);
			theWheel.addEventListener('mousemove', function () {
				_this.dragClick(event, this.firstChild, index);
			},false);
			theWheel.addEventListener('mouseup', function () {
				_this.dragClick(event, this.firstChild, index);
			},true); 
		},

		addListenerLi:function(sliderIndex){
			var _this = this;
			var curWheelLi = _this.slider[sliderIndex].getElementsByTagName('li');
			// console.log(curWheelLi);
			for(var j=0; j<curWheelLi.length;j++){
				(function (j) {
					curWheelLi[j].addEventListener('click',function(){
						_this.singleClick(this, j, sliderIndex);
					},false);
				})(j);
			}
		},

		checkDataType: function(){ 
			var _this = this;
			if(typeof(_this.wheelsData[0].data[0])=='object'){
				_this.jsonType = true;
				_this.jsonData = _this.wheelsData[0].data;
			}
		},

		checkCascade: function(){
			var _this = this;
			if(_this.jsonType){ 
				var node = _this.wheelsData[0].data;
				for(var i=0; i<node.length; i++){
					if('childs' in node[i] && node[i].childs.length > 0){
						_this.cascade = true;
						break;
					}
				}
			}else{
				_this.cascade = false;
			}
		},

		initCascade: function(){
			var _this = this;
			_this.displayJson.push(_this.generateArrData(_this.jsonData));
			_this.checkArrDeep(_this.jsonData[0]);
			//console.log('弱녻쫨�양ㅊ�꼓son:'); 
			//console.log(_this.displayJson);
			_this.updateWheels();
		},

		generateArrData: function (targetArr) {
			var tempArr = [];
			for(var i=0; i<targetArr.length; i++){
				tempArr.push({
					"id": targetArr[i].id,
					"value": targetArr[i].value
				});	
			}
			return tempArr;
		},

		checkArrDeep: function (parent) { //
			var _this = this;
			if ('childs' in parent && parent.childs.length > 0) {
				_this.displayJson.push(_this.generateArrData(parent.childs)) ; //
				_this.checkArrDeep(parent.childs[0]);//
			}
		},

		checkRange: function(index, posIndexArr){
			var _this = this;
			var deleteNum = _this.displayJson.length-1-index;
			for(var i=0; i<deleteNum; i++){
				_this.displayJson.pop(); //岳�뵻 displayJson
			}
			var resultNode;
			for (var i = 0; i <= index; i++){
				if (i == 0)
					resultNode = _this.jsonData[posIndexArr[0]];
				else {
					resultNode = resultNode.childs[posIndexArr[i]];
				}
			}
			_this.checkArrDeep(resultNode);
			//console.log(_this.displayJson);
			_this.updateWheels();
			_this.fixRowStyle();
			_this.setCurDistance(_this.resetPostion(index, posIndexArr));
		},

		resetPostion: function(index, posIndexArr){
			var _this = this;
			var tempPosArr = posIndexArr;
			var tempCount;
			if(_this.slider.length > posIndexArr.length){ 
				tempCount = _this.slider.length - posIndexArr.length;
				for(var i=0; i<tempCount; i++){  
					tempPosArr.push(0);
				}
			}else if(_this.slider.length < posIndexArr.length){
				tempCount = posIndexArr.length - _this.slider.length;
				for(var i=0; i<tempCount; i++){
					tempPosArr.pop();
				}	
			}
			for(var i=index+1; i< tempPosArr.length; i++){
				tempPosArr[i] = 0;
			} 
			return tempPosArr;
		},

		updateWheels: function(){
			var _this = this;
			//�좈솮鸚싦퐰�꼠heel
			if(_this.wheel.length > _this.displayJson.length){
				var count = _this.wheel.length - _this.displayJson.length;
				for(var i=0; i<count; i++){
					_this.wheels.removeChild(_this.wheel[_this.wheel.length-1]);
				}
			}

			for(var i=0; i<_this.displayJson.length; i++){ //��
				(function (i) {
					var tempHTML='';
					if(_this.wheel[i]){
						//console.log('�믣뀯Li');
						for(var j=0; j<_this.displayJson[i].length; j++){ //烏�
							tempHTML += '<li data-id="'+_this.displayJson[i][j].id+'">'+_this.displayJson[i][j].value+'</li>';
						}
						_this.slider[i].innerHTML = tempHTML;

					}else{
						var tempWheel = document.createElement("div");
						tempWheel.className = "wheel";
						tempHTML = '<ul class="selectContainer">';
						for(var j=0; j<_this.displayJson[i].length; j++){ //烏�
							tempHTML += '<li data-id="'+_this.displayJson[i][j].id+'">'+_this.displayJson[i][j].value+'</li>';
						}
						tempHTML += '</ul>';
						tempWheel.innerHTML = tempHTML;

						_this.addListenerWheel(tempWheel, i);
				    	_this.wheels.appendChild(tempWheel); 
					}
					_this.addListenerLi(i);
				})(i);
			}
		},

		updateWheel: function(sliderIndex, data){
			var _this = this;
			var tempHTML='';
			for(var j=0; j<data.length; j++){
				tempHTML += '<li>'+data[j]+'</li>'
			}
			_this.slider[sliderIndex].innerHTML = tempHTML;
			_this.addListenerLi(sliderIndex);
		},

		fixRowStyle: function(){
			var _this = this;
			var width = (100/_this.wheel.length).toFixed(2);
			for(var i=0; i<_this.wheel.length; i++){
				_this.wheel[i].style.width = width+'%';
			}
		},

	    getIndex: function(distance){
	        return Math.round((2*this.liHeight-distance)/this.liHeight);
	    },

	    getIndexArr: function(){
	    	var _this = this;
	    	var temp = [];
	    	for(var i=0; i<_this.curDistance.length; i++){
	    		temp.push(_this.getIndex(_this.curDistance[i]));
	    	}
	    	return temp;
	    },

	    getJson: function(){
	    	var _this = this;
	    	var temp = [];
	    	var positionArr = _this.getIndexArr();
	    	if(_this.cascade){
		    	for(var i=0; i<_this.wheel.length; i++){
		    		temp.push(_this.displayJson[i][positionArr[i]]);
		    	}
	    	}
	    	else if(_this.jsonType){
		    	for(var i=0; i<_this.curDistance.length; i++){
		    		temp.push(_this.wheelsData[i].data[_this.getIndex(_this.curDistance[i])]);
		    	}
	    	}else{
		    	for(var i=0; i<_this.curDistance.length; i++){
		    		temp.push(_this.getValue(i));
		    	}
	    	}
	    	return temp;
	    },

	    calcDistance: function(index){
			return 2*this.liHeight-index*this.liHeight;
	    },

	    setCurDistance: function(indexArr){
	    	var _this = this;
	    	var temp = [];
	    	for(var i=0; i<_this.slider.length; i++){
	    		temp.push(_this.calcDistance(indexArr[i]));
	    		_this.movePosition(_this.slider[i],temp[i]);
	    	}
	    	_this.curDistance = temp;
	    },

	    fixPosition: function(distance){
	        return -(this.getIndex(distance)-2)*this.liHeight;
	    },

	    movePosition: function(theSlider, distance){
	        theSlider.style.webkitTransform = 'translate3d(0,' + distance + 'px, 0)';
	        theSlider.style.transform = 'translate3d(0,' + distance + 'px, 0)';
	    },

	    locatePostion: function(index, posIndex){
	    	this.curDistance[index] = this.calcDistance(posIndex);
	    	this.movePosition(this.slider[index],this.curDistance[index]);
	    },

	    updateCurDistance: function(theSlider, index){
			this.curDistance[index] = parseInt(theSlider.style.transform.split(',')[1]);
	    },

	    getDistance:function(theSlider){
	    	return parseInt(theSlider.style.transform.split(',')[1]);
	    },

	    getValue: function(sliderIndex){
	    	var _this = this;
			var index = _this.getIndex(_this.curDistance[sliderIndex]);
			return _this.slider[sliderIndex].getElementsByTagName('li')[index].innerHTML;
	    },

	    touch: function(event, theSlider, index){
	    	var _this = this;
	    	event = event || window.event;
	    	switch(event.type){
	    		case "touchstart":
			        _this.startY = event.touches[0].clientY;
			        _this.oldMoveY = _this.startY;
	    			break;

	    		case "touchend":

			        _this.moveEndY = event.changedTouches[0].clientY;
			        _this.offsetSum = _this.moveEndY - _this.startY;

					//岳��鵝띸쉰
			        _this.updateCurDistance(theSlider, index);
			        _this.curDistance[index] = _this.fixPosition(_this.curDistance[index]);
			        _this.movePosition(theSlider, _this.curDistance[index]);
			        _this.oversizeBorder = -(theSlider.getElementsByTagName('li').length-3)*_this.liHeight; 


			        //�띶섰
			        if(_this.curDistance[index] + _this.offsetSum > 2*_this.liHeight){
			            _this.curDistance[index] = 2*_this.liHeight;
			            setTimeout(function(){
			                _this.movePosition(theSlider, _this.curDistance[index]);
			            }, 100);

			        }else if(_this.curDistance[index] + _this.offsetSum < _this.oversizeBorder){
			            _this.curDistance[index] = _this.oversizeBorder;
			            setTimeout(function(){
			                _this.movePosition(theSlider, _this.curDistance[index]);
			            }, 100);
			        }


			        _this.limit(_this.getIndexArr(),_this.getJson());

			        if(_this.cascade){
				        var tempPosArr = _this.getIndexArr();
				        tempPosArr[index] = _this.getIndex(_this.curDistance[index]);
			        	_this.checkRange(index, tempPosArr);
			        }

	    			break;

	    		case "touchmove":
			        event.preventDefault();
			        _this.moveY = event.touches[0].clientY;
			        _this.offset = _this.moveY - _this.oldMoveY;

			        _this.updateCurDistance(theSlider, index);
			        _this.curDistance[index] = _this.curDistance[index] + _this.offset;
			        _this.movePosition(theSlider, _this.curDistance[index]);
			        _this.oldMoveY = _this.moveY;
	    			break;
	    	}
	    },

	    dragClick: function(event, theSlider, index){
	    	var _this = this;
	    	event = event || window.event;
	    	switch(event.type){
	    		case "mousedown":
			        _this.startY = event.clientY;
			        _this.oldMoveY = _this.startY;
			        _this.clickStatus = true;
	    			break;

	    		case "mouseup":

			        _this.moveEndY = event.clientY;
			        _this.offsetSum = _this.moveEndY - _this.startY;

					//岳��鵝띸쉰
			        _this.updateCurDistance(theSlider, index);
			        _this.curDistance[index] = _this.fixPosition(_this.curDistance[index]);
			        _this.movePosition(theSlider, _this.curDistance[index]);
			        _this.oversizeBorder = -(theSlider.getElementsByTagName('li').length-3)*_this.liHeight; 


			        //�띶섰
			        if(_this.curDistance[index] + _this.offsetSum > 2*_this.liHeight){
			            _this.curDistance[index] = 2*_this.liHeight;
			            setTimeout(function(){
			                _this.movePosition(theSlider, _this.curDistance[index]);
			            }, 100);

			        }else if(_this.curDistance[index] + _this.offsetSum < _this.oversizeBorder){
			            _this.curDistance[index] = _this.oversizeBorder;
			            setTimeout(function(){
			                _this.movePosition(theSlider, _this.curDistance[index]);
			            }, 100);
			        }

			        _this.clickStatus = false;
			        _this.limit(_this.getIndexArr(),_this.getJson());
			        if(_this.cascade){
				        var tempPosArr = _this.getIndexArr();
				        tempPosArr[index] = _this.getIndex(_this.curDistance[index]);
			        	_this.checkRange(index, tempPosArr);
			        }
	    			break;

	    		case "mousemove":
			        event.preventDefault();
			        if(_this.clickStatus){
				        _this.moveY = event.clientY;
				        _this.offset = _this.moveY - _this.oldMoveY;

				        _this.updateCurDistance(theSlider, index);
				        _this.curDistance[index] = _this.curDistance[index] + _this.offset;
				        _this.movePosition(theSlider, _this.curDistance[index]);
				        _this.oldMoveY = _this.moveY;
			        }
	    			break;
	    	}
	    },

	    singleClick: function(theLi, index, sliderIndex){
			var _this = this;
			// console.log(this);
	        if(_this.cascade){
		        var tempPosArr = _this.getIndexArr();
		        tempPosArr[sliderIndex] = index;
	        	_this.checkRange(sliderIndex, tempPosArr);

	        }else{
		        _this.curDistance[sliderIndex] = (2-index)*_this.liHeight;
		        _this.movePosition(theLi.parentNode, _this.curDistance[sliderIndex]);
	        }
	    }

	};

	return MobileSelect;
})();
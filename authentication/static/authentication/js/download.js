jQuery(function($){$('body').on('click','.js-btn-download',function(e){e.preventDefault();var download_link=$(this).data('download-link');var template_name=$(this).data('template-name');$('input[name="download-link"]').val('');$('input[name="download-link"]').val(download_link);$('input[name="template-name"]').val('');$('input[name="template-name"]').val(template_name);var post_id=$(this).attr('data-id'),nonce=$(this).attr("data-nonce"),name=$(this).attr("data-short-name");var url=window.location.origin+'/download/'+'untree.co-'+name+'.zip';window.location=url
$.ajax({url:download_url.ajax_url,type:'POST',data:{action:'download_action',post_id:post_id,nonce:nonce},success:function(response){}});return false;});$('body').on('click','.js-btn-download-htmlkit',function(e){e.preventDefault();var download_link=$(this).data('download-link');var template_name=$(this).data('template-name');$('input[name="download-link"]').val('');$('input[name="download-link"]').val(download_link);$('input[name="template-name"]').val('');$('input[name="template-name"]').val(template_name);var post_id=$(this).attr('data-id'),nonce=$(this).attr("data-nonce"),name=$(this).attr("data-short-name");download_name=$(this).attr("data-download-name");var url=window.location.origin+'/download/'+download_name;window.location=url
$.ajax({url:download_url.ajax_url,type:'POST',data:{action:'download_action',post_id:post_id,nonce:nonce},success:function(response){}});return false;})});
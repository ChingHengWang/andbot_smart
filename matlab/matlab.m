close all;
clear all

raw= importdata('miku.txt');
sz=size(raw);
sz=sz(1);
j=1;
for i=1:sz
    if (raw(i,3)==1)
        Draw(j,:)=[raw(i,1) raw(i,2)];
        j=j+1;
        
    end
end

figure;plot(Draw(:,1),Draw(:,2),'.')


nn= importdata('miku_2_10_10_1_sigmoid_epoch_10_batch_size_10.txt');
sz=size(nn);
sz=sz(1);
j=1;
for i=1:sz
    if (nn(i,3)>0.)
        Dnn(j,:)=[nn(i,1) nn(i,2)];
        j=j+1;
        
    end
end        
figure;plot(Dnn(:,1),Dnn(:,2),'.');
title('miku 2 10 10 1 sigmoid epoch 10 batch size 10 bias:0.')
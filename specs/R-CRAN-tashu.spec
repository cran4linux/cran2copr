%global __brp_check_rpaths %{nil}
%global packname  tashu
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis and Prediction of Bicycle Rental Amount

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-drat 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-drat 

%description
Provides functions for analyzing citizens' bicycle usage pattern and
predicting rental amount on specific conditions. Functions on this package
interacts with data on 'tashudata' package, a 'drat' repository.
'tashudata' package contains rental/return history on public bicycle
system('Tashu'), weather for 3 years and bicycle station information. To
install this data package, see the instructions at
<https://github.com/zeee1/Tashu_Rpackage>. top10_stations(), top10_paths()
function visualizes image showing the most used top 10 stations and paths.
daily_bike_rental() and monthly_bike_rental() shows daily, monthly amount
of bicycle rental. create_train_dataset(), create_test_dataset() is data
processing function for prediction. Bicycle rental history from 2013 to
2014 is used to create training dataset and that on 2015 is for test
dataset. Users can make random-forest prediction model by using
create_train_model() and predict amount of bicycle rental in 2015 by using
predict_bike_rental().

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}

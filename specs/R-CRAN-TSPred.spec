%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TSPred
%global packver   5.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Functions for Benchmarking Time Series Prediction

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-KFAS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MuMIn 
BuildRequires:    R-CRAN-wavelets 
BuildRequires:    R-CRAN-ModelMetrics 
BuildRequires:    R-CRAN-RSNNS 
BuildRequires:    R-CRAN-Rlibeemd 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-elmNNRcpp 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-keras 
BuildRequires:    R-CRAN-tfdatasets 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-KFAS 
Requires:         R-stats 
Requires:         R-CRAN-MuMIn 
Requires:         R-CRAN-wavelets 
Requires:         R-CRAN-ModelMetrics 
Requires:         R-CRAN-RSNNS 
Requires:         R-CRAN-Rlibeemd 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-elmNNRcpp 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-plyr 
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-keras 
Requires:         R-CRAN-tfdatasets 

%description
Functions for defining and conducting a time series prediction process
including pre(post)processing, decomposition, modelling, prediction and
accuracy assessment. The generated models and its yielded prediction
errors can be used for benchmarking other time series prediction methods
and for creating a demand for the refinement of such methods. For this
purpose, benchmark data from prediction competitions may be used.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tspredit
%global packver   1.2.747
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.747
Release:          1%{?dist}%{?buildtag}
Summary:          Time Series Prediction with Integrated Tuning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-elmNNRcpp 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-hht 
BuildRequires:    R-CRAN-KFAS 
BuildRequires:    R-CRAN-mFilter 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-wavelets 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-daltoolbox 
Requires:         R-stats 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-elmNNRcpp 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-hht 
Requires:         R-CRAN-KFAS 
Requires:         R-CRAN-mFilter 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-wavelets 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-daltoolbox 

%description
Time series prediction is a critical task in data analysis, requiring not
only the selection of appropriate models, but also suitable data
preprocessing and tuning strategies. TSPredIT (Time Series Prediction with
Integrated Tuning) is a framework that provides a seamless integration of
data preprocessing, decomposition, model training, hyperparameter
optimization, and evaluation. Unlike other frameworks, TSPredIT emphasizes
the co-optimization of both preprocessing and modeling steps, improving
predictive performance. It supports a variety of statistical and machine
learning models, filtering techniques, outlier detection, data
augmentation, and ensemble strategies. More information is available in
Salles et al. <doi:10.1007/978-3-662-68014-8_2>.

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

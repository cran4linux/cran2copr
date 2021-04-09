%global packname  DMLLZU
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Double Machine Learning

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-ISLR 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-ISLR 

%description
Yang(2020,<doi:10.1016/j.jeconom.2020.01.018>) come up with Double Machine
Learning model ,it is based on this model, using four machine learning
methods-- bagging, Boosting, random forest and neural network, and then
based on the four models for two different combinations of the integrated
model -- linear model combination and random forest .

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  deepregression
%global packver   2.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting Deep Distributional Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tensorflow >= 2.2.0
BuildRequires:    R-CRAN-keras >= 2.2.0
BuildRequires:    R-CRAN-reticulate >= 1.14
BuildRequires:    R-CRAN-coro >= 1.0.3
BuildRequires:    R-CRAN-torchvision >= 0.5.1
BuildRequires:    R-CRAN-luz >= 0.4.0
BuildRequires:    R-CRAN-tfprobability 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tfruns 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-torch 
Requires:         R-CRAN-tensorflow >= 2.2.0
Requires:         R-CRAN-keras >= 2.2.0
Requires:         R-CRAN-reticulate >= 1.14
Requires:         R-CRAN-coro >= 1.0.3
Requires:         R-CRAN-torchvision >= 0.5.1
Requires:         R-CRAN-luz >= 0.4.0
Requires:         R-CRAN-tfprobability 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tfruns 
Requires:         R-methods 
Requires:         R-CRAN-torch 

%description
Allows for the specification of semi-structured deep distributional
regression models which are fitted in a neural network as proposed by
Ruegamer et al. (2023) <doi:10.18637/jss.v105.i02>. Predictors can be
modeled using structured (penalized) linear effects, structured non-linear
effects or using an unstructured deep network model.

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

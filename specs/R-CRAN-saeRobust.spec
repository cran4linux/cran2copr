%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  saeRobust
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Small Area Estimation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-aoos 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-modules 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-methods 
Requires:         R-CRAN-aoos 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-modules 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-spdep 

%description
Methods to fit robust alternatives to commonly used models used in Small
Area Estimation. The methods here used are based on best linear unbiased
predictions and linear mixed models. At this time available models include
area level models incorporating spatial and temporal correlation in the
random effects.

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

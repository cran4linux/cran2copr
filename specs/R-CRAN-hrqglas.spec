%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hrqglas
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Group Variable Selection for Quantile and Robust Mean Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.4
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-quantreg 
Requires:         R-CRAN-Rcpp >= 1.0.4
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-graphics 
Requires:         R-CRAN-quantreg 

%description
A program that conducts group variable selection for quantile and robust
mean regression (Sherwood and Li, 2022). The group lasso penalty (Yuan and
Lin, 2006) is used for group-wise variable selection. Both of the quantile
and mean regression models are based on the Huber loss. Specifically, with
the tuning parameter in the Huber loss approaching to 0, the quantile
check function can be approximated by the Huber loss for the median and
the tilted version of Huber loss at other quantiles. Such approximation
provides computational efficiency and stability, and has also been shown
to be statistical consistent.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SNSequate
%global packver   1.3-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Standard and Nonstandard Statistical Models and Methods for Test Equating

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-emdbook 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-progress 
Requires:         R-CRAN-magic 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-emdbook 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-progress 

%description
Contains functions to perform various models and methods for test
equating. It currently implements the traditional mean, linear and
equipercentile equating methods. Both IRT observed-score and true-score
equating are also supported, as well as the mean-mean, mean-sigma, Haebara
and Stocking-Lord IRT linking methods. It also supports newest methods
such that local equating, kernel equating (using Gaussian, logistic,
Epanechnikov, uniform and adaptive kernels) with presmoothing, and IRT
parameter linking methods based on asymmetric item characteristic
functions. Functions to obtain both standard error of equating (SEE) and
standard error of equating differences between two equating functions
(SEED) are also implemented for the kernel method of equating.

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

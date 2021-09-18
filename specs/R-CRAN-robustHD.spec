%global __brp_check_rpaths %{nil}
%global packname  robustHD
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Methods for High-Dimensional Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-robustbase >= 0.9.5
BuildRequires:    R-CRAN-ggplot2 >= 0.9.2
BuildRequires:    R-CRAN-Rcpp >= 0.9.10
BuildRequires:    R-CRAN-perry >= 0.3.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.3.0
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-grDevices 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-robustbase >= 0.9.5
Requires:         R-CRAN-ggplot2 >= 0.9.2
Requires:         R-CRAN-Rcpp >= 0.9.10
Requires:         R-CRAN-perry >= 0.3.0
Requires:         R-CRAN-MASS 
Requires:         R-grDevices 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Robust methods for high-dimensional data, in particular linear model
selection techniques based on least angle regression and sparse
regression.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tensorMiss
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Handle Missing Tensor Data with C++ Integration

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.11
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-rTensor 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 1.0.11
Requires:         R-CRAN-RcppEigen 
Requires:         R-CRAN-rTensor 
Requires:         R-stats 

%description
To handle higher-order tensor data. See Kolda and Bader (2009)
<doi:10.1137/07070111X> for details on tensor. While existing packages on
tensor data extend the base 'array' class to some data classes, this
package serves as an alternative resort to handle tensor only as 'array'
class. Some functionalities related to missingness are also supported.

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

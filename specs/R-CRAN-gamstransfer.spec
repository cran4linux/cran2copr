%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gamstransfer
%global packver   3.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          A Data Interface Between 'GAMS' and R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-R6 >= 2.5.1
BuildRequires:    R-CRAN-R.utils >= 2.11.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.6
BuildRequires:    R-CRAN-collections >= 0.3.6
Requires:         R-CRAN-R6 >= 2.5.1
Requires:         R-CRAN-R.utils >= 2.11.0
Requires:         R-CRAN-Rcpp >= 1.0.6
Requires:         R-CRAN-collections >= 0.3.6

%description
Read, analyze, modify, and write 'GAMS' (General Algebraic Modeling
System) data. The main focus of 'gamstransfer' is the highly efficient
transfer of data with 'GAMS' <https://www.gams.com/>, while keeping these
operations as simple as possible for the user. The transfer of data
usually takes place via an intermediate GDX (GAMS Data Exchange) file.
Additionally, 'gamstransfer' provides utility functions to get an overview
of 'GAMS' data and to check its validity.

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

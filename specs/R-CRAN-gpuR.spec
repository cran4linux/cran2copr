%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gpuR
%global packver   2.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          GPU Functions for R Objects

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-RViennaCL >= 1.7.1.7
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.4.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.15
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 0.12.15
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-RViennaCL >= 1.7.1.7
Requires:         R-CRAN-BH 
Requires:         R-CRAN-RcppEigen >= 0.3.3.4.0

%description
Provides GPU enabled functions for 'R' objects in a simple and
approachable manner.  New 'gpu*' and 'vcl*' classes have been provided to
wrap typical 'R' objects (e.g. vector, matrix), in both host and device
spaces, to mirror typical 'R' syntax without the need to know 'OpenCL'.

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

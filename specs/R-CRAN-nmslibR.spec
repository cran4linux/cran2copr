%global __brp_check_rpaths %{nil}
%global packname  nmslibR
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Non Metric Space (Approximate) Library

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildRequires:    R-CRAN-RcppArmadillo >= 0.8.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-KernelKnn 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 0.12.7
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-KernelKnn 
Requires:         R-utils 

%description
A Non-Metric Space Library ('NMSLIB' <https://github.com/nmslib/nmslib>)
wrapper, which according to the authors "is an efficient cross-platform
similarity search library and a toolkit for evaluation of similarity
search methods. The goal of the 'NMSLIB'
<https://github.com/nmslib/nmslib> Library is to create an effective and
comprehensive toolkit for searching in generic non-metric spaces. Being
comprehensive is important, because no single method is likely to be
sufficient in all cases. Also note that exact solutions are hardly
efficient in high dimensions and/or non-metric spaces. Hence, the main
focus is on approximate methods". The wrapper also includes Approximate
Kernel k-Nearest-Neighbor functions based on the 'NMSLIB'
<https://github.com/nmslib/nmslib> 'Python' Library.

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

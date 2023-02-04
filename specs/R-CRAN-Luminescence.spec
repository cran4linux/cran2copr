%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Luminescence
%global packver   0.9.21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.21
Release:          1%{?dist}%{?buildtag}
Summary:          Comprehensive Luminescence Dating Data Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-mclust >= 6.0.0
BuildRequires:    R-CRAN-XML >= 3.99
BuildRequires:    R-CRAN-plotrix >= 3.8.2
BuildRequires:    R-CRAN-DEoptim >= 2.2.8
BuildRequires:    R-CRAN-lamW >= 2.1.1
BuildRequires:    R-CRAN-zoo >= 1.8
BuildRequires:    R-CRAN-shape >= 1.4.6
BuildRequires:    R-CRAN-httr >= 1.4.4
BuildRequires:    R-CRAN-readxl >= 1.4.1
BuildRequires:    R-CRAN-minpack.lm >= 1.2.3
BuildRequires:    R-CRAN-data.table >= 1.14.6
BuildRequires:    R-CRAN-bbmle >= 1.0.25
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-CRAN-matrixStats >= 0.63.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.11.4.0.0
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
Requires:         R-CRAN-mclust >= 6.0.0
Requires:         R-CRAN-XML >= 3.99
Requires:         R-CRAN-plotrix >= 3.8.2
Requires:         R-CRAN-DEoptim >= 2.2.8
Requires:         R-CRAN-lamW >= 2.1.1
Requires:         R-CRAN-zoo >= 1.8
Requires:         R-CRAN-shape >= 1.4.6
Requires:         R-CRAN-httr >= 1.4.4
Requires:         R-CRAN-readxl >= 1.4.1
Requires:         R-CRAN-minpack.lm >= 1.2.3
Requires:         R-CRAN-data.table >= 1.14.6
Requires:         R-CRAN-bbmle >= 1.0.25
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-CRAN-matrixStats >= 0.63.0
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-parallel 

%description
A collection of various R functions for the purpose of Luminescence dating
data analysis. This includes, amongst others, data import, export,
application of age models, curve deconvolution, sequence analysis and
plotting of equivalent dose distributions.

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

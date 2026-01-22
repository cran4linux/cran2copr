%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  multivarious
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Extensible Data Structures for Multivariate Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-chk 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-rsvd 
BuildRequires:    R-CRAN-svd 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-geigen 
BuildRequires:    R-CRAN-PRIMME 
BuildRequires:    R-CRAN-GPArotation 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-chk 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-rsvd 
Requires:         R-CRAN-svd 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-irlba 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-future 
Requires:         R-CRAN-geigen 
Requires:         R-CRAN-PRIMME 
Requires:         R-CRAN-GPArotation 
Requires:         R-CRAN-lifecycle 

%description
Provides a set of basic and extensible data structures and functions for
multivariate analysis, including dimensionality reduction techniques,
projection methods, and preprocessing functions. The aim of this package
is to offer a flexible and user-friendly framework for multivariate
analysis that can be easily extended for custom requirements and specific
data analysis tasks.

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

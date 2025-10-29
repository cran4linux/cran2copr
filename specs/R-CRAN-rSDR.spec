%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rSDR
%global packver   1.0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Sufficient Dimension Reduction

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-ManifoldOptim 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rstiefel 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggsci 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-ManifoldOptim 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rstiefel 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggsci 

%description
A novel sufficient-dimension reduction method is robust against outliers
using alpha-distance covariance and manifold-learning in dimensionality
reduction problems. Please refer Hsin-Hsiung Huang, Feng Yu & Teng Zhang
(2024) <doi:10.1080/10485252.2024.2313137> for the details.

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

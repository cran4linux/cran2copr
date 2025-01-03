%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CCMMR
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Minimization of the Convex Clustering Loss Function

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-methods >= 4.1.0
BuildRequires:    R-graphics >= 4.1.0
BuildRequires:    R-stats >= 4.1
BuildRequires:    R-CRAN-RANN >= 2.6.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-methods >= 4.1.0
Requires:         R-graphics >= 4.1.0
Requires:         R-stats >= 4.1
Requires:         R-CRAN-RANN >= 2.6.1
Requires:         R-CRAN-Rcpp >= 1.0.7

%description
Implements the convex clustering through majorization-minimization (CCMM)
algorithm described in Touw, Groenen, and Terada (2022)
<doi:10.48550/arXiv.2211.01877> to perform minimization of the convex
clustering loss function.

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

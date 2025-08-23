%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NPflow
%global packver   0.13.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.13.6
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Nonparametrics for Automatic Gating of Flow-Cytometry Data

License:          LGPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.11
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-fastcluster 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.11
Requires:         R-CRAN-truncnorm 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-fastcluster 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pheatmap 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-GGally 

%description
Dirichlet process mixture of multivariate normal, skew normal or skew
t-distributions modeling oriented towards flow-cytometry data
preprocessing applications. Method is detailed in: Hejblum, Alkhassimn,
Gottardo, Caron & Thiebaut (2019) <doi: 10.1214/18-AOAS1209>.

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

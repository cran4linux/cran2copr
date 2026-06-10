%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  plantmix
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Genetic Study of Plant Mixtures

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-TMB >= 1.9.17
BuildRequires:    R-CRAN-Rcpp >= 1.0.13
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-TMB >= 1.9.17
Requires:         R-CRAN-Rcpp >= 1.0.13
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lme4 
Requires:         R-graphics 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Fit linear mixed models dedicated to the genetic study of plant mixtures,
such as those based on general and specific mixing abilities (GMA-SMA) as
well as direct and social breeding values (DBV-SBV), also known as direct
and indirect genetic effects (DGE-IGE). More details in Forst et al (2019,
<doi:10.1016/j.fcr.2019.107571>) for GMA-SMA models, and Salomon et al
(2026, <doi:10.64898/2026.03.27.714849>) for DBV-SBV models. The package
also provides functions to optimize experimental designs, simulate data
sets and compute interaction indices.

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

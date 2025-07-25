%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SensoMineR
%global packver   1.28
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.28
Release:          1%{?dist}%{?buildtag}
Summary:          Sensory Data Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-FactoMineR >= 2.7
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-AlgDesign 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-ggrepel 
Requires:         R-CRAN-FactoMineR >= 2.7
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-KernSmooth 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-AlgDesign 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-ggrepel 

%description
Statistical Methods to Analyse Sensory Data. SensoMineR: A package for
sensory data analysis. S. Le and F. Husson (2008).

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

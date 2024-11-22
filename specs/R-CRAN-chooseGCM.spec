%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  chooseGCM
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Selecting General Circulation Models for Species Distribution Modeling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-factoextra 
BuildRequires:    R-CRAN-ggcorrplot 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-usedist 
BuildRequires:    R-utils 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-factoextra 
Requires:         R-CRAN-ggcorrplot 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-CRAN-httr 
Requires:         R-methods 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-usedist 
Requires:         R-utils 

%description
Methods to help selecting General Circulation Models (GCMs) in the context
of projecting models to future scenarios. It is provided clusterization
algorithms, distance and correlation metrics, as well as a tailor-made
algorithm to detect the optimum subset of GCMs that recreate the
environment of all GCMs.

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

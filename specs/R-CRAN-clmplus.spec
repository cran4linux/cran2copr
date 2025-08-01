%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  clmplus
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tool-Box of Chain Ladder Plus Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-StMoMo 
BuildRequires:    R-CRAN-ChainLadder 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-StMoMo 
Requires:         R-CRAN-ChainLadder 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-reshape2 

%description
Implementation of the age–period–cohort models for claim development
presented in Pittarello G, Hiabu M, Villegas A (2025) “Replicating and
Extending Chain‑Ladder via an Age–Period–Cohort Structure on the Claim
Development in a Run‑Off Triangle” <doi:10.1080/10920277.2025.2496725>.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ManyIVsNets
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Environmental Phillips Curve Analysis with Multiple Instrumental Variables and Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggraph 
BuildRequires:    R-CRAN-AER 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggraph 
Requires:         R-CRAN-AER 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-magrittr 

%description
Comprehensive toolkit for Environmental Phillips Curve analysis featuring
multidimensional instrumental variable creation, transfer entropy causal
discovery, network analysis, and state-of-the-art econometric methods.
Implements geographic, technological, migration, geopolitical, financial,
and natural risk instruments with robust diagnostics and visualization.
Provides 24 different instrumental variable approaches with empirical
validation. Methods based on Phillips (1958)
<doi:10.1111/j.1468-0335.1958.tb00003.x>, transfer entropy by Schreiber
(2000) <doi:10.1103/PhysRevLett.85.461>, and weak instrument tests by
Stock and Yogo (2005) <doi:10.1017/CBO9780511614491.006>.

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

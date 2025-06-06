%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rwty
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          R We There Yet? Visualizing MCMC Convergence in Phylogenetics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-ggdendro 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-TreeDist 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-viridis 
Requires:         R-grid 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-ggdendro 
Requires:         R-CRAN-GGally 
Requires:         R-parallel 
Requires:         R-CRAN-TreeDist 

%description
Implements various tests, visualizations, and metrics for diagnosing
convergence of MCMC chains in phylogenetics.  It implements and automates
many of the functions of the AWTY package in the R environment, as well as
a host of other functions.  Warren, Geneva, and Lanfear (2017),
<doi:10.1093/molbev/msw279>.

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

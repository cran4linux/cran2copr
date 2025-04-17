%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pcvr
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Plant Phenotyping and Bayesian Statistics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-bayestestR 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-lmeSplines 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-car 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-extraDistr 
Requires:         R-parallel 
Requires:         R-CRAN-bayestestR 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-nlme 
Requires:         R-splines 
Requires:         R-CRAN-lmeSplines 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-car 

%description
Analyse common types of plant phenotyping data, provide a simplified
interface to longitudinal growth modeling and select Bayesian statistics,
and streamline use of 'PlantCV' output. Several Bayesian methods and
reporting guidelines for Bayesian methods are described in Kruschke (2018)
<doi:10.1177/2515245918771304>, Kruschke (2013) <doi:10.1037/a0029146>,
and Kruschke (2021) <doi:10.1038/s41562-021-01177-7>.

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

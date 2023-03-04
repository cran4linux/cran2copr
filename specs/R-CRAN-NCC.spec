%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NCC
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation and Analysis of Platform Trials with Non-Concurrent Controls

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RBesT 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-spaMM 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-magick 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-RBesT 
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lmerTest 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-parallelly 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-spaMM 
Requires:         R-CRAN-mgcv 
Requires:         R-splines 
Requires:         R-CRAN-magick 

%description
Design and analysis of flexible platform trials with non-concurrent
controls. Functions for data generation, analysis, visualization and
running simulation studies are provided. The implemented analysis methods
are described in: Bofill Roig et al. (2022)
<doi:10.1186/s12874-022-01683-w>, Saville et al. (2022)
<doi:10.1177/17407745221112013> and Schmidli et al. (2014)
<doi:10.1111/biom.12242>.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  detect
%global packver   0.5-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analyzing Wildlife Data with Detection Error

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-extraDistr 
Requires:         R-CRAN-Formula 
Requires:         R-stats4 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-extraDistr 

%description
Models for analyzing site occupancy and count data models with detection
error, including single-visit based models (Lele et al. 2012
<doi:10.1093/jpe/rtr042>, Moreno et al. 2010 <doi:10.1890/09-1073.1>,
Solymos et al. 2012 <doi:10.1002/env.1149>, Denes et al. 2016
<doi:10.1111/1365-2664.12818>), conditional distance sampling and
time-removal models (QPAD) (Solymos et al. 2013
<doi:10.1111/2041-210X.12106>, Solymos et al. 2018
<doi:10.1650/CONDOR-18-32.1>), and single bin QPAD (SQPAD) models (Lele &
Solymos 2025). Package development was supported by the Alberta
Biodiversity Monitoring Institute and the Boreal Avian Modelling Project.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CEACT
%global packver   0.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          Cost-Effectiveness Analysis Toolkit for Clinical Trials

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-basetable >= 1.4.5
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-parallel 
Requires:         R-CRAN-basetable >= 1.4.5
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-boot 
Requires:         R-parallel 

%description
Provides tools for trial-based economic evaluation of healthcare
interventions. Computes and visualizes incremental cost-effectiveness
ratios, cost-effectiveness acceptability curves, cost-effectiveness
planes, net monetary benefit tables, and one-way deterministic sensitivity
analyses. Supports cost-utility analyses using observed summaries and
non-parametric bootstrap uncertainty, and multiply imputed data through
Rubin's rules (Rubin 1987, ISBN:9780471087052) or bootstrap-then-impute
resampling (Brand et al. 2019 <doi:10.1002/sim.7956>).

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

%global __brp_check_rpaths %{nil}
%global packname  IrregLong
%global packver   0.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Longitudinal Data with Irregular Observation Times

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-geepack 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-graphics 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-geepack 
Requires:         R-CRAN-data.table 
Requires:         R-graphics 

%description
Functions to help with analysis of longitudinal data featuring irregular
observation times, where the observation times may be associated with the
outcome process. There are functions to quantify the degree of
irregularity, fit inverse-intensity weighted Generalized Estimating
Equations (Lin H, Scharfstein DO, Rosenheck RA (2004)
<doi:10.1111/j.1467-9868.2004.b5543.x>), perform multiple outputation
(Pullenayegum EM (2016) <doi:10.1002/sim.6829>) and fit semi-parametric
joint models (Liang Y (2009) <doi: 10.1111/j.1541-0420.2008.01104.x>).

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rdstagger
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Staggered Regression Discontinuity with Network Interference

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rdrobust 
Requires:         R-stats 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rdrobust 

%description
Implements a unified framework combining staggered
difference-in-differences with regression discontinuity designs and
network interference. Extends Callaway and Sant'Anna (2021)
<doi:10.1016/j.jeconom.2020.12.001> to settings where treatment assignment
is determined by a running variable crossing a cutoff, adoption timing is
heterogeneous across units, and spillover effects operate through a known
network structure. Provides group-time average treatment effects (direct
and spillover), aggregation schemes, bandwidth selection, and
pre-treatment falsification tests.

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

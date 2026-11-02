%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HeatStressR
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate Heat Stress Indices

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-heatindex >= 0.0.2
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
Requires:         R-CRAN-heatindex >= 0.0.2
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-parallel 

%description
Calculates heat-stress indices from meteorological observations using
shared psychrometric calculations and consistent method-specific input
handling. Methods include the physically based outdoor wet-bulb globe
temperature model described by Liljegren et al. (2008)
<doi:10.1080/15459620802310770>, wet-bulb temperature and heat-index
calculations, and established closed-form heat-stress indices. Provides
row-level diagnostics, configurable physical controls, vectorized batch
processing, and optional parallel execution for the Liljegren method. It
is an independently maintained fork of 'HeatStress'; its Liljegren
implementation is not a bitwise-compatible port of the original program.

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

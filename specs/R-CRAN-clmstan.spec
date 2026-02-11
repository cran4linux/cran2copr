%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  clmstan
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cumulative Link Models with 'CmdStanR'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-instantiate 
BuildRequires:    R-CRAN-posterior 
BuildRequires:    R-CRAN-bayesplot 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-stats 
Requires:         R-CRAN-instantiate 
Requires:         R-CRAN-posterior 
Requires:         R-CRAN-bayesplot 
Requires:         R-CRAN-loo 
Requires:         R-stats 

%description
Fits cumulative link models (CLMs) for ordinal categorical data using
'CmdStanR'. Supports various link functions including logit, probit,
cloglog, loglog, cauchit, and flexible parametric links such as
Generalized Extreme Value (GEV), Asymmetric Exponential Power (AEP), and
Symmetric Power. Models are pre-compiled using the 'instantiate' package
for fast execution without runtime compilation. Methods are described in
Agresti (2010, ISBN:978-0-470-08289-8), Wang and Dey (2011)
<doi:10.1007/s10651-010-0154-8>, and Naranjo, Perez, and Martin (2015)
<doi:10.1007/s11222-014-9449-1>.

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

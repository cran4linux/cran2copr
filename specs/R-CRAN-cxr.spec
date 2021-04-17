%global packname  cxr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Toolbox for Modelling Species Coexistence in R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-optimx 
Requires:         R-stats 
Requires:         R-CRAN-mvtnorm 

%description
Recent developments in modern coexistence theory have advanced our
understanding on how species are able to persist and co-occur with other
species at varying abundances. However, applying this mathematical
framework to empirical data is still challenging, precluding a larger
adoption of the theoretical tools developed by empiricists. This package
provides a complete toolbox for modelling interaction effects between
species, and calculate fitness and niche differences. The functions are
flexible, may accept covariates, and different fitting algorithms can be
used. A full description of the underlying methods is available in
García-Callejas, D., Godoy, O., and Bartomeus, I. (2020)
<doi:10.1111/2041-210X.13443>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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

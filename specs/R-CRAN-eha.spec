%global packname  eha
%global packver   2.8.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8.4
Release:          1%{?dist}%{?buildtag}
Summary:          Event History Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-survival >= 3.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-survival >= 3.0
Requires:         R-stats 
Requires:         R-graphics 

%description
Parametric proportional hazards fitting with left truncation and right
censoring for common families of distributions, piecewise constant
hazards, and discrete models. Parametric accelerated failure time models
for left truncated and right censored data. Proportional hazards models
for tabular and register data. Sampling of risk sets in Cox regression,
selections in the Lexis diagram, bootstrapping. Broström (2012)
<doi:10.1201/9781315373942>.

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
test $(gcc -dumpversion) -ge 10 && mkdir -p ~/.R && echo "FFLAGS=$(R CMD config FFLAGS) -fallow-argument-mismatch" > ~/.R/Makevars
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}

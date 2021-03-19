%global packname  AnimalAPD
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Compare Activity Patterns with Activity Probability Density (APD)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-brms 
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-overlap 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-activityGCMM 
Requires:         R-CRAN-brms 
Requires:         R-CRAN-circular 
Requires:         R-CRAN-overlap 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-loo 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-activityGCMM 

%description
Calculation and analyses of Activity Probability Density (APD) for
comparing animal activity patterns with automated Bayesian model selection
using 'STAN'. See Campbell et al. (in press) "A new approach to comparing
animal temporal activity: a more informative, robust, and flexible method
that controls for nested data, quantifies relationship asymmetries, and
allows linear modelling of temporal behaviour."

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

%global packname  qgcomp
%global packver   2.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Quantile G-Computation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-arm 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-pscl 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-arm 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-generics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-pscl 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-tibble 

%description
G-computation for a set of time-fixed exposures with quantile-based basis
functions, possibly under linearity and homogeneity assumptions. This
approach estimates a regression line corresponding to the expected change
in the outcome (on the link basis) given a simultaneous increase in the
quantile-based category for all exposures. Works with continuous, binary,
and right-censored time-to-event outcomes.  Reference: Alexander P. Keil,
Jessie P. Buckley, Katie M. OBrien, Kelly K. Ferguson, Shanshan Zhao, and
Alexandra J. White (2019) A quantile-based g-computation approach to
addressing the effects of exposure mixtures; <doi:10.1289/EHP5838>.

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

%global __brp_check_rpaths %{nil}
%global packname  gamlss.dist
%global packver   6.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Distributions for Generalized Additive Models for Location Scale and Shape

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-grDevices 

%description
A set of distributions which can be used for modelling the response
variables in Generalized Additive Models for Location Scale and Shape,
Rigby and Stasinopoulos (2005), <doi:10.1111/j.1467-9876.2005.00510.x>.
The distributions can be continuous, discrete or mixed distributions.
Extra distributions can be created, by transforming, any continuous
distribution defined on the real line, to a distribution defined on ranges
0 to infinity or 0 to 1, by using a ''log'' or a ''logit' transformation
respectively.

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

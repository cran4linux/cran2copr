%global __brp_check_rpaths %{nil}
%global packname  glmxdiag
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Collection of Graphic Tools for GLM Diagnostics and some Extensions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-VGAM 
Requires:         R-CRAN-VGAM 

%description
Provides diagnostic graphic tools for GLMs, beta-binomial regression model
(estimated by 'VGAM' package), beta regression model (estimated by
'betareg' package) and negative binomial regression model (estimated by
'MASS' package). Since most of functions implemented in 'glmxdiag' already
exist in other packages, the aim is to provide the user unique functions
that work on almost all regression models previously specified. Details
about some of the implemented functions can be found in Brown (1992)
<doi:10.2307/2347617>, Dunn and Smyth (1996) <doi:10.2307/1390802>, O'Hara
Hines and Carter (1993) <doi:10.2307/2347405>, Wang (1985)
<doi:10.2307/1269708>.

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

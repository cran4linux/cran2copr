%global __brp_check_rpaths %{nil}
%global packname  ecotox
%global packver   1.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.4
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Ecotoxicology

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
Requires:         R-stats 
Requires:         R-CRAN-tibble 

%description
A simple approach to using a probit or logit analysis to calculate lethal
concentration (LC) or time (LT) and the appropriate fiducial confidence
limits desired for selected LC or LT for ecotoxicology studies (Finney
1971; Wheeler et al. 2006; Robertson et al. 2007). The simplicity of
'ecotox' comes from the syntax it implies within its functions which are
similar to functions like glm() and lm(). In addition to the simplicity of
the syntax, a comprehensive data frame is produced which gives the user a
predicted LC or LT value for the desired level and a suite of important
parameters such as fiducial confidence limits and slope. Finney, D.J.
(1971, ISBN: 052108041X); Wheeler, M.W., Park, R.M., and Bailer, A.J.
(2006) <doi:10.1897/05-320R.1>; Robertson, J.L., Savin, N.E., Russell,
R.M., and Preisler, H.K. (2007, ISBN: 0849323312).

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

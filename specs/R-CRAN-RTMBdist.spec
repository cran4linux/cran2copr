%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RTMBdist
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Distributions Compatible with Automatic Differentiation by 'RTMB'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RTMB >= 1.7
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-gamlss.dist 
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-movMF 
Requires:         R-CRAN-RTMB >= 1.7
Requires:         R-stats 
Requires:         R-CRAN-gamlss.dist 
Requires:         R-CRAN-circular 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-movMF 

%description
Extends the functionality of the 'RTMB'
<https://kaskr.r-universe.dev/RTMB> package by providing a collection of
non-standard probability distributions compatible with automatic
differentiation (AD). While 'RTMB' enables flexible and efficient
modelling, including random effects, its built-in support is limited to
standard distributions. The package adds additional AD-compatible
distributions, broadening the range of models that can be implemented and
estimated using 'RTMB'. Automatic differentiation and Laplace
approximation are described in Kristensen et al. (2016)
<doi:10.18637/jss.v070.i05>.

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

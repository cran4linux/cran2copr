%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  glam
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Additive and Linear Models (GLAM)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gam 
BuildRequires:    R-stats 
Requires:         R-CRAN-gam 
Requires:         R-stats 

%description
Contains methods for fitting Generalized Linear Models (GLMs) and
Generalized Additive Models (GAMs). Generalized regression models are
common methods for handling data for which assuming Gaussian-distributed
errors is not appropriate. For instance, if the response of interest is
binary, count, or proportion data, one can instead model the expectation
of the response based on an appropriate data-generating distribution. This
package provides methods for fitting GLMs and GAMs under Beta regression,
Poisson regression, Gamma regression, and Binomial regression (currently
GLM only) settings. Models are fit using local scoring algorithms
described in Hastie and Tibshirani (1990) <doi:10.1214/ss/1177013604>.

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

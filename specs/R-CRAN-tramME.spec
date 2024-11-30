%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tramME
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Transformation Models with Mixed Effects

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-mgcv >= 1.8.34
BuildRequires:    R-CRAN-TMB >= 1.7.15
BuildRequires:    R-CRAN-mlt >= 1.1.0
BuildRequires:    R-CRAN-basefun >= 1.0.6
BuildRequires:    R-CRAN-variables >= 1.0.2
BuildRequires:    R-CRAN-tram >= 0.3.2
BuildRequires:    R-CRAN-alabama 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-coneproj 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-reformulas 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-mgcv >= 1.8.34
Requires:         R-CRAN-TMB >= 1.7.15
Requires:         R-CRAN-mlt >= 1.1.0
Requires:         R-CRAN-basefun >= 1.0.6
Requires:         R-CRAN-variables >= 1.0.2
Requires:         R-CRAN-tram >= 0.3.2
Requires:         R-CRAN-alabama 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-nlme 
Requires:         R-stats 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-coneproj 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-reformulas 

%description
Likelihood-based estimation of mixed-effects transformation models using
the Template Model Builder ('TMB', Kristensen et al., 2016)
<doi:10.18637/jss.v070.i05>. The technical details of transformation
models are given in Hothorn et al. (2018) <doi:10.1111/sjos.12291>.
Likelihood contributions of exact, randomly censored (left, right,
interval) and truncated observations are supported. The random effects are
assumed to be normally distributed on the scale of the transformation
function, the marginal likelihood is evaluated using the Laplace
approximation, and the gradients are calculated with automatic
differentiation (Tamasi & Hothorn, 2021) <doi:10.32614/RJ-2021-075>.
Penalized smooth shift terms can be defined using 'mgcv'.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  scam
%global packver   1.2-20
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.20
Release:          1%{?dist}%{?buildtag}
Summary:          Shape Constrained Additive Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-mgcv >= 1.8.2
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-splines 
Requires:         R-CRAN-mgcv >= 1.8.2
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-Matrix 
Requires:         R-splines 

%description
Generalized additive models under shape constraints on the component
functions of the linear predictor. Models can include multiple
shape-constrained (univariate and bivariate) and unconstrained terms.
Routines of the package 'mgcv' are used to set up the model matrix, print,
and plot the results. Multiple smoothing parameter estimation by the
Generalized Cross Validation or similar. See Pya and Wood (2015)
<doi:10.1007/s11222-013-9448-7> for an overview. A broad selection of
shape-constrained smoothers, linear functionals of smooths with shape
constraints, and Gaussian models with AR1 residuals.

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

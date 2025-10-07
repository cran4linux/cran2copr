%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  quantregGrowth
%global packver   1.7-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.2
Release:          1%{?dist}%{?buildtag}
Summary:          Non-Crossing Additive Regression Quantiles and Non-Parametric Growth Charts

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-methods 
Requires:         R-CRAN-quantreg 
Requires:         R-splines 
Requires:         R-CRAN-SparseM 
Requires:         R-methods 

%description
Fits non-crossing regression quantiles as a function of linear covariates
and multiple smooth terms, including varying coefficients, via B-splines
with L1-norm difference penalties. Random intercepts and variable
selection are allowed via the lasso penalties. The smoothing parameters
are estimated as part of the model fitting, see Muggeo and others (2021)
<doi:10.1177/1471082X20929802>. Monotonicity and concavity constraints on
the fitted curves are allowed, see Muggeo and others (2013)
<doi:10.1007/s10651-012-0232-1>, and also
<doi:10.13140/RG.2.2.12924.85122> or <doi:10.13140/RG.2.2.29306.21445>
some code examples.

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

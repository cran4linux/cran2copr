%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fbrglm
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Safe Formula-Based Regularized Generalized Linear Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-glmnet 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-tibble 

%description
A formula-based wrapper around 'glmnet' that brings the 'glm()'-compatible
modeling workflow to regularized generalized linear models. Training-time
'terms', 'xlevels', and 'contrasts' are stored on the fit object and
reused at predict time, so the design matrix is reconstructed consistently
across sessions. Complete-case bookkeeping is exposed via 'nobs_info', and
linearly dependent columns are detected by a QR pivot and reported as 'NA'
in 'coef()' and 'summary()' (the 'stats::glm()' convention),
distinguishing "not identifiable" from "shrunk to zero by the penalty".
Novel factor levels at predict time raise the same error
'stats::predict.glm()' does by default, with 'on_new_levels = "na"' as a
production-style opt-in. Accepts character family strings ('gaussian',
'binomial', 'poisson', 'cox', 'multinomial', 'mgaussian') and any 'glm'
family object the underlying 'glmnet' itself accepts, including 'Gamma'
and fixed-theta negative binomial via 'MASS::negative.binomial'.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  powerutilities
%global packver   0.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Power Analysis for Linear and Generalized Linear Mixed Models

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmmTMB >= 1.1.14
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-pbkrtest 
BuildRequires:    R-CRAN-reformulas 
BuildRequires:    R-CRAN-retrodesign 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-glmmTMB >= 1.1.14
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-pbkrtest 
Requires:         R-CRAN-reformulas 
Requires:         R-CRAN-retrodesign 
Requires:         R-CRAN-rlang 

%description
Prospective power analysis and design planning using the "plug-in"
approach described by Piepho et al. (2022) <doi:10.1017/S0021859622000466>
and Stroup, Ptukhina and Garai (2024) <doi:10.1201/9780429092060-24>.
Expected treatment means and the proposed experimental design are encoded
in an artificial data set, and a model is "fit" to it with random effect
variances, correlations and residual dispersion fixed at user-specified
values rather than being estimated. The resulting standard errors are used
to compute the power of F-tests and user-defined contrasts, as well as
Type S (sign) and Type M (magnitude) error rates (Gelman and Carlin, 2014
<doi:10.1177/1745691614551642>). Models are fit with 'glmmTMB', so the
approach accommodates non-normal responses, heteroscedasticity, nested and
crossed random effects, correlated random slopes, and structured
covariances such as AR(1) and spatial correlation. Helper functions
convert standard deviations and correlations into the internal
parameterization of 'glmmTMB' and report the order in which random effect
parameters must be supplied. Denominator degrees of freedom can be
computed by the Kenward-Roger, residual or asymptotic methods (or can be
specified by users), and contrasts are specified through 'emmeans'.
Vignettes cover estimated marginal means, contrast specification, and
worked examples for common agricultural designs.

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

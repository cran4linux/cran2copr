%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  glm.predict
%global packver   4.3-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Predicted Values and Discrete Changes for Regression Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-AER 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-mlogit 
BuildRequires:    R-CRAN-dfidx 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-VGAM 
Requires:         R-stats 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-AER 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-MASS 
Requires:         R-parallel 
Requires:         R-CRAN-mlogit 
Requires:         R-CRAN-dfidx 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-VGAM 

%description
Functions to calculate predicted values and the difference between the two
cases with confidence interval for lm() [linear model], glm() [generalized
linear model], glm.nb() [negative binomial model], polr() [ordinal
logistic model], vglm() [generalized ordinal logistic model], multinom()
[multinomial model], tobit() [tobit model], svyglm() [survey-weighted
generalised linear models] and lmer() [linear multilevel models] using
Monte Carlo simulations or bootstrap. Reference: Bennet A. Zelner (2009)
<doi:10.1002/smj.783>.

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

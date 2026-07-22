%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  statwitness
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Model-Aware Validation and Audit Certificates for Statistical Analyses

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-reformulas 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
Requires:         R-graphics 
Requires:         R-CRAN-reformulas 
Requires:         R-stats 
Requires:         R-tools 

%description
Provides model-aware behavioral validation and audit certificates for
statistical analyses. Controlled transformations and model-specific
diagnostic checks are organized across five domains: computational
integrity, numerical stability, design adequacy, assumption screening, and
influence stability. Supported workflows include linear models,
generalized linear models, classical and repeated-measures analyses of
variance, mixed-effects models fitted using 'lme4' or 'glmmTMB', and
survival models fitted using 'survival'. Checks are selected according to
registered applicability conditions for each model class. The resulting
certificates describe computational behavior and selected diagnostic
findings; they do not establish causal validity, model correctness, or
scientific appropriateness.

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

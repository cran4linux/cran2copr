%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ccva
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Climate Change Vulnerability Assessment with Constrained Latent Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-lavaan >= 0.6.12
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-lavaan >= 0.6.12
Requires:         R-stats 
Requires:         R-utils 

%description
A general framework for climate change vulnerability assessment (CCVA) of
any species and any dataset. Variables are tagged as exposure, sensitivity
or adaptive capacity; each component is computed from its own predictors
by a chosen method; and the three components are combined into
vulnerability. Methods range from the rule-based framework of Foden et al.
(2013) <doi:10.1371/journal.pone.0065427> and the conventional weighted
index of Ofori et al. (2017) <doi:10.1038/s41598-017-13245-y> to
shape-constrained additive models ('scam'), latent-variable structural
equation models ('lavaan') in which vulnerability is inferred from
observable proxies, and penalised regression ('glmnet') for
high-dimensional predictors. Missing traits and outcomes are handled by
full-information maximum likelihood. Ecological knowledge enters as
explicit constraints on predictors, on each component's role and on the
links between components. Diagnostics, validation against observed
outcomes, bootstrap and weight-based uncertainty, calibrated risk
predictions and plots for every step are included.

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

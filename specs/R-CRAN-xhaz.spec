%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xhaz
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Excess Hazard Modelling Considering Inappropriate Mortality Rates

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mexhaz >= 2.6
BuildRequires:    R-CRAN-survival >= 2.6
BuildRequires:    R-CRAN-statmod >= 1.5.0
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-optimParallel 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-survexp.fr 
BuildRequires:    R-stats 
Requires:         R-CRAN-mexhaz >= 2.6
Requires:         R-CRAN-survival >= 2.6
Requires:         R-CRAN-statmod >= 1.5.0
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-optimParallel 
Requires:         R-splines 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-survexp.fr 
Requires:         R-stats 

%description
Fits relative survival regression models with or without proportional
excess hazards and with the additional possibility to correct for
background mortality by one or more parameter(s). These models are
relevant when the observed mortality in the studied group is not
comparable to that of the general population or in population-based
studies where the available life tables used for net survival estimation
are insufficiently stratified. In the latter case, the proposed model by
Touraine et al. (2020) <doi:10.1177/0962280218823234> can be used. The
user can also fit a model that relaxes the proportional expected hazards
assumption considered in the Touraine et al. excess hazard model. This
extension was proposed by Mba et al. (2020)
<doi:10.1186/s12874-020-01139-z> to allow non-proportional effects of the
additional variable on the general population mortality. In
non-population-based studies, researchers can identify non-comparability
source of bias in terms of expected mortality of selected individuals. An
excess hazard model correcting this selection bias is presented in
Goungounga et al. (2019) <doi:10.1186/s12874-019-0747-3>. This class of
model with a random effect at the cluster level on excess hazard is
presented in Goungounga et al. (2023) <doi:10.1002/bimj.202100210>.

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

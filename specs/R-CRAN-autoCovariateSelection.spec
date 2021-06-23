%global __brp_check_rpaths %{nil}
%global packname  autoCovariateSelection
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Covariate Selection Using HDPS Algorithm

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-data.table 

%description
Contains functions to implement automated covariate selection using
methods described in the high-dimensional propensity score (HDPS)
algorithm by Schneeweiss et.al. Covariate adjustment in
real-world-observational-data (RWD) is important for for estimating
adjusted outcomes and this can be done by using methods such as, but not
limited to, propensity score matching, propensity score weighting and
regression analysis. While these methods strive to statistically adjust
for confounding, the major challenge is in selecting the potential
covariates that can bias the outcomes comparison estimates in
observational RWD (Real-World-Data). This is where the utility of
automated covariate selection comes in. The functions in this package help
to implement the three major steps of automated covariate selection as
described by Schneeweiss et. al elsewhere. These three functions, in order
of the steps required to execute automated covariate selection are,
get_candidate_covariates(), get_recurrence_covariates() and
get_prioritised_covariates(). In addition to these functions, a sample
real-world-data from publicly available de-identified medical claims data
is also available for running examples and also for further exploration.
The original article where the algorithm is described by Schneeweiss
et.al. (2009) <doi:10.1097/EDE.0b013e3181a663cc> .

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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

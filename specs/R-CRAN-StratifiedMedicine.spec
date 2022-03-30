%global __brp_check_rpaths %{nil}
%global packname  StratifiedMedicine
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Stratified Medicine

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggparty 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-coin 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-partykit 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggparty 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-coin 

%description
A toolkit for stratified medicine, subgroup identification, and precision
medicine. Current tools include (1) filtering models (reduce covariate
space), (2) patient-level estimate models (counterfactual patient-level
quantities, such as the conditional average treatment effect), (3)
subgroup identification models (find subsets of patients with similar
treatment effects), and (4) treatment effect estimation and inference (for
the overall population and discovered subgroups). These tools can be
customized and are directly used in PRISM (patient response identifiers
for stratified medicine; Jemielita and Mehrotra 2019 <arXiv:1912.03337>.
This package is in beta and will be continually updated.

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

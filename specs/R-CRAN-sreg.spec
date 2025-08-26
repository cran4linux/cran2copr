%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sreg
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Stratified Randomized Experiments

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-viridis 

%description
Estimate average treatment effects (ATEs) in stratified randomized
experiments. `sreg` supports a wide range of stratification designs,
including matched pairs, n-tuple designs, and larger strata with many
units — possibly of unequal size across strata. 'sreg' is designed to
accommodate scenarios with multiple treatments and cluster-level treatment
assignments, and accommodates optimal linear covariate adjustment based on
baseline observable characteristics. 'sreg' computes estimators and
standard errors based on Bugni, Canay, Shaikh (2018)
<doi:10.1080/01621459.2017.1375934>; Bugni, Canay, Shaikh, Tabord-Meehan
(2024+) <doi:10.48550/arXiv.2204.08356>; Jiang, Linton, Tang, Zhang
(2023+) <doi:10.48550/arXiv.2201.13004>; Bai, Jiang, Romano, Shaikh, and
Zhang (2024) <doi:10.1016/j.jeconom.2024.105740>; Bai (2022)
<doi:10.1257/aer.20201856>; Bai, Romano, and Shaikh (2022)
<doi:10.1080/01621459.2021.1883437>; Liu (2024+)
<doi:10.48550/arXiv.2301.09016>; and Cytrynbaum (2024)
<doi:10.3982/QE2475>.

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

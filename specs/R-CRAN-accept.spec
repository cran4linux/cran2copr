%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  accept
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          The Acute COPD Exacerbation Prediction Tool (ACCEPT)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-CRAN-vetiver >= 0.2.1
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-reldist 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-hardhat 
BuildRequires:    R-CRAN-vctrs 
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-CRAN-vetiver >= 0.2.1
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-reldist 
Requires:         R-splines 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-hardhat 
Requires:         R-CRAN-vctrs 

%description
Allows clinicians to predict the rate and severity of future acute
exacerbation in Chronic Obstructive Pulmonary Disease (COPD) patients,
based on the clinical prediction models published in Adibi et al. (2020)
<doi:10.1016/S2213-2600(19)30397-2> and Safari et al. (2022)
<doi:10.1016/j.eclinm.2022.101574>.

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

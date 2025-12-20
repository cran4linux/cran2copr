%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ambiR
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate AZTI’s Marine Biotic Index

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-magrittr 
Requires:         R-utils 
Requires:         R-stats 

%description
Calculate AZTI’s Marine Biotic Index - AMBI. The included list of benthic
fauna species according to their sensitivity to pollution. Matching
species in sample data to the list allows the calculation of fractions of
individuals in the different sensitivity categories and thereafter the
AMBI index. The Shannon Diversity Index H' and the Danish benthic fauna
quality index DKI (Dansk Kvalitetsindeks) can also be calculated, as well
as the multivariate M-AMBI index. Borja, A., Franco, J. ,Pérez, V. (2000)
"A marine biotic index to establish the ecological quality of soft bottom
benthos within European estuarine and coastal environments"
<doi:10.1016/S0025-326X(00)00061-8>.

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

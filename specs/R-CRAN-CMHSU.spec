%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CMHSU
%global packver   0.0.6.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.6.9
Release:          1%{?dist}%{?buildtag}
Summary:          Mental Health Status, Substance Use Status and their Concurrent Status in North American Healthcare Administrative Databases

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
Patients' Mental Health (MH) status, Substance Use (SU) status, and
concurrent MH/SU status in the American/Canadian Healthcare Administrative
Databases can be identified. The detection is based on given parameters of
interest by clinicians including the list of plausible ICD MH/SU codes
(3/4/5 characters), the required number of visits of hospital for MH/SU ,
the required number of visits of service physicians for MH/SU, and the
maximum time span within MH visits, within SU visits, and, between MH and
SU visits. Methods are described in: Khan S
<https://pubmed.ncbi.nlm.nih.gov/29044442/>, Keen C, et al. (2021)
<doi:10.1111/add.15580>, Lavergne MR, et al. (2022)
<doi:10.1186/s12913-022-07759-z>, Casillas, S M, et al. (2022)
<doi:10.1016/j.abrep.2022.100464>, CIHI (2022) <https://www.cihi.ca/en>,
CDC (2024) <https://www.cdc.gov>, WHO (2019) <https://icd.who.int/en>.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sdtm.oak
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          SDTM Data Transformation Engine

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.2.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-tidyr >= 1.2.0
BuildRequires:    R-CRAN-admiraldev >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.0.2
BuildRequires:    R-CRAN-purrr >= 1.0.1
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-vctrs >= 0.5.0
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-pillar 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-tibble >= 3.2.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-tidyr >= 1.2.0
Requires:         R-CRAN-admiraldev >= 1.1.0
Requires:         R-CRAN-rlang >= 1.0.2
Requires:         R-CRAN-purrr >= 1.0.1
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-vctrs >= 0.5.0
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-pillar 
Requires:         R-CRAN-cli 

%description
An Electronic Data Capture system (EDC) and Data Standard agnostic
solution that enables the pharmaceutical programming community to develop
Clinical Data Interchange Standards Consortium (CDISC) Study Data
Tabulation Model (SDTM) datasets in R. The reusable algorithms concept in
'sdtm.oak' provides a framework for modular programming and can
potentially automate the conversion of raw clinical data to SDTM through
standardized SDTM specifications. SDTM is one of the required standards
for data submission to the Food and Drug Administration (FDA) in the
United States and Pharmaceuticals and Medical Devices Agency (PMDA) in
Japan. SDTM standards are implemented following the SDTM Implementation
Guide as defined by CDISC
<https://www.cdisc.org/standards/foundational/sdtmig>.

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

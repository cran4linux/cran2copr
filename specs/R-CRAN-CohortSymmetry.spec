%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CohortSymmetry
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Sequence Symmetry Analysis Using the Observational Medical Outcomes Partnership Common Data Model

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-CodelistGenerator >= 3.1.0
BuildRequires:    R-CRAN-CDMConnector >= 1.7.0
BuildRequires:    R-CRAN-PatientProfiles >= 1.0.0
BuildRequires:    R-CRAN-omopgenerics >= 1.0.0
BuildRequires:    R-CRAN-DrugUtilisation >= 0.7.0
BuildRequires:    R-CRAN-visOmopResults >= 0.4.0
BuildRequires:    R-CRAN-omock >= 0.3.1
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-here 
Requires:         R-CRAN-CodelistGenerator >= 3.1.0
Requires:         R-CRAN-CDMConnector >= 1.7.0
Requires:         R-CRAN-PatientProfiles >= 1.0.0
Requires:         R-CRAN-omopgenerics >= 1.0.0
Requires:         R-CRAN-DrugUtilisation >= 0.7.0
Requires:         R-CRAN-visOmopResults >= 0.4.0
Requires:         R-CRAN-omock >= 0.3.1
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-stats 
Requires:         R-CRAN-here 

%description
Calculating crude sequence ratio, adjusted sequence ratio and confidence
intervals using data mapped to the Observational Medical Outcomes
Partnership Common Data Model.

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

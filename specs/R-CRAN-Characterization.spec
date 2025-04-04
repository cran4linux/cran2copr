%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Characterization
%global packver   2.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Implement Descriptive Studies Using the Common Data Model

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DatabaseConnector >= 6.3.1
BuildRequires:    R-CRAN-FeatureExtraction >= 3.6.0
BuildRequires:    R-CRAN-ParallelLogger >= 3.0.0
BuildRequires:    R-CRAN-SqlRender >= 1.9.0
BuildRequires:    R-CRAN-Andromeda 
BuildRequires:    R-CRAN-ResultModelManager 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-DatabaseConnector >= 6.3.1
Requires:         R-CRAN-FeatureExtraction >= 3.6.0
Requires:         R-CRAN-ParallelLogger >= 3.0.0
Requires:         R-CRAN-SqlRender >= 1.9.0
Requires:         R-CRAN-Andromeda 
Requires:         R-CRAN-ResultModelManager 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rlang 

%description
An end-to-end framework that enables users to implement various
descriptive studies for a given set of target and outcome cohorts for data
mapped to the Observational Medical Outcomes Partnership Common Data
Model.

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

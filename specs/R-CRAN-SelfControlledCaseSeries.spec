%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SelfControlledCaseSeries
%global packver   6.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Self-Controlled Case Series

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-DatabaseConnector >= 6.0.0
BuildRequires:    R-CRAN-Cyclops >= 3.4.0
BuildRequires:    R-CRAN-ParallelLogger >= 3.4.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-SqlRender >= 1.16.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.9
BuildRequires:    R-CRAN-Andromeda >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-EmpiricalCalibration 
BuildRequires:    R-splines 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-ResultModelManager 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-DatabaseConnector >= 6.0.0
Requires:         R-CRAN-Cyclops >= 3.4.0
Requires:         R-CRAN-ParallelLogger >= 3.4.0
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-SqlRender >= 1.16.0
Requires:         R-CRAN-Rcpp >= 1.0.9
Requires:         R-CRAN-Andromeda >= 1.0.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-EmpiricalCalibration 
Requires:         R-splines 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-ResultModelManager 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-R6 

%description
Execute the self-controlled case series (SCCS) design using observational
data in the OMOP Common Data Model. Extracts all necessary data from the
database and transforms it to the format required for SCCS. Age and season
can be modeled using splines assuming constant hazard within calendar
months. Event-dependent censoring of the observation period can be
corrected for. Many exposures can be included at once (MSCCS), with
regularization on all coefficients except for the exposure of interest.
Includes diagnostics for all major assumptions of the SCCS.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FeatureExtraction
%global packver   3.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.7.2
Release:          1%{?dist}%{?buildtag}
Summary:          Generating Features for a Cohort

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DatabaseConnector >= 3.0.0
BuildRequires:    R-CRAN-ParallelLogger >= 2.0.2
BuildRequires:    R-CRAN-SqlRender >= 1.18.0
BuildRequires:    R-CRAN-Andromeda 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-pillar 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-checkmate 
Requires:         R-CRAN-DatabaseConnector >= 3.0.0
Requires:         R-CRAN-ParallelLogger >= 2.0.2
Requires:         R-CRAN-SqlRender >= 1.18.0
Requires:         R-CRAN-Andromeda 
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-pillar 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-checkmate 

%description
An R interface for generating features for a cohort using data in the
Common Data Model. Features can be constructed using default or custom
made feature definitions. Furthermore it's possible to aggregate features
and get the summary statistics.

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

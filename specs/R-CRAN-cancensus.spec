%global __brp_check_rpaths %{nil}
%global packname  cancensus
%global packver   0.4.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.8
Release:          1%{?dist}%{?buildtag}
Summary:          Access, Retrieve, and Work with Canadian Census Data and Geography

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.0.0
BuildRequires:    R-CRAN-jsonlite >= 1.0
BuildRequires:    R-CRAN-dplyr >= 0.7
BuildRequires:    R-CRAN-digest >= 0.1
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-httr >= 1.0.0
Requires:         R-CRAN-jsonlite >= 1.0
Requires:         R-CRAN-dplyr >= 0.7
Requires:         R-CRAN-digest >= 0.1
Requires:         R-CRAN-rlang 

%description
Integrated, convenient, and uniform access to Canadian Census data and
geography retrieved using the 'CensusMapper' API. This package produces
analysis-ready tidy data frames and spatial data in multiple formats, as
well as convenience functions for working with Census variables, variable
hierarchies, and region selection. API keys are freely available with free
registration at <https://censusmapper.ca/api>. Census data and boundary
geometries are reproduced and distributed on an "as is" basis with the
permission of Statistics Canada (Statistics Canada 2001; 2006; 2011;
2016).

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

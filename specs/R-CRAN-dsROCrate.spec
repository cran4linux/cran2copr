%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dsROCrate
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          'DataSHIELD' RO-Crate Governance Functions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rocrateR >= 0.1.0
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DSMolgenisArmadillo 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-opalr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-RcppTOML 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-vtree 
BuildRequires:    R-CRAN-xptr 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-rocrateR >= 0.1.0
Requires:         R-CRAN-digest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DSMolgenisArmadillo 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-opalr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-RcppTOML 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-vtree 
Requires:         R-CRAN-xptr 
Requires:         R-CRAN-yaml 

%description
Tools for wrapping 'DataSHIELD' analyses into RO-Crate (Research Object
Crate) objects. Provides functions to create structured metadata for
federated data analysis projects, enabling governance tracking of data
access, project membership, analysis execution and output validation
across distributed data sources.

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

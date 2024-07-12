%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  genieBPC
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Project GENIE BioPharma Collaborative Data Processing Pipeline

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.1.2
BuildRequires:    R-CRAN-cli >= 2.5.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-dtplyr >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.6
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-sunburstR 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-tibble >= 3.1.2
Requires:         R-CRAN-cli >= 2.5.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-dtplyr >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.6
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-sunburstR 
Requires:         R-CRAN-tidyr 

%description
The American Association Research (AACR) Project Genomics Evidence
Neoplasia Information Exchange (GENIE) BioPharma Collaborative represents
a multi-year, multi-institution effort to build a pan-cancer repository of
linked clinico-genomic data. The genomic and clinical data are provided in
multiple releases (separate releases for each cancer cohort with updates
following data corrections), which are stored on the data sharing platform
'Synapse' <https://www.synapse.org/>. The 'genieBPC' package provides a
seamless way to obtain the data corresponding to each release from
'Synapse' and to prepare datasets for analysis.

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

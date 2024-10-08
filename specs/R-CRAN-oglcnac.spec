%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  oglcnac
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Processing and Analysis of O-GlcNAcAtlas Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-glue 

%description
Provides tools for processing and analyzing data from the 'O-GlcNAcAtlas'
database <https://oglcnac.org/>, as described in Ma (2021)
<doi:10.1093/glycob/cwab003>. It integrates 'UniProt'
<https://www.uniprot.org/> API calls to retrieve additional information.
It is specifically designed for research workflows involving
'O-GlcNAcAtlas' data, providing a flexible and user-friendly interface for
customizing and downloading processed results. Interactive elements allow
users to easily adjust parameters and handle various biological datasets.

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

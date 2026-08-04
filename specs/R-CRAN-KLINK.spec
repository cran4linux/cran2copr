%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  KLINK
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Kinship Analysis with Linked Markers

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-pedtools >= 2.11.0
BuildRequires:    R-CRAN-forrel >= 1.9.0
BuildRequires:    R-CRAN-shiny >= 1.9.0
BuildRequires:    R-CRAN-pedprobr >= 1.1.0
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-CRAN-norSTR 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-pedFamilias 
BuildRequires:    R-CRAN-pedmut 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-verbalisr 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-pedtools >= 2.11.0
Requires:         R-CRAN-forrel >= 1.9.0
Requires:         R-CRAN-shiny >= 1.9.0
Requires:         R-CRAN-pedprobr >= 1.1.0
Requires:         R-CRAN-gt 
Requires:         R-CRAN-norSTR 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-pedFamilias 
Requires:         R-CRAN-pedmut 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-verbalisr 
Requires:         R-CRAN-xml2 

%description
A 'shiny' application for forensic kinship testing, based on the
'pedsuite' R packages. 'KLINK' is closely aligned with the (non-R)
software 'Familias' and 'FamLink', but offers several unique features,
including visualisations and automated report generation. The calculation
of likelihood ratios supports pairs of linked markers, and all common
mutation models. The program is described in Vigeland and Gilfillan (2026)
<doi:10.1016/j.fsigen.2026.103578>.

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

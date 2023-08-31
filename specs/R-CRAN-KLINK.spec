%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  KLINK
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Kinship Analysis with Linked Markers

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-pedtools >= 2.3.1
BuildRequires:    R-CRAN-shiny >= 1.7.4
BuildRequires:    R-CRAN-forrel >= 1.5.3
BuildRequires:    R-CRAN-gt >= 0.9.0
BuildRequires:    R-CRAN-pedprobr >= 0.8.0
BuildRequires:    R-CRAN-pedmut >= 0.6.0
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-pkgload 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-verbalisr 
Requires:         R-CRAN-pedtools >= 2.3.1
Requires:         R-CRAN-shiny >= 1.7.4
Requires:         R-CRAN-forrel >= 1.5.3
Requires:         R-CRAN-gt >= 0.9.0
Requires:         R-CRAN-pedprobr >= 0.8.0
Requires:         R-CRAN-pedmut >= 0.6.0
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-pkgload 
Requires:         R-CRAN-shinydashboard 
Requires:         R-utils 
Requires:         R-CRAN-verbalisr 

%description
A 'shiny' application for forensic kinship testing, based on the
'pedsuite' R packages. 'KLINK' is closely aligned with the (non-R)
software 'Familias' and 'FamLink', but offers several unique features,
including visualisations and automated report generation. The calculation
of likelihood ratios supports pairs of linked markers, and all common
mutation models.

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

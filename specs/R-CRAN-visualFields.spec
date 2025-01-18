%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  visualFields
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Methods for Visual Fields

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-polyclip 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-oro.dicom 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-htmlTable 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-polyclip 
Requires:         R-CRAN-deldir 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-oro.dicom 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-htmlTable 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-pracma 

%description
A collection of tools for analyzing the field of vision. It provides a
framework for development and use of innovative methods for visualization,
statistical analysis, and clinical interpretation of visual-field loss and
its change over time. It is intended to be a tool for collaborative
research. The package is described in Marin-Franch and Swanson (2013)
<doi:10.1167/13.4.10> and is part of the Open Perimetry Initiative (OPI)
[Turpin, Artes, and McKendrick (2012) <doi:10.1167/12.11.22>].

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

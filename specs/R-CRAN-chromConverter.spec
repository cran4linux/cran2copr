%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  chromConverter
%global packver   0.7.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.5
Release:          1%{?dist}%{?buildtag}
Summary:          Chromatographic File Converter

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate >= 1.41.0
BuildRequires:    R-CRAN-bitops 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RaMS 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-reticulate >= 1.41.0
Requires:         R-CRAN-bitops 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-RaMS 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-digest 

%description
Reads chromatograms from binary formats into R objects. Currently supports
conversion of 'Agilent ChemStation', 'Agilent MassHunter', 'Shimadzu
LabSolutions', 'ThermoRaw', and 'Varian Workstation' files as well as
various text-based formats. In addition to its internal parsers,
chromConverter contains bindings to parsers in external libraries, such as
'Aston' <https://github.com/bovee/aston>, 'Entab'
<https://github.com/bovee/entab>, 'rainbow'
<https://rainbow-api.readthedocs.io/>, and 'ThermoRawFileParser'
<https://github.com/compomics/ThermoRawFileParser>.

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

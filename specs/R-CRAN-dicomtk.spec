%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dicomtk
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Comprehensive 'DICOM' Toolkit for Medical Imaging

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-jsonlite >= 1.8.0
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-jsonlite >= 1.8.0
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-tools 

%description
A comprehensive R interface to the 'DICOM' Toolkit ('DCMTK'), providing
native R bindings for reading, writing, modifying, and visualizing Digital
Imaging and Communications in Medicine ('DICOM') files. Features include
'tidyverse'-compliant data structures, 'ggplot2'-based image
visualization, interactive 'Shiny' viewers, 'PACS' networking (C-ECHO,
C-FIND, C-STORE, C-MOVE), structured report handling, 'DICOM'
deidentification, and integration with local and cloud-based large
language models ('LLM') via 'Ollama' and 'OpenAI'-compatible APIs for
AI-assisted medical image analysis. The 'DCMTK' C++ library is bundled and
compiled from source, requiring no external installation.

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

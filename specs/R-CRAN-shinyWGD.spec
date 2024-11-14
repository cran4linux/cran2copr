%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shinyWGD
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          'Shiny' Application for Whole Genome Duplication Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyalert 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-vroom 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-seqinr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyalert 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-vroom 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-seqinr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 

%description
Provides a comprehensive 'Shiny' application for analyzing Whole Genome
Duplication ('WGD') events. This package provides a user-friendly 'Shiny'
web application for non-experienced researchers to prepare input data and
execute command lines for several well-known 'WGD' analysis tools,
including 'wgd', 'ksrates', 'i-ADHoRe', 'OrthoFinder', and 'Whale'. This
package also provides the source code for experienced researchers to
adjust and install the package to their own server. Key Features 1) Input
Data Preparation This package allows users to conveniently upload and
format their data, making it compatible with various 'WGD' analysis tools.
2) Command Line Generation This package automatically generates the
necessary command lines for selected 'WGD' analysis tools, reducing manual
errors and saving time. 3) Visualization This package offers interactive
visualizations to explore and interpret 'WGD' results, facilitating
in-depth 'WGD' analysis. 4) Comparative Genomics Users can study and
compare 'WGD' events across different species, aiding in evolutionary and
comparative genomics studies. 5) User-Friendly Interface This 'Shiny' web
application provides an intuitive and accessible interface, making 'WGD'
analysis accessible to researchers and 'bioinformaticians' of all levels.

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

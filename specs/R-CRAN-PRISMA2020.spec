%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PRISMA2020
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Make Interactive 'PRISMA' Flow Diagrams

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-DiagrammeR 
BuildRequires:    R-CRAN-DiagrammeRsvg 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-rsvg 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-webp 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-rio 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-zip 
Requires:         R-CRAN-DiagrammeR 
Requires:         R-CRAN-DiagrammeRsvg 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-rsvg 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-webp 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-rio 
Requires:         R-tools 
Requires:         R-CRAN-zip 

%description
Systematic reviews should be described in a high degree of methodological
detail. The 'PRISMA' Statement calls for a high level of reporting detail
in systematic reviews and meta-analyses. An integral part of the
methodological description of a review is a flow diagram. This package
produces an interactive flow diagram that conforms to the 'PRISMA2020'
preprint. When made interactive, the reader/user can click on each box and
be directed to another website or file online (e.g. a detailed description
of the screening methods, or a list of excluded full texts), with a
mouse-over tool tip that describes the information linked to in more
detail. Interactive versions can be saved as HTML files, whilst static
versions for inclusion in manuscripts can be saved as HTML, PDF, PNG, SVG,
PS or WEBP files.

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

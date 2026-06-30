%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mapsf.gui
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Create Thematic Maps Interactively

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shinyjs >= 2.0.0
BuildRequires:    R-CRAN-mapsf >= 1.2.1
BuildRequires:    R-CRAN-shiny >= 1.12.0
BuildRequires:    R-CRAN-bslib >= 0.10.0
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-Ckmeans.1d.dp 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-formatR 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-phosphoricons 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-shiny.i18n 
BuildRequires:    R-CRAN-sortable 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-shinyjs >= 2.0.0
Requires:         R-CRAN-mapsf >= 1.2.1
Requires:         R-CRAN-shiny >= 1.12.0
Requires:         R-CRAN-bslib >= 0.10.0
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-Ckmeans.1d.dp 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-formatR 
Requires:         R-CRAN-jpeg 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-phosphoricons 
Requires:         R-CRAN-png 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-shiny.i18n 
Requires:         R-CRAN-sortable 
Requires:         R-stats 
Requires:         R-utils 

%description
A 'Shiny' application to create thematic maps interactively, based on the
'mapsf' package. Features include: a user-friendly interface to create and
customize thematic maps without coding, support for various map types
(choropleth, proportional symbols, etc.) and customization options
(colors, legends, etc.), R code generation to ensure reproducibility and
export options to save maps in different formats (PNG, SVG).

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

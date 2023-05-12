%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SEAHORS
%global packver   1.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Exploration of ArcHaeological Objects in R Shiny

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-htmlwidgets 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-htmlwidgets 

%description
An R 'Shiny' application dedicated to the intra-site spatial analysis of
piece-plotted archaeological remains, making the two and three-dimensional
spatial exploration of archaeological data as user-friendly as possible.
Documentation about 'SEAHORS' is provided by the vignette included in this
package and by the companion scientific paper: Royer, Discamps, Plutniak,
Thomas (2023, PCI Archaeology, <doi:10.5281/zenodo.7674698>).

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

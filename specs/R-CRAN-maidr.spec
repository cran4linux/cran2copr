%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  maidr
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Multimodal Access and Interactive Data Representation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggplotify 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridSVG 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggplotify 
Requires:         R-grid 
Requires:         R-CRAN-gridSVG 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-R6 

%description
Provides accessible, interactive visualizations through the 'MAIDR'
(Multimodal Access and Interactive Data Representation) system. Converts
'ggplot2' and Base R plots into accessible HTML/SVG formats with keyboard
navigation, screen reader support, and 'sonification' capabilities.
Supports bar charts (simple, grouped, stacked), histograms, line plots,
scatter plots, box plots, heat maps, density/smooth curves, faceted plots,
multi-panel layouts (including patchwork), and multi-layered plot
combinations. Enables data exploration for users with visual impairments
through multiple sensory modalities. For more details see the 'MAIDR'
project <https://maidr.ai/>.

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

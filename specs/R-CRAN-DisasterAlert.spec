%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DisasterAlert
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Disaster Alert and Sentiment Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-wordcloud 
BuildRequires:    R-CRAN-textdata 
BuildRequires:    R-CRAN-tidytext 
BuildRequires:    R-CRAN-quanteda 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-DT 
Requires:         R-methods 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-wordcloud 
Requires:         R-CRAN-textdata 
Requires:         R-CRAN-tidytext 
Requires:         R-CRAN-quanteda 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-DT 

%description
By systematically aggregating and processing textual reports from
earthquakes, floods, storms, wildfires, and other natural disasters, the
framework enables a holistic assessment of crisis narratives. Intelligent
cleaning and normalization techniques transform raw commentary into
structured data, ensuring precise extraction of disaster-specific
insights. Collective sentiments of affected communities are quantitatively
scored and qualitatively categorized, providing a multifaceted view of
societal responses under duress. Interactive geographic maps and temporal
charts illustrate the evolution and spatial dispersion of emotional
reactions and impact indicators.

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

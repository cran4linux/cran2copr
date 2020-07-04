%global packname  oceanis
%global packver   1.7.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.4
Release:          1%{?dist}
Summary:          Cartography for Statistical Analysis

License:          GPL (>= 2.0) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-utils >= 3.3.3
BuildRequires:    R-grDevices >= 3.3.3
BuildRequires:    R-graphics >= 3.3.3
BuildRequires:    R-CRAN-ggplot2 >= 3.2.0
BuildRequires:    R-CRAN-mapview >= 2.7.0
BuildRequires:    R-CRAN-leaflet >= 2.0.3
BuildRequires:    R-CRAN-shiny >= 1.4.0.2
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-shinythemes >= 1.1.2
BuildRequires:    R-CRAN-shinyjs >= 1.1
BuildRequires:    R-CRAN-leaflet.extras >= 1.0.0
BuildRequires:    R-CRAN-sf >= 0.9.0
BuildRequires:    R-CRAN-dplyr >= 0.8.4
BuildRequires:    R-CRAN-shinyBS >= 0.61
BuildRequires:    R-CRAN-units >= 0.6.5
BuildRequires:    R-CRAN-classInt >= 0.4.2
BuildRequires:    R-CRAN-lwgeom >= 0.2.1
BuildRequires:    R-CRAN-DT >= 0.12
Requires:         R-utils >= 3.3.3
Requires:         R-grDevices >= 3.3.3
Requires:         R-graphics >= 3.3.3
Requires:         R-CRAN-ggplot2 >= 3.2.0
Requires:         R-CRAN-mapview >= 2.7.0
Requires:         R-CRAN-leaflet >= 2.0.3
Requires:         R-CRAN-shiny >= 1.4.0.2
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-shinythemes >= 1.1.2
Requires:         R-CRAN-shinyjs >= 1.1
Requires:         R-CRAN-leaflet.extras >= 1.0.0
Requires:         R-CRAN-sf >= 0.9.0
Requires:         R-CRAN-dplyr >= 0.8.4
Requires:         R-CRAN-shinyBS >= 0.61
Requires:         R-CRAN-units >= 0.6.5
Requires:         R-CRAN-classInt >= 0.4.2
Requires:         R-CRAN-lwgeom >= 0.2.1
Requires:         R-CRAN-DT >= 0.12

%description
Creating maps for statistical analysis such as proportional circles,
chroropleth, typology and flows. Some functions use 'shiny' or 'leaflet'
technologies for dynamism and interactivity. The great features are : -
Create maps in a web environment where the parameters are modifiable on
the fly ('shiny' and 'leaflet' technology). - Create interactive maps
through zoom and pop-up ('leaflet' technology). - Create frozen maps with
the possibility to add labels.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}

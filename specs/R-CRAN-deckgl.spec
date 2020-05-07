%global packname  deckgl
%global packver   0.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.7
Release:          1%{?dist}
Summary:          An R Interface to 'deck.gl'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-tibble 

%description
Makes 'deck.gl' <https://deck.gl/>, a WebGL-powered open-source JavaScript
framework for visual exploratory data analysis of large datasets,
available within R via the 'htmlwidgets' package. Furthermore, it supports
basemaps from 'mapbox' <https://www.mapbox.com/> via 'mapbox-gl-js'
<https://github.com/mapbox/mapbox-gl-js>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/htmlwidgets
%doc %{rlibdir}/%{packname}/icons
%{rlibdir}/%{packname}/sample-data
%{rlibdir}/%{packname}/INDEX

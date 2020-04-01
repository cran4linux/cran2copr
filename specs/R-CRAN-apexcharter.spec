%global packname  apexcharter
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          Create Interactive Chart with the JavaScript 'ApexCharts'Library

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.1.0
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-shiny >= 1.1.0
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-jsonlite 

%description
Provides an 'htmlwidgets' interface to 'apexcharts.js'. 'Apexcharts' is a
modern JavaScript charting library to build interactive charts and
visualizations with simple API. 'Apexcharts' examples and documentation
are available here: <https://apexcharts.com/>.

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
%doc %{rlibdir}/%{packname}/examples-input
%doc %{rlibdir}/%{packname}/examples-proxy
%{rlibdir}/%{packname}/htmlwidgets
%{rlibdir}/%{packname}/INDEX

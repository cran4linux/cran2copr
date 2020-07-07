%global packname  RLumShiny
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          3%{?dist}
Summary:          'Shiny' Applications for the R Package 'Luminescence'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-knitr >= 1.20
BuildRequires:    R-CRAN-rmarkdown >= 1.11
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-CRAN-shiny >= 1.1.0
BuildRequires:    R-CRAN-readxl >= 1.1.0
BuildRequires:    R-CRAN-shinyjs >= 1.0
BuildRequires:    R-CRAN-Luminescence >= 0.8.5
BuildRequires:    R-CRAN-shinydashboard >= 0.7.0
BuildRequires:    R-CRAN-googleVis >= 0.6.2
BuildRequires:    R-CRAN-DT >= 0.4
BuildRequires:    R-CRAN-rhandsontable >= 0.3.4
BuildRequires:    R-CRAN-RCarb >= 0.1.0
Requires:         R-CRAN-knitr >= 1.20
Requires:         R-CRAN-rmarkdown >= 1.11
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-shiny >= 1.1.0
Requires:         R-CRAN-readxl >= 1.1.0
Requires:         R-CRAN-shinyjs >= 1.0
Requires:         R-CRAN-Luminescence >= 0.8.5
Requires:         R-CRAN-shinydashboard >= 0.7.0
Requires:         R-CRAN-googleVis >= 0.6.2
Requires:         R-CRAN-DT >= 0.4
Requires:         R-CRAN-rhandsontable >= 0.3.4
Requires:         R-CRAN-RCarb >= 0.1.0

%description
A collection of 'shiny' applications for the R package 'Luminescence'.
These mainly, but not exclusively, include applications for plotting
chronometric data from e.g. luminescence or radiocarbon dating. It further
provides access to bootstraps tooltip and popover functionality and
contains the 'jscolor.js' library with a custom 'shiny' output binding.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/shiny
%doc %{rlibdir}/%{packname}/www
%{rlibdir}/%{packname}/INDEX

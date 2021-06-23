%global __brp_check_rpaths %{nil}
%global packname  EventDetectGUI
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Graphical User Interface for the 'EventDetectR' Package

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-EventDetectR 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-EventDetectR 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-plotly 
Requires:         R-tools 
Requires:         R-CRAN-DT 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 

%description
A graphical user interface for open source event detection.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/app.R
%doc %{rlibdir}/%{packname}/appTests
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/config.xml
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX

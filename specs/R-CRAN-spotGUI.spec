%global packname  spotGUI
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          Graphical User Interface for the Package 'SPOT'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-SPOT >= 2.0.3
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-smoof 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-rhandsontable 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-rclipboard 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-httpuv 
BuildRequires:    R-methods 
Requires:         R-CRAN-SPOT >= 2.0.3
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-smoof 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-rhandsontable 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-rclipboard 
Requires:         R-CRAN-plotly 
Requires:         R-tools 
Requires:         R-CRAN-httpuv 
Requires:         R-methods 

%description
A graphical user interface for the Sequential Parameter Optimization
Toolbox (package 'SPOT'). It includes a quick, graphical setup for spot,
interactive 3D plots, export possibilities and more.

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
%doc %{rlibdir}/%{packname}/app.R
%doc %{rlibdir}/%{packname}/config.xml
%{rlibdir}/%{packname}/INDEX

%global __brp_check_rpaths %{nil}
%global packname  eAnalytics
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          3%{?dist}%{?buildtag}
Summary:          Dynamic Web-Based Analytics for the Energy Industry

License:          Apache License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.5.2
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-energyr 
BuildRequires:    R-CRAN-googleVis 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinytest 
BuildRequires:    R-CRAN-shinyWidgets 
Requires:         R-CRAN-plotly >= 4.5.2
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-energyr 
Requires:         R-CRAN-googleVis 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinytest 
Requires:         R-CRAN-shinyWidgets 

%description
A 'Shiny' web application for energy industry analytics. Take an overview
of the industry, measure Key Performance Indicators, identify changes in
the industry over time, and discover new relationships in the data.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}

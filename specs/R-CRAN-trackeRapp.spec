%global packname  trackeRapp
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Interface for the Analysis of Running, Cycling and Swimming Datafrom GPS-Enabled Tracking Devices

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-trackeR >= 1.5.0
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-changepoint 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-mapdeck 
BuildRequires:    R-CRAN-V8 
Requires:         R-CRAN-trackeR >= 1.5.0
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-foreach 
Requires:         R-mgcv 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-changepoint 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-mapdeck 
Requires:         R-CRAN-V8 

%description
Provides an integrated user interface and workflow for the analysis of
running, cycling and swimming data from GPS-enabled tracking devices
through the 'trackeR' <https://CRAN.R-project.org/package=trackeR> R
package.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX

%global packname  shinyML
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Compare H20 or Spark Supervised Regression Models Using ShinyApp

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.0.3
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-h2o 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-dygraphs 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-sparklyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-shinycssloaders 
Requires:         R-CRAN-shiny >= 1.0.3
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-h2o 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-dygraphs 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-sparklyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-shinycssloaders 

%description
Implementation of a shiny app to easily compare supervised regression
model performances. You provide the data and configure each model
parameter directly on the shiny app. Four main supervised learning
algorithms can be tested either on Spark or H2O frameworks to suit your
regression problem on a given time series. Implementation of these time
series forecasting methods on R has been done by Shmueli and Lichtendahl
(2015, ISBN:0991576632).

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

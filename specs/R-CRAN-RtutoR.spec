%global packname  RtutoR
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Shiny Apps for Plotting and Exploratory Analysis

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-FSelector 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-devtools 
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-FSelector 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-devtools 

%description
Contains Shiny apps for Plotting and Exploratory Analysis. The plotting
app provides an automated interface for generating plots using the
'ggplot2' package. Current version of this app supports 10 different plot
types along with options to manipulate specific aesthetics and controls
related to each plot type. Exploratory Analysis app helps generates an
Exploratory analysis report (in PowerPoint format) comprising of
Univariate and Bivariate plots & related summary tables.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/ReadMe_Plotter.rmd
%doc %{rlibdir}/%{packname}/ReadMe_ppt_app.rmd
%{rlibdir}/%{packname}/INDEX

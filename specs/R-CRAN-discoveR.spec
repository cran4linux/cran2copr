%global packname  discoveR
%global packver   1.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          1%{?dist}
Summary:          Exploratory Data Analysis System

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinydashboardPlus 
BuildRequires:    R-CRAN-shinyAce 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-factoextra 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-zip 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinydashboardPlus 
Requires:         R-CRAN-shinyAce 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-factoextra 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-zip 

%description
Performs an exploratory data analysis through a 'shiny' interface. It
includes basic methods such as the mean, median, mode, normality test,
among others. It also includes clustering techniques such as Principal
Components Analysis, Hierarchical Clustering and the K-Means Method.

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
%doc %{rlibdir}/%{packname}/application
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX

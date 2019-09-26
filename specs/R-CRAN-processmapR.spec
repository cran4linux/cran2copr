%global packname  processmapR
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}
Summary:          Construct Process Maps Using Event Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-DiagrammeR >= 1.0.0
BuildRequires:    R-CRAN-edeaR >= 0.8.0
BuildRequires:    R-CRAN-bupaR >= 0.4.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-hms 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-DiagrammeR >= 1.0.0
Requires:         R-CRAN-edeaR >= 0.8.0
Requires:         R-CRAN-bupaR >= 0.4.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-hms 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tidyr 

%description
Visualize of process maps based on event logs, in the form of directed
graphs. Part of the 'bupaR' framework.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

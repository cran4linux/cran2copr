%global packname  shinyHeatmaply
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Deploy 'heatmaply' using 'shiny'

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.3.0
Requires:         R-core >= 2.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-heatmaply 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-htmlwidgets 
Requires:         R-CRAN-heatmaply 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-readxl 
Requires:         R-utils 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-htmlwidgets 

%description
Access functionality of the 'heatmaply' package through 'Shiny UI'.

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
%doc %{rlibdir}/%{packname}/example
%doc %{rlibdir}/%{packname}/shinyapp
%{rlibdir}/%{packname}/INDEX

%global packname  shinyHeatmaply
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          2%{?dist}
Summary:          Deploy 'heatmaply' using 'shiny'

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.3.0
Requires:         R-core >= 2.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-heatmaply >= 1.0.0
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-readxl 
Requires:         R-CRAN-heatmaply >= 1.0.0
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-CRAN-xtable 
Requires:         R-tools 
Requires:         R-CRAN-rmarkdown 
Requires:         R-utils 
Requires:         R-CRAN-readxl 

%description
Access functionality of the 'heatmaply' package through 'Shiny UI'.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/example
%doc %{rlibdir}/%{packname}/shinyapp
%{rlibdir}/%{packname}/INDEX

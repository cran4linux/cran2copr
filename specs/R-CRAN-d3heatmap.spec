%global packname  d3heatmap
%global packver   0.6.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1.2
Release:          1%{?dist}
Summary:          Interactive Heat Maps Using 'htmlwidgets' and 'D3.js'

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-scales >= 0.2.5
BuildRequires:    R-CRAN-dendextend >= 0.18.0
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-scales >= 0.2.5
Requires:         R-CRAN-dendextend >= 0.18.0
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-png 
Requires:         R-CRAN-base64enc 
Requires:         R-stats 
Requires:         R-grDevices 

%description
Create interactive heat maps that are usable from the R console, in the
'RStudio' viewer pane, in 'R Markdown' documents, and in 'Shiny' apps.
Hover the mouse pointer over a cell to show details, drag a rectangle to
zoom, and click row/column labels to highlight.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/htmlwidgets
%doc %{rlibdir}/%{packname}/www
%{rlibdir}/%{packname}/INDEX

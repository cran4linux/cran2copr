%global packname  bdchecks
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          3%{?dist}%{?buildtag}
Summary:          Biodiversity Data Checks

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-bdDwC 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-finch 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rgbif 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-spocc 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-bdDwC 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-finch 
Requires:         R-methods 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rgbif 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-spocc 
Requires:         R-CRAN-yaml 

%description
Supplies a Shiny app and a set of functions to perform and managing data
checks for biodiversity data.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX

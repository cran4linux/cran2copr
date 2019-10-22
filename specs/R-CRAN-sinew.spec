%global packname  sinew
%global packver   0.3.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.8
Release:          1%{?dist}
Summary:          Create 'roxygen2' Skeleton with Information from Function Script

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.3.0
Requires:         R-core >= 2.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-sos 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-rematch2 
Requires:         R-CRAN-rstudioapi 
Requires:         R-utils 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-miniUI 
Requires:         R-tools 
Requires:         R-CRAN-sos 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-rematch2 

%description
Create 'roxygen2' skeleton populated with information scraped from the
within the function script. Also creates field entries for imports in the
'DESCRIPTION' and import in the 'NAMESPACE' files. Can be run from the R
console or through the 'RStudio' 'addin' menu.

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
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX

%global packname  sigmajs
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          2%{?dist}
Summary:          Interface to 'Sigma.js' Graph Visualization Library

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-crosstalk 
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-crosstalk 

%description
Interface to 'sigma.js' graph visualization library including animations,
plugins and shiny proxies.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/htmlwidgets
%{rlibdir}/%{packname}/INDEX

%global packname  shiny.semantic
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          Semantic UI Support for Shiny

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlwidgets >= 0.8
BuildRequires:    R-CRAN-htmltools >= 0.2.6
BuildRequires:    R-CRAN-purrr >= 0.2.2
BuildRequires:    R-CRAN-shiny >= 0.12.1
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-htmlwidgets >= 0.8
Requires:         R-CRAN-htmltools >= 0.2.6
Requires:         R-CRAN-purrr >= 0.2.2
Requires:         R-CRAN-shiny >= 0.12.1
Requires:         R-utils 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-jsonlite 

%description
Creating a great user interface for your Shiny apps can be a hassle,
especially if you want to work purely in R and don't want to use, for
instance HTML templates. This package adds support for a powerful UI
library Semantic UI - <http://semantic-ui.com/>. It also supports
universal UI input binding that works with various DOM elements.

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
%doc %{rlibdir}/%{packname}/assets
%doc %{rlibdir}/%{packname}/htmlwidgets
%doc %{rlibdir}/%{packname}/prepare_package_cran.sh
%doc %{rlibdir}/%{packname}/semantic-range
%doc %{rlibdir}/%{packname}/www
%{rlibdir}/%{packname}/INDEX

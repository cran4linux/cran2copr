%global packname  cartools
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Tools for Understanding Highway Performance

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-animation 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gapminder 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-roxygen2 
BuildRequires:    R-CRAN-sde 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-utils 
Requires:         R-CRAN-animation 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gapminder 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-roxygen2 
Requires:         R-CRAN-sde 
Requires:         R-CRAN-shiny 
Requires:         R-stats 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-usethis 
Requires:         R-utils 

%description
Analytical tools are designed to help people understand the complex
relationships associated with freeway performance and traffic breakdown.
Emphasis is placed on: (1) Traffic noise or volatility; (2) Driver
behavior and safety; and (3) Stochastic modeling, models that explain
breakdown and performance.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

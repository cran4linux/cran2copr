%global packname  moderndive
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          3%{?dist}
Summary:          Tidyverse-Friendly Introductory Linear Regression

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-broom >= 0.4.3
BuildRequires:    R-CRAN-rlang >= 0.2.0
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-infer 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-broom >= 0.4.3
Requires:         R-CRAN-rlang >= 0.2.0
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-formula.tools 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-infer 
Requires:         R-CRAN-glue 

%description
Datasets and wrapper functions for tidyverse-friendly introductory linear
regression, used in "Statistical Inference via Data Science: A ModernDive
into R and the Tidyverse" available at <https://moderndive.com/>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

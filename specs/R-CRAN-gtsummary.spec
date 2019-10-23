%global packname  gtsummary
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          Presentation-Ready Data Summary and Analytic Result Tables

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 2.0.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-glue >= 1.3.0
BuildRequires:    R-CRAN-knitr >= 1.21
BuildRequires:    R-CRAN-tidyr >= 0.8.2
BuildRequires:    R-CRAN-dplyr >= 0.7.8
BuildRequires:    R-CRAN-broom >= 0.5.1
BuildRequires:    R-CRAN-rlang >= 0.3.1
BuildRequires:    R-CRAN-purrr >= 0.3.0
BuildRequires:    R-CRAN-tidyselect >= 0.2.5
BuildRequires:    R-CRAN-broom.mixed >= 0.2.3
BuildRequires:    R-survival 
Requires:         R-CRAN-tibble >= 2.0.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-glue >= 1.3.0
Requires:         R-CRAN-knitr >= 1.21
Requires:         R-CRAN-tidyr >= 0.8.2
Requires:         R-CRAN-dplyr >= 0.7.8
Requires:         R-CRAN-broom >= 0.5.1
Requires:         R-CRAN-rlang >= 0.3.1
Requires:         R-CRAN-purrr >= 0.3.0
Requires:         R-CRAN-tidyselect >= 0.2.5
Requires:         R-CRAN-broom.mixed >= 0.2.3
Requires:         R-survival 

%description
Creates presentation-ready tables summarizing data sets, regression
models, and more. The code to create the tables is concise and highly
customizable. Data frames can be summarized with any function, e.g.
mean(), median(), even user-written functions. Regression models are
summarized and include the reference rows for categorical variables.
Common regression models, such as logistic regression and Cox proportional
hazards regression, are automatically identified and the tables are
pre-filled with appropriate column headers. The package is enhanced when
the 'gt' package is installed. Use this code to install:
'remotes::install_github("rstudio/gt")'.

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
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX

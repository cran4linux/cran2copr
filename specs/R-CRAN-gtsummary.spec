%global packname  gtsummary
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}
Summary:          Presentation-Ready Data Summary and Analytic Result Tables

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.1
BuildRequires:    R-CRAN-usethis >= 1.6.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-glue >= 1.4.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-knitr >= 1.28
BuildRequires:    R-CRAN-tidyselect >= 1.1.0
BuildRequires:    R-CRAN-tidyr >= 1.0.3
BuildRequires:    R-CRAN-dplyr >= 0.8.5
BuildRequires:    R-CRAN-broom >= 0.5.6
BuildRequires:    R-CRAN-forcats >= 0.5.0
BuildRequires:    R-CRAN-rlang >= 0.4.6
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-broom.mixed >= 0.2.6
BuildRequires:    R-CRAN-gt >= 0.2.1
BuildRequires:    R-CRAN-lifecycle >= 0.2.0
BuildRequires:    R-survival 
Requires:         R-CRAN-tibble >= 3.0.1
Requires:         R-CRAN-usethis >= 1.6.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-glue >= 1.4.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-knitr >= 1.28
Requires:         R-CRAN-tidyselect >= 1.1.0
Requires:         R-CRAN-tidyr >= 1.0.3
Requires:         R-CRAN-dplyr >= 0.8.5
Requires:         R-CRAN-broom >= 0.5.6
Requires:         R-CRAN-forcats >= 0.5.0
Requires:         R-CRAN-rlang >= 0.4.6
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-broom.mixed >= 0.2.6
Requires:         R-CRAN-gt >= 0.2.1
Requires:         R-CRAN-lifecycle >= 0.2.0
Requires:         R-survival 

%description
Creates presentation-ready tables summarizing data sets, regression
models, and more. The code to create the tables is concise and highly
customizable. Data frames can be summarized with any function, e.g.
mean(), median(), even user-written functions. Regression models are
summarized and include the reference rows for categorical variables.
Common regression models, such as logistic regression and Cox proportional
hazards regression, are automatically identified and the tables are
pre-filled with appropriate column headers.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/rmarkdown_example
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX

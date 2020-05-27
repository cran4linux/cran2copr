%global packname  modelsummary
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Summary Tables for Statistical Models: Beautiful, Customizable,and Publication-Ready

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 1.8.5
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-tibble >= 1.4.2
BuildRequires:    R-CRAN-stringr >= 1.3.0
BuildRequires:    R-CRAN-knitr >= 1.20
BuildRequires:    R-CRAN-kableExtra >= 1.1.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.5
BuildRequires:    R-CRAN-broom >= 0.5.1
BuildRequires:    R-CRAN-purrr >= 0.2.1
BuildRequires:    R-CRAN-gt >= 0.2.0
BuildRequires:    R-CRAN-generics >= 0.0.2
Requires:         R-CRAN-checkmate >= 1.8.5
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-tibble >= 1.4.2
Requires:         R-CRAN-stringr >= 1.3.0
Requires:         R-CRAN-knitr >= 1.20
Requires:         R-CRAN-kableExtra >= 1.1.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.5
Requires:         R-CRAN-broom >= 0.5.1
Requires:         R-CRAN-purrr >= 0.2.1
Requires:         R-CRAN-gt >= 0.2.0
Requires:         R-CRAN-generics >= 0.0.2

%description
Create beautiful and customizable summary tables for statistical models.
'modelsummary' leverages the power of the 'gt', 'kableExtra' and 'broom'
packages. It supports dozens of model types, and can produce tables in
HTML, LaTeX, RTF, Text/Markdown, JPG, PNG, and LaTeX formats. The tables
can also be integrated in 'Rmarkdown', 'knitr', or 'Sweave' dynamic
documents.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX

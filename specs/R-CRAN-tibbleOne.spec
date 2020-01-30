%global packname  tibbleOne
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Table One for 'Latex', 'Word', and 'Html' 'R Markdown' Documents

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-knitr >= 1.23
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-labelled 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-knitr >= 1.23
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-officer 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-labelled 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-glue 
Requires:         R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lifecycle 

%description
Table one is a tabular description of characteristics, e.g., demographics
of patients in a clinical trial, presented overall and also stratified by
a categorical variable, e.g. treatment group.  There are many excellent
packages available to create table one.  This package focuses on providing
table one objects that seamlessly fit into 'R Markdown' analyses.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

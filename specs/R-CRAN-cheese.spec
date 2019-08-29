%global packname  cheese
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}
Summary:          Tools for Intuitive and Flexible Statistical Analysis Workflows

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-methods >= 3.4.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-tibble >= 1.4.2
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-knitr >= 1.20
BuildRequires:    R-CRAN-kableExtra >= 1.0.1
BuildRequires:    R-CRAN-tidyr >= 0.8.1
BuildRequires:    R-CRAN-dplyr >= 0.7.7
BuildRequires:    R-CRAN-rlang >= 0.3.0.1
BuildRequires:    R-CRAN-forcats >= 0.3.0
BuildRequires:    R-CRAN-purrr >= 0.2.4
BuildRequires:    R-CRAN-tidyselect >= 0.2.4
Requires:         R-methods >= 3.4.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-tibble >= 1.4.2
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-knitr >= 1.20
Requires:         R-CRAN-kableExtra >= 1.0.1
Requires:         R-CRAN-tidyr >= 0.8.1
Requires:         R-CRAN-dplyr >= 0.7.7
Requires:         R-CRAN-rlang >= 0.3.0.1
Requires:         R-CRAN-forcats >= 0.3.0
Requires:         R-CRAN-purrr >= 0.2.4
Requires:         R-CRAN-tidyselect >= 0.2.4

%description
Contains flexible and intuitive functions to assist in carrying out tasks
in a statistical analysis and to get from the raw data to
presentation-ready results. A user-friendly interface is used in
specialized functions that are aimed at common tasks such as building a
univariate descriptive table for variables in a dataset. These high-level
functions are built on a collection of low(er)-level functions that may be
useful for aspects of a custom statistical analysis workflow or for
general programming use.

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

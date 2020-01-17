%global packname  groupedstats
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Grouped Statistical Analyses in a Tidy Way

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-haven >= 2.2.0
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-skimr >= 2.0.2
BuildRequires:    R-CRAN-glue >= 1.3.1
BuildRequires:    R-CRAN-lme4 >= 1.1.21
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-rlang >= 0.4.2
BuildRequires:    R-CRAN-purrr >= 0.3.3
BuildRequires:    R-CRAN-parameters >= 0.3.0
BuildRequires:    R-CRAN-sjstats >= 0.17.7
BuildRequires:    R-CRAN-rstudioapi >= 0.10
BuildRequires:    R-CRAN-broomExtra >= 0.0.6
BuildRequires:    R-stats 
Requires:         R-CRAN-haven >= 2.2.0
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-skimr >= 2.0.2
Requires:         R-CRAN-glue >= 1.3.1
Requires:         R-CRAN-lme4 >= 1.1.21
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-rlang >= 0.4.2
Requires:         R-CRAN-purrr >= 0.3.3
Requires:         R-CRAN-parameters >= 0.3.0
Requires:         R-CRAN-sjstats >= 0.17.7
Requires:         R-CRAN-rstudioapi >= 0.10
Requires:         R-CRAN-broomExtra >= 0.0.6
Requires:         R-stats 

%description
Collection of functions to run statistical tests across all combinations
of multiple grouping variables.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX

%global packname  tidyr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Tidy Messy Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-tibble >= 2.1.1
BuildRequires:    R-CRAN-dplyr >= 0.8.2
BuildRequires:    R-CRAN-tidyselect >= 0.2.5
BuildRequires:    R-CRAN-vctrs >= 0.2.0
BuildRequires:    R-CRAN-ellipsis >= 0.1.0
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-tibble >= 2.1.1
Requires:         R-CRAN-dplyr >= 0.8.2
Requires:         R-CRAN-tidyselect >= 0.2.5
Requires:         R-CRAN-vctrs >= 0.2.0
Requires:         R-CRAN-ellipsis >= 0.1.0
Requires:         R-CRAN-glue 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringi 
Requires:         R-utils 
Requires:         R-CRAN-lifecycle 

%description
Tools to help to create tidy data, where each column is a variable, each
row is an observation, and each cell contains a single value. 'tidyr'
contains tools for changing the shape (pivoting) and hierarchy (nesting
and 'unnesting') of a dataset, turning deeply nested lists into
rectangular data frames ('rectangling'), and extracting values out of
string columns. It also includes tools for working with missing values
(both implicit and explicit).

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
%{rlibdir}/%{packname}/libs

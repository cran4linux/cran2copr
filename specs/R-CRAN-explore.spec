%global packname  explore
%global packver   0.5.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.5
Release:          2%{?dist}
Summary:          Simplifies Exploratory Data Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-odbc 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-rpart.plot 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-magrittr 
Requires:         R-MASS 
Requires:         R-CRAN-odbc 
Requires:         R-CRAN-rlang 
Requires:         R-rpart 
Requires:         R-CRAN-rpart.plot 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rmarkdown 

%description
Interactive data exploration with one line of code or use an easy to
remember set of tidy functions for exploratory data analysis. Introduces
three main verbs. explore() to graphically explore a variable or table,
describe() to describe a variable or table and report() to create an
automated report.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX

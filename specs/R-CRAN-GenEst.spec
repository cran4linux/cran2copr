%global packname  GenEst
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          1%{?dist}
Summary:          Generalized Mortality Estimator

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-htmlwidgets >= 1.5
BuildRequires:    R-CRAN-shiny >= 1.4.0
BuildRequires:    R-CRAN-corpus 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-hellno 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-sticky 
BuildRequires:    R-survival 
Requires:         R-CRAN-htmlwidgets >= 1.5
Requires:         R-CRAN-shiny >= 1.4.0
Requires:         R-CRAN-corpus 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-gsl 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-hellno 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-lubridate 
Requires:         R-MASS 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-sticky 
Requires:         R-survival 

%description
Command-line and 'shiny' GUI implementation of the GenEst models for
estimating bird and bat mortality at wind and solar power facilities,
following Dalthorp, et al. (2018) <doi:10.3133/tm7A2>.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/app
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

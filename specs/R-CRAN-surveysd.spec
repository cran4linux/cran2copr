%global packname  surveysd
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Survey Standard Error Estimation for Cumulated Estimates andtheir Differences in Complex Panel Designs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-laeken 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-laeken 
Requires:         R-methods 
Requires:         R-CRAN-dplyr 

%description
Calculate point estimates and their standard errors in complex household
surveys using bootstrap replicates. Bootstrapping considers survey design
with a rotating panel. A comprehensive description of the methodology can
be found under
<https://statistikat.github.io/surveysd/articles/methodology.html>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

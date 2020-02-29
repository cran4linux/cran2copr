%global packname  sdcTable
%global packver   0.30
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.30
Release:          1%{?dist}
Summary:          Methods for Statistical Disclosure Control in Tabular Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    glpk-devel
BuildRequires:    gmp-devel
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-sdcHierarchies >= 0.18
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rglpk 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-CRAN-lpSolveAPI 
Requires:         R-CRAN-sdcHierarchies >= 0.18
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-methods 
Requires:         R-CRAN-Rglpk 
Requires:         R-CRAN-slam 
Requires:         R-CRAN-lpSolveAPI 

%description
Methods for statistical disclosure control in tabular data such as primary
and secondary cell suppression as described for example in Hundepol et al.
(2012) <doi:10.1002/9781118348239> are covered in this package.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

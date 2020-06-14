%global packname  cort
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          2%{?dist}
Summary:          Some Empiric and Nonparametric Copula Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-osqp 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-furrr 
Requires:         R-CRAN-Rdpack 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-osqp 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-furrr 

%description
Provides S4 classes and methods to fit several copula models: The classic
empirical checkerboard copula and the empirical checkerboard copula with
known margins, see Cuberos, Masiello and Maume-Deschamps (2019)
<doi:10.1080/03610926.2019.1586936> are proposed. These two models allow
to fit copulas in high dimension with a small number of observations, and
they are always proper copulas. Some flexibility is added via a
possibility to differentiate the checkerboard parameter by dimension. The
last model consist of the implementation of the Copula Recursive Tree
algorithm proposed by Laverny, Maume-Deschamps, Masiello and Rullière
(2020) <arXiv:2005.02912>, including the localised dimension reduction,
which fits a copula by recursive splitting of the copula domain. We also
provide an efficient way of mixing copulas, allowing to bag the algorithm
into a forest, and a generic way of measuring d-dimensional boxes with a
copula.

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
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

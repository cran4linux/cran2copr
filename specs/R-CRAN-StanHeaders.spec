%global debug_package %{nil}
%global packname  StanHeaders
%global packver   2.21.0-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.21.0.5
Release:          2%{?dist}
Summary:          C++ Header Files for Stan

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-RcppParallel >= 5.0.1

%description
The C++ header files of the Stan project are provided by this package, but
it contains little R code or documentation. The main reference is the
vignette. There is a shared object containing part of the 'CVODES'
library, but its functionality is not accessible from R. 'StanHeaders' is
only useful for developers who want to utilize the 'LinkingTo' directive
of their package's DESCRIPTION file to build on the Stan library without
incurring unnecessary dependencies. The Stan project develops a
probabilistic programming language that implements full or approximate
Bayesian statistical inference via Markov Chain Monte Carlo or
'variational' methods and implements (optionally penalized) maximum
likelihood estimation via optimization. The Stan library includes an
advanced automatic differentiation scheme, 'templated' statistical and
linear algebra functions that can handle the automatically
'differentiable' scalar types (and doubles, 'ints', etc.), and a parser
for the Stan language. The 'rstan' package provides user-facing R
functions to parse, compile, test, estimate, and analyze Stan models.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
%doc %{rlibdir}/%{packname}/lib

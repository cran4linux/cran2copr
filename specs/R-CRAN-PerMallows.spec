%global packname  PerMallows
%global packver   1.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.13
Release:          2%{?dist}
Summary:          Permutations and Mallows Distributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.10.3
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 0.10.3
Requires:         R-utils 

%description
Includes functions to work with the Mallows and Generalized Mallows
Models. The considered distances are Kendall's-tau, Cayley, Hamming and
Ulam and it includes functions for making inference, sampling and learning
such distributions, some of which are novel in the literature. As a
by-product, PerMallows also includes operations for permutations, paying
special attention to those related with the Kendall's-tau, Cayley, Ulam
and Hamming distances. It is also possible to generate random permutations
at a given distance, or with a given number of inversions, or cycles, or
fixed points or even with a given length on LIS (longest increasing
subsequence).

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/test.txt
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

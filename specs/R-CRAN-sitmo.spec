%global __brp_check_rpaths %{nil}
%global packname  sitmo
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Parallel Pseudo Random Number Generator (PPRNG) 'sitmo' HeaderFiles

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.13
Requires:         R-CRAN-Rcpp >= 0.12.13

%description
Provided within are two high quality and fast PPRNGs that may be used in
an 'OpenMP' parallel environment. In addition, there is a generator for
one dimensional low-discrepancy sequence. The objective of this library to
consolidate the distribution of the 'sitmo' (C++98 & C++11), 'threefry'
and 'vandercorput' (C++11-only) engines on CRAN by enabling others to link
to the header files inside of 'sitmo' instead of including a copy of each
engine within their individual package. Lastly, the package contains
example implementations using the 'sitmo' package and three accompanying
vignette that provide additional information.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

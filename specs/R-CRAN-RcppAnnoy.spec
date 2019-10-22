%global packname  RcppAnnoy
%global packver   0.0.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.13
Release:          1%{?dist}
Summary:          'Rcpp' Bindings for 'Annoy', a Library for Approximate NearestNeighbors

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-Rcpp >= 0.11.3
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 0.11.3
Requires:         R-methods 

%description
'Annoy' is a small C++ library for Approximate Nearest Neighbors written
for efficient memory usage as well an ability to load from / save to disk.
This package provides an R interface by relying on the 'Rcpp' package,
exposing the same interface as the original Python wrapper to 'Annoy'. See
<https://github.com/spotify/annoy> for more on 'Annoy'. 'Annoy' is
released under Version 2.0 of the Apache License. Also included is a small
Windows port of 'mmap' which is released under the MIT license.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/tinytest
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

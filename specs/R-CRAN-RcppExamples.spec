%global __brp_check_rpaths %{nil}
%global packname  RcppExamples
%global packver   0.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.9
Release:          3%{?dist}%{?buildtag}
Summary:          Examples using 'Rcpp' to Interface R and C++

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-Rcpp 

%description
Examples for Seamless R and C++ integration The 'Rcpp' package contains a
C++ library that facilitates the integration of R and C++ in various ways.
This package provides some usage examples. Note that the documentation in
this package currently does not cover all the features in the package. The
site <http://gallery.rcpp.org> regroups a large number of examples for
'Rcpp'.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}

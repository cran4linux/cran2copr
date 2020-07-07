%global packname  eNchange
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Ensemble Methods for Multiple Change-Point Detection

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-hawkes 
BuildRequires:    R-CRAN-ACDm 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-doParallel 
Requires:         R-methods 
Requires:         R-CRAN-hawkes 
Requires:         R-CRAN-ACDm 

%description
Implements a segmentation algorithm for multiple change-point detection in
univariate time series using the Ensemble Binary Segmentation of Korkas
(2020) <arXiv:2003.03649>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

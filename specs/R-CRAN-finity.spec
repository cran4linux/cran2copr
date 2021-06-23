%global __brp_check_rpaths %{nil}
%global packname  finity
%global packver   0.1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4.1
Release:          3%{?dist}%{?buildtag}
Summary:          Test for Finiteness of Moments in a Distribution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-CRAN-stabledist >= 0.7
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-CRAN-stabledist >= 0.7

%description
The purpose of this package is to tests whether a given moment of the
distribution of a given sample is finite or not. For heavy-tailed
distributions with tail exponent b, only moments of order smaller than b
are finite. Tail exponent and heavy- tailedness are notoriously difficult
to ascertain. But the finiteness of moments (including fractional moments)
can be tested directly. This package does that following the test
suggested by Trapani (2016) <doi:10.1016/j.jeconom.2015.08.006>.

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

%global packname  mmpca
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}
Summary:          Integrative Analysis of Several Related Data Matrices

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-gsl >= 1.9
BuildRequires:    R-CRAN-digest >= 0.6.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-gsl >= 1.9
Requires:         R-CRAN-digest >= 0.6.0

%description
A generalization of principal component analysis for integrative analysis.
The method finds principal components that describe single matrices or
that are common to several matrices. The solutions are sparse. Rank of
solutions is automatically selected using cross validation. The method is
described in Kallus, Johansson, Nelander and Jörnsten (2019)
<arXiv:1911.04927>.

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

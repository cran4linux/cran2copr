%global packname  blockmatrix
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          blockmatrix: Tools to solve algebraic systems with partitionedmatrices

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13
Requires:         R-core >= 2.13
BuildArch:        noarch

%description
Some elementary matrix algebra tools are implemented to manage block
matrices or partitioned matrix, i.e. "matrix of matrices"
(http://en.wikipedia.org/wiki/Block_matrix). The block matrix is here
defined as a new S3 object. In this package, some methods for "matrix"
object are rewritten for "blockmatrix" object. New methods are
implemented. This package was created to solve equation systems with block
matrices for the analysis of environmental vector time series .
Bugs/comments/questions/collaboration of any kind are warmly welcomed.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

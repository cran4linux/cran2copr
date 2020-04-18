%global packname  kernelTDA
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Statistical Learning with Kernel for Persistence Diagrams

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Rdpack 
Requires:         R-methods 
Requires:         R-stats 

%description
Provides tools for exploiting topological information into standard
statistical learning algorithms. To this aim, this package contains the
most popular kernels defined on the space of persistence diagrams, and
persistence images. Moreover, it provides a solver for kernel Support
Vector Machines problems, whose kernels are not necessarily positive
semidefinite, based on the C++ library 'LIBSVM'
<https://www.csie.ntu.edu.tw/~cjlin/libsvm/>. Additionally, it allows to
compute Wasserstein distance between persistence diagrams with an
arbitrary ground metric, building an R interface for the C++ library
'HERA' <https://bitbucket.org/grey_narn/hera/src/master/>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

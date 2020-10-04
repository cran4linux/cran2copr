%global packname  kergp
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          3%{?dist}%{?buildtag}
Summary:          Gaussian Process Laboratory

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.10.5
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-lattice 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 0.10.5
Requires:         R-methods 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-nloptr 
Requires:         R-lattice 
Requires:         R-MASS 
Requires:         R-CRAN-numDeriv 
Requires:         R-stats4 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-doFuture 
Requires:         R-utils 

%description
Gaussian process regression with an emphasis on kernels. Quantitative and
qualitative inputs are accepted. Some pre-defined kernels are available,
such as radial or tensor-sum for quantitative inputs, and compound
symmetry, low rank, group kernel for qualitative inputs. The user can
define new kernels and composite kernels through a formula mechanism.
Useful methods include parameter estimation by maximum likelihood,
simulation, prediction and leave-one-out validation.

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
%{rlibdir}/%{packname}/libs

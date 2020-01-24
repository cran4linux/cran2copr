%global packname  gofCopula
%global packver   0.3-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Goodness-of-Fit Tests for Copulae

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.9.0
Requires:         R-core >= 1.9.0
BuildRequires:    R-CRAN-VineCopula >= 2.0.5
BuildRequires:    R-CRAN-copula >= 0.999.15
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-SparseGrid 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-yarrr 
BuildRequires:    R-CRAN-progress 
Requires:         R-CRAN-VineCopula >= 2.0.5
Requires:         R-CRAN-copula >= 0.999.15
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-SparseGrid 
Requires:         R-CRAN-numDeriv 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-MASS 
Requires:         R-utils 
Requires:         R-CRAN-yarrr 
Requires:         R-CRAN-progress 

%description
Several Goodness-of-Fit (GoF) tests for Copulae are provided. A new hybrid
test, Zhang et al. (2016) <doi:10.1016/j.jeconom.2016.02.017> is
implemented which supports all of the individual tests in the package,
e.g. Genest et al. (2009) <doi:10.1016/j.insmatheco.2007.10.005>.
Estimation methods for the margins are provided and all the tests support
parameter estimation and predefined values. The parameters are estimated
by pseudo maximum likelihood but if it fails the estimation switches
automatically to inversion of Kendall's tau. For reproducibility of
results, the functions support the definition of seeds. Also all the tests
support automatized parallelization of the bootstrapping tasks. The
package provides an interface to perform new GoF tests by submitting the
test statistic.

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
%{rlibdir}/%{packname}/INDEX

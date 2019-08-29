%global packname  ETAS
%global packver   0.4.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.6
Release:          1%{?dist}
Summary:          Modeling Earthquake Data Using 'ETAS' Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-goftest 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-fields 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-maps 
Requires:         R-lattice 
Requires:         R-CRAN-goftest 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-fields 

%description
Fits the space-time Epidemic Type Aftershock Sequence ('ETAS') model to
earthquake catalogs using a stochastic 'declustering' approach. The 'ETAS'
model is a 'spatio-temporal' marked point process model and a special case
of the 'Hawkes' process. The package is based on a Fortran program by
'Jiancang Zhuang' (available at
<http://bemlar.ism.ac.jp/zhuang/software.html>), which is modified and
translated into C++ and C such that it can be called from R. Parallel
computing with 'OpenMP' is possible on supported platforms.

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
%{rlibdir}/%{packname}/libs

%global packname  demu
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          2%{?dist}
Summary:          Optimal Design Emulators via Point Processes

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-ClusterR 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-stats 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-spam 
Requires:         R-Matrix 
Requires:         R-CRAN-ClusterR 

%description
Implements the Determinantal point process (DPP) based optimal design
emulator described in Pratola, Lin and Craigmile (2018) <arXiv:1804.02089>
for Gaussian process regression models.  See
<http://www.matthewpratola.com/software> for more information and
examples.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

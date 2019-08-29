%global packname  fChange
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          Change Point Analysis in Functional Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-sde 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-lattice 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-sde 
Requires:         R-stats 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-reshape2 
Requires:         R-lattice 

%description
Change point estimation and detection methods for functional data are
implemented using dimension reduction via functional principal component
analysis and a fully-functional (norm-based) method. Detecting and dating
structural breaks for both dependent and independent functional samples is
illustrated along with some basic functional data generating processes.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX

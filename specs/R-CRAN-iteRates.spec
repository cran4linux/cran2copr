%global packname  iteRates
%global packver   3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1
Release:          1%{?dist}
Summary:          Parametric rate comparison

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-partitions 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-apTreeshape 
BuildRequires:    R-CRAN-geiger 
BuildRequires:    R-CRAN-gtools 
Requires:         R-CRAN-partitions 
Requires:         R-stats 
Requires:         R-CRAN-VGAM 
Requires:         R-MASS 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-apTreeshape 
Requires:         R-CRAN-geiger 
Requires:         R-CRAN-gtools 

%description
Iterates through a phylogenetic tree to identify regions of rate variation
using the parametric rate comparison test.

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

%global packname  PCPS
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          1%{?dist}
Summary:          Principal Coordinates of Phylogenetic Structure

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-SYNCSA >= 1.3.4
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-picante 
BuildRequires:    R-CRAN-phylobase 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-parallel 
BuildRequires:    R-nlme 
Requires:         R-CRAN-SYNCSA >= 1.3.4
Requires:         R-CRAN-ape 
Requires:         R-CRAN-picante 
Requires:         R-CRAN-phylobase 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-RcppArmadillo 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-parallel 
Requires:         R-nlme 

%description
Set of functions for analysis of Principal Coordinates of Phylogenetic
Structure (PCPS).

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

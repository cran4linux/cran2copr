%global packname  fbati
%global packver   1.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}
Summary:          Gene by Environment Interaction and Conditional Gene Tests forNuclear Families

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-pbatR >= 2.0.0
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-fgui 
BuildRequires:    R-CRAN-rootSolve 
Requires:         R-CRAN-pbatR >= 2.0.0
Requires:         R-tcltk 
Requires:         R-CRAN-fgui 
Requires:         R-CRAN-rootSolve 

%description
Does family-based gene by environment interaction tests, joint gene,
gene-environment interaction test, and a test of a set of genes
conditional on another set of genes.

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

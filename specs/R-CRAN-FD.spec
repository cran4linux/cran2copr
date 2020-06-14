%global packname  FD
%global packver   1.0-12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.12
Release:          2%{?dist}
Summary:          Measuring functional diversity (FD) from multiple traits, andother tools for functional ecology

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-vegan 

%description
FD is a package to compute different multidimensional FD indices. It
implements a distance-based framework to measure FD that allows any number
and type of functional traits, and can also consider species relative
abundances. It also contains other useful tools for functional ecology.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

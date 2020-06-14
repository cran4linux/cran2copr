%global packname  miniCRAN
%global packver   0.2.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.12
Release:          2%{?dist}
Summary:          Create a Mini Version of CRAN Containing Only Selected Packages

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-assertthat 
Requires:         R-graphics 
Requires:         R-CRAN-httr 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-assertthat 

%description
Makes it possible to create an internally consistent repository consisting
of selected packages from CRAN-like repositories. The user specifies a set
of desired packages, and 'miniCRAN' recursively reads the dependency tree
for these packages, then downloads only this subset. The user can then
install packages from this repository directly, rather than from CRAN.
This is useful in production settings, e.g. server behind a firewall, or
remote locations with slow (or zero) Internet access.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX

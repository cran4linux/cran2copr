%global packname  brranching
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}
Summary:          Fetch 'Phylogenies' from Many Sources

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-crul >= 0.4.0
BuildRequires:    R-CRAN-phylocomr >= 0.1.4
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-taxize 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-conditionz 
Requires:         R-CRAN-crul >= 0.4.0
Requires:         R-CRAN-phylocomr >= 0.1.4
Requires:         R-CRAN-curl 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-taxize 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-conditionz 

%description
Includes methods for fetching 'phylogenies' from a variety of sources,
including the 'Phylomatic' web service
(<http://phylodiversity.net/phylomatic>), and 'Phylocom'
(<https://github.com/phylocom/phylocom/>).

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/ignore
%doc %{rlibdir}/%{packname}/vign
%{rlibdir}/%{packname}/INDEX

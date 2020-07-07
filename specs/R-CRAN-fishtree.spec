%global packname  fishtree
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          3%{?dist}
Summary:          Interface to the Fish Tree of Life API

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ape >= 5.2
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-rlang >= 0.4.1
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-parallel 
Requires:         R-CRAN-ape >= 5.2
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-rlang >= 0.4.1
Requires:         R-utils 
Requires:         R-CRAN-memoise 
Requires:         R-parallel 

%description
An interface to the Fish Tree of Life API to download taxonomies,
phylogenies, fossil calibrations, and diversification rate information for
ray-finned fishes.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX

%global packname  Diderot
%global packver   0.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.13
Release:          2%{?dist}
Summary:          Bibliographic Network Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-splitstackshape 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-graphics 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-splitstackshape 
Requires:         R-CRAN-data.table 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 

%description
Enables the user to build a citation network/graph from bibliographic data
and, based on modularity and heterocitation metrics, assess the degree of
awareness/cross-fertilization between two corpora/communities. This
toolset is optimized for Scopus data.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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

%global packname  bipartite
%global packver   2.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.13
Release:          1%{?dist}
Summary:          Visualising Bipartite Networks and Calculating Some (Ecological)Indices

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-permute 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-sna 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-igraph 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-CRAN-permute 

%description
Functions to visualise webs and calculate a series of indices commonly
used to describe pattern in (ecological) webs. It focuses on webs
consisting of only two levels (bipartite), e.g. pollination webs or
predator-prey-webs. Visualisation is important to get an idea of what we
are actually looking at, while the indices summarise different aspects of
the web's topology.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

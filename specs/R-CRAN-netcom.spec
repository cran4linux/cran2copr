%global packname  netcom
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Dynamic Network Alignment

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-pdist 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-clue 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-igraph 
Requires:         R-Matrix 
Requires:         R-CRAN-pdist 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-vegan 

%description
Functions to take two networks stored as matrices and return a node-level
injection between them (bijection if the input networks are of the same
size). The alignment is made by comparing diffusion kernels originating
from each node in one network to those originating from each node in the
other network. This creates a cost matrix where rows are nodes from one
network and columns are nodes from the other network. Optimal node
pairings are then found using the Hungarian algorithm.

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

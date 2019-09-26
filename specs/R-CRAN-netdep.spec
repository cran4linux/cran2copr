%global packname  netdep
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Testing for Network Dependence

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-igraphdata 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mvrtn 
Requires:         R-stats 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-igraphdata 
Requires:         R-MASS 
Requires:         R-CRAN-mvrtn 

%description
When network dependence is present, that is when social relations can
engender dependence in the outcome of interest, treating such observations
as independent results in invalid, anti-conservative statistical
inference. We propose a test of independence among observations sampled
from a single network <arXiv:1710.03296>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

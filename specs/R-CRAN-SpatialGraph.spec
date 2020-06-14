%global packname  SpatialGraph
%global packver   1.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          2%{?dist}
Summary:          SpatialGraph Class

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-splancs 
Requires:         R-CRAN-igraph 
Requires:         R-methods 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-shape 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-splancs 

%description
Provision of the S4 SpatialGraph class built on top of objects provided by
'igraph' and 'sp' packages, and associated utilities. See the
documentation of the SpatialGraph-class within this package for further
description. An example of how from a few points one can arrive to a
SpatialGraph is provided in the function sl2sg().

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

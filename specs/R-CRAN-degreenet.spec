%global __brp_check_rpaths %{nil}
%global packname  degreenet
%global packver   1.3-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.3
Release:          3%{?dist}%{?buildtag}
Summary:          Models for Skewed Count Distributions Relevant to Networks

License:          GPL-3 + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-network 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-network 

%description
Likelihood-based inference for skewed count distributions used in network
modeling. "degreenet" is a part of the "statnet" suite of packages for
network analysis.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}

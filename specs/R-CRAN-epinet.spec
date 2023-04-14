%global __brp_check_rpaths %{nil}
%global packname  epinet
%global packver   2.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.8
Release:          3%{?dist}%{?buildtag}
Summary:          Epidemic/Network-Related Tools

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-network 
Requires:         R-CRAN-network 

%description
A collection of epidemic/network-related tools. Simulates transmission of
diseases through contact networks. Performs Bayesian inference on network
and epidemic parameters, given epidemic data.

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

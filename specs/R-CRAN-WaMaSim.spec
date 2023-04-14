%global __brp_check_rpaths %{nil}
%global packname  WaMaSim
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Simulate Rehabilitation Strategies for Water DistributionSystems

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-magrittr >= 1.5

%description
The outcome of various rehabilitation strategies for water distribution
systems can be modeled with the Water Management Simulator (WaMaSim). Pipe
breaks and the corresponding damage and rehabilitation costs are
simulated. It is mainly intended to be used as educational tool for the
Water Infrastructure Experimental and Computer Laboratory at ETH Zurich,
Switzerland.

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

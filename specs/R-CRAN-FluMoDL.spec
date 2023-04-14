%global __brp_check_rpaths %{nil}
%global packname  FluMoDL
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Influenza-Attributable Mortality with Distributed-Lag Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dlnm 
BuildRequires:    R-CRAN-mvmeta 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-tsModel 
Requires:         R-CRAN-dlnm 
Requires:         R-CRAN-mvmeta 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-splines 
Requires:         R-CRAN-tsModel 

%description
Functions to estimate the mortality attributable to influenza and
temperature, using distributed-lag nonlinear models (DLNMs), as first
implemented in Lytras et al. (2019)
<doi:10.2807/1560-7917.ES.2019.24.14.1800118>. Full descriptions of
underlying DLNM methodology in Gasparrini et al. <doi:10.1002/sim.3940>
(DLNMs), <doi:10.1186/1471-2288-14-55> (attributable risk from DLNMs) and
<doi:10.1002/sim.5471> (multivariate meta-analysis).

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

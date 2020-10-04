%global packname  mlVAR
%global packver   0.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.4
Release:          2%{?dist}%{?buildtag}
Summary:          Multi-Level Vector Autoregression

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-arm 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-clusterGeneration 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-MplusAutomation 
BuildRequires:    R-CRAN-graphicalVAR 
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-arm 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-clusterGeneration 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-abind 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-MplusAutomation 
Requires:         R-CRAN-graphicalVAR 

%description
Estimates the multi-level vector autoregression model on time-series data.
Three network structures are obtained: temporal networks, contemporaneous
networks and between-subjects networks.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}

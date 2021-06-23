%global __brp_check_rpaths %{nil}
%global packname  MBNMAdose
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Dose-Response MBNMA Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags >= 4.8
BuildRequires:    R-CRAN-checkmate >= 1.8.5
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-reshape2 >= 1.4.3
BuildRequires:    R-CRAN-igraph >= 1.1.2
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-R2jags >= 0.5.7
BuildRequires:    R-CRAN-rgeos >= 0.5.2
BuildRequires:    R-CRAN-Rdpack >= 0.11.0
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-utf8 
BuildRequires:    R-CRAN-formatR 
Requires:         R-CRAN-rjags >= 4.8
Requires:         R-CRAN-checkmate >= 1.8.5
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-reshape2 >= 1.4.3
Requires:         R-CRAN-igraph >= 1.1.2
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-R2jags >= 0.5.7
Requires:         R-CRAN-rgeos >= 0.5.2
Requires:         R-CRAN-Rdpack >= 0.11.0
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-utf8 
Requires:         R-CRAN-formatR 

%description
Fits Bayesian dose-response model-based network meta-analysis (MBNMA) that
incorporate multiple doses within an agent by modelling different
dose-response functions, as described by Mawdsley et al. (2016)
<doi:10.1002/psp4.12091>. By modelling dose-response relationships this
can connect networks of evidence that might otherwise be disconnected, and
can improve precision on treatment estimates. Several common dose-response
functions are provided; others may be added by the user. Various
characteristics and assumptions can be flexibly added to the models, such
as shared class effects. The consistency of direct and indirect evidence
in the network can be assessed using unrelated mean effects models and/or
by node-splitting at the treatment level.

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
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}

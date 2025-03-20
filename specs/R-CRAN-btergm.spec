%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  btergm
%global packver   1.11.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.11.1
Release:          1%{?dist}%{?buildtag}
Summary:          Temporal Exponential Random Graph Models by Bootstrapped Pseudolikelihood

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ergm >= 4.8.1
BuildRequires:    R-CRAN-statnet.common >= 4.11.0
BuildRequires:    R-CRAN-sna >= 2.8
BuildRequires:    R-CRAN-igraph >= 2.1.2
BuildRequires:    R-CRAN-Matrix >= 1.3.2
BuildRequires:    R-CRAN-boot >= 1.3.17
BuildRequires:    R-CRAN-network >= 1.19.0
BuildRequires:    R-CRAN-ROCR >= 1.0.7
BuildRequires:    R-CRAN-coda >= 0.18.1
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-parallel 
Requires:         R-CRAN-ergm >= 4.8.1
Requires:         R-CRAN-statnet.common >= 4.11.0
Requires:         R-CRAN-sna >= 2.8
Requires:         R-CRAN-igraph >= 2.1.2
Requires:         R-CRAN-Matrix >= 1.3.2
Requires:         R-CRAN-boot >= 1.3.17
Requires:         R-CRAN-network >= 1.19.0
Requires:         R-CRAN-ROCR >= 1.0.7
Requires:         R-CRAN-coda >= 0.18.1
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-parallel 

%description
Temporal Exponential Random Graph Models (TERGM) estimated by maximum
pseudolikelihood with bootstrapped confidence intervals or Markov Chain
Monte Carlo maximum likelihood. Goodness of fit assessment for ERGMs,
TERGMs, and SAOMs. Micro-level interpretation of ERGMs and TERGMs. The
methods are described in Leifeld, Cranmer and Desmarais (2018), JStatSoft
<doi:10.18637/jss.v083.i06>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}

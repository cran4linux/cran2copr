%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  latentnet
%global packver   2.12.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.12.0
Release:          1%{?dist}%{?buildtag}
Summary:          Latent Position and Cluster Models for Statistical Networks

License:          GPL-3 + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-statnet.common >= 4.12.0
BuildRequires:    R-CRAN-ergm >= 4.10.1
BuildRequires:    R-CRAN-sna >= 2.8
BuildRequires:    R-CRAN-abind >= 1.4.8
BuildRequires:    R-CRAN-mvtnorm >= 1.3.3
BuildRequires:    R-CRAN-network >= 1.19.0
BuildRequires:    R-CRAN-coda >= 0.19.4.1
BuildRequires:    R-tools 
Requires:         R-CRAN-statnet.common >= 4.12.0
Requires:         R-CRAN-ergm >= 4.10.1
Requires:         R-CRAN-sna >= 2.8
Requires:         R-CRAN-abind >= 1.4.8
Requires:         R-CRAN-mvtnorm >= 1.3.3
Requires:         R-CRAN-network >= 1.19.0
Requires:         R-CRAN-coda >= 0.19.4.1
Requires:         R-tools 

%description
Fit and simulate latent position and cluster models for statistical
networks. See Krivitsky and Handcock (2008) <doi:10.18637/jss.v024.i05>
and Krivitsky, Handcock, Raftery, and Hoff (2009)
<doi:10.1016/j.socnet.2009.04.001>.

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

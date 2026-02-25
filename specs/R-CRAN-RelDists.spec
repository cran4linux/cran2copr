%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RelDists
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation for some Reliability Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-EstimationTools >= 4.0.0
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-gamlss 
BuildRequires:    R-CRAN-gamlss.dist 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-zipfR 
BuildRequires:    R-CRAN-BBmisc 
BuildRequires:    R-CRAN-lamW 
BuildRequires:    R-CRAN-VGAM 
Requires:         R-CRAN-EstimationTools >= 4.0.0
Requires:         R-CRAN-survival 
Requires:         R-CRAN-gamlss 
Requires:         R-CRAN-gamlss.dist 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-zipfR 
Requires:         R-CRAN-BBmisc 
Requires:         R-CRAN-lamW 
Requires:         R-CRAN-VGAM 

%description
Parameters estimation and linear regression models for Reliability
distributions families reviewed by Almalki & Nadarajah (2014)
<doi:10.1016/j.ress.2013.11.010> using Generalized Additive Models for
Location, Scale and Shape, GAMLSS by Rigby & Stasinopoulos (2005)
<doi:10.1111/j.1467-9876.2005.00510.x>.

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

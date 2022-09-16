%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Karen
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Kalman Reaction Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-gaussquad 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-parallel 
Requires:         R-CRAN-gaussquad 
Requires:         R-splines 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-expm 
Requires:         R-methods 

%description
This is a stochastic framework that combines biochemical reaction networks
with extended Kalman filter and Rauch-Tung-Striebel smoothing. This
framework allows to investigate the dynamics of cell differentiation from
high-dimensional clonal tracking data subject to measurement noise, false
negative errors, and systematically unobserved cell types. Our tool can
provide statistical support to biologists in gene therapy clonal tracking
studies for a deeper understanding of clonal reconstitution dynamics.
Further details on the methods can be found in L. Del Core et al., (2022)
<doi:10.1101/2022.07.08.499353>.

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

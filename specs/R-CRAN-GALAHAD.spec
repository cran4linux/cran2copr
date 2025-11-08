%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GALAHAD
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Geometry-Adaptive Lyapunov-Assured Hybrid Optimizer

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Implements the GALAHAD algorithm (Geometry-Adaptive 'Lyapunov'-Assured
Hybrid Optimizer), combining 'Riemannian' metrics, 'Lyapunov' stability
checks, and trust-region methods for stable optimization of mixed-geometry
parameters. Designed for biological modeling (germination, dose-response,
survival) where rates, concentrations, and unconstrained variables
coexist. Developed at the Minnesota Center for Prion Research and Outreach
(MNPRO), University of Minnesota. Based on Conn et al. (2000)
<doi:10.1137/1.9780898719857>, Amari (1998)
<doi:10.1162/089976698300017746>, Beck & Teboulle (2003)
<doi:10.1016/S0167-6377(02)00231-6>, Nesterov (2017)
<https://www.jstor.org/stable/resrep30722>, and Walne et al. (2020)
<doi:10.1002/agg2.20098>.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TemporalHazard
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Temporal Parametric Hazard Modeling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-survival 

%description
Provides native R implementations of the multiphase parametric hazard
model of Blackstone, Naftel, and Turner (1986)
<doi:10.1080/01621459.1986.10478314> with a focus on behavioral parity,
transparent numerics, and reproducible validation against reference
outputs from the original 'C'/'SAS' HAZARD program, originally developed
at the University of Alabama at Birmingham (UAB). The 'SAS'/'C' code and
this R package are currently developed and maintained at The Cleveland
Clinic Foundation, and the R code was wholly developed at The Cleveland
Clinic Foundation. The generalized temporal decomposition family extends
to longitudinal mixed-effects settings (Rajeswaran et al. 2018
<doi:10.1177/0962280215623583>). The package is intentionally implemented
in pure R first; performance-critical paths may later be accelerated with
'Rcpp' without changing the public interface.

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

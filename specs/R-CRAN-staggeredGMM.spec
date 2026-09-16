%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  staggeredGMM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          GMM Estimation of Treatment Effects Under Staggered Adoption

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fixest 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-fixest 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-utils 

%description
Estimates cohort-by-time average treatment effects under staggered
treatment adoption by the generalized method of moments. Three weighting
schemes are provided, corresponding to a pooled stationary covariance, a
cohort-specific stationary covariance, and an unrestricted within-cohort
covariance. Optional adjustment for baseline covariates by outcome
regression, and a serial-correlation robust over-identification test of
parallel trends and no anticipation, are also supported. The methods are
described in Arora and Bijani (2026) <doi:10.2139/ssrn.6558759>.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  superspreading
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Understand Individual-Level Variation in Infectious Disease Transmission

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-rlang 
Requires:         R-stats 

%description
Estimate and understand individual-level variation in transmission.
Implements density and cumulative compound Poisson discrete distribution
functions ('Kremer et al.' (2021) <doi:10.1038/s41598-021-93578-x>), as
well as functions to calculate infectious disease outbreak statistics
given epidemiological parameters on individual-level transmission;
including the probability of an outbreak becoming an epidemic/extinct
('Kucharski et al.' (2020) <doi:10.1016/S1473-3099(20)30144-4>), or the
cluster size statistics, e.g. what proportion of cases cause X%% of
transmission ('Lloyd-Smith et al.' (2005) <doi:10.1038/nature04153>).

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

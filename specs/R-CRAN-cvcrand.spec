%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cvcrand
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient Design and Analysis of Cluster Randomized Trials

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tableone 
Requires:         R-CRAN-tableone 

%description
Constrained randomization by Raab and Butcher (2001)
<doi:10.1002/1097-0258(20010215)20:3%%3C351::AID-SIM797%%3E3.0.CO;2-C> is
suitable for cluster randomized trials (CRTs) with a small number of
clusters (e.g., 20 or fewer). The procedure of constrained randomization
is based on the baseline values of some cluster-level covariates
specified. The intervention effect on the individual outcome can then be
analyzed through clustered permutation test introduced by Gail, et al.
(1996)
<doi:10.1002/(SICI)1097-0258(19960615)15:11%%3C1069::AID-SIM220%%3E3.0.CO;2-Q>.
Motivated from Li, et al. (2016) <doi:10.1002/sim.7410>, the package
performs constrained randomization on the baseline values of cluster-level
covariates and clustered permutation test on the individual-level outcomes
for cluster randomized trials.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dist.structure
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Structured Random Variables for Reliability System Distributions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-algebraic.dist 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-algebraic.dist 
Requires:         R-stats 
Requires:         R-utils 

%description
Extends the 'algebraic.dist' distribution algebra to random variables with
internal structure: coherent reliability systems decomposed into
components arranged by a structure function (series, parallel, k-out-of-n,
bridge, and arbitrary topologies via minimal path sets). Every
'dist_structure' object is a 'dist', so the full distribution algebra
(mean, vcov, sampler, surv, cdf) works automatically via default methods
that compose component-level distributions through the topology. Adds
structural queries: structure function evaluation, minimal path and cut
sets, system signature, critical states, dual, Birnbaum structural
importance, and system reliability. Topology shortcut constructors
(series_dist, parallel_dist, kofn_dist, bridge_dist) produce ready-to-use
dists from component dists and a chosen structure.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  biogeom
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Biological Geometries

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-spatstat.geom >= 2.4.0
Requires:         R-CRAN-spatstat.geom >= 2.4.0

%description
Is used to simulate and fit biological geometries. 'biogeom' incorporates
several novel universal parametric equations that can generate the
profiles of bird eggs, flowers, linear and lanceolate leaves, seeds,
starfish, and tree-rings (Gielis (2003) <doi:10.3732/ajb.90.3.333>; Shi et
al. (2020) <doi:10.3390/sym12040645>), three growth-rate curves
representing the ontogenetic growth trajectories of animals and plants
against time, and the axially symmetrical and integral forms of all these
functions (Shi et al. (2017) <doi:10.1016/j.ecolmodel.2017.01.012>; Shi et
al. (2021) <doi:10.3390/sym13081524>). The optimization method proposed by
Nelder and Mead (1965) <doi:10.1093/comjnl/7.4.308> was used to estimate
model parameters. 'biogeom' includes several real data sets of the
boundary coordinates of natural shapes, including avian eggs, fruit,
lanceolate and ovate leaves, tree rings, seeds, and sea stars,and can be
potentially applied to other natural shapes. 'biogeom' can quantify the
conspecific or interspecific similarity of natural outlines, and provides
information with important ecological and evolutionary implications for
the growth and form of living organisms. Please see Shi et al. (2022)
<doi:10.1111/nyas.14862> for details.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  informativeSCI
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Informative Simultaneous Confidence Intervals

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm >= 1.2.4
BuildRequires:    R-CRAN-gMCP >= 0.8.17
Requires:         R-CRAN-mvtnorm >= 1.2.4
Requires:         R-CRAN-gMCP >= 0.8.17

%description
Calculation of informative simultaneous confidence intervals for graphical
described multiple test procedures and given information weights. Bretz et
al. (2009) <doi:10.1002/sim.3495> and Brannath et al. (2024)
<doi:10.48550/arXiv.2402.13719>. Furthermore, exploration of the behavior
of the informative bounds in dependence of the information weights.
Comparisons with compatible bounds are possible. Strassburger and Bretz
(2008) <doi:10.1002/sim.3338>.

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

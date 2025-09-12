%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rsamplr
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Sampling Algorithms and Spatially Balanced Sampling

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2

%description
Fast tools for unequal probability sampling in multi-dimensional spaces,
implemented in Rust for high performance. The package offers a wide range
of methods, including Sampford (Sampford, 1967,
<doi:10.1093/biomet/54.3-4.499>) and correlated Poisson sampling
(Bondesson and Thorburn, 2008, <doi:10.1111/j.1467-9469.2008.00596.x>),
pivotal sampling (Deville and Tillé, 1998, <doi:10.1093/biomet/91.4.893>),
and balanced sampling such as the cube method (Deville and Tillé, 2004,
<doi:10.1093/biomet/91.4.893>) to ensure auxiliary totals are respected.
Spatially balanced approaches, including the local pivotal method
(Grafström et al., 2012, <doi:10.1111/j.1541-0420.2011.01699.x>),
spatially correlated Poisson sampling (Grafström, 2012,
<doi:10.1016/j.jspi.2011.07.003>), and locally correlated Poisson sampling
(Prentius, 2024, <doi:10.1002/env.2832>), provide efficient designs when
the target variable is linked to auxiliary information.

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

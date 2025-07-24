%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  triplediff
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Triple-Difference Estimators

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildRequires:    R-CRAN-Matrix >= 1.6.1
BuildRequires:    R-CRAN-BMisc >= 1.4.6
BuildRequires:    R-parallel >= 1.4.0
BuildRequires:    R-CRAN-data.table >= 1.15.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-CRAN-speedglm >= 0.3.5
BuildRequires:    R-CRAN-parglm >= 0.1.7
Requires:         R-CRAN-Matrix >= 1.6.1
Requires:         R-CRAN-BMisc >= 1.4.6
Requires:         R-parallel >= 1.4.0
Requires:         R-CRAN-data.table >= 1.15.0
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-CRAN-speedglm >= 0.3.5
Requires:         R-CRAN-parglm >= 0.1.7

%description
Implements triple-difference (DDD) estimators for both average treatment
effects and event-study parameters. Methods include regression adjustment,
inverse-probability weighting, and doubly-robust estimators, all of which
rely on a conditional DDD parallel-trends assumption and allow covariate
adjustment across multiple pre- and post-treatment periods. The
methodology is detailed in Ortiz-Villavicencio and Sant'Anna (2025)
<doi:10.48550/arXiv.2505.09942>.

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

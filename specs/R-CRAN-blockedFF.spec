%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  blockedFF
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generation of Blocked Fractional Factorial Designs (Two-Level and Three-Level)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Provides computational tools to generate efficient blocked and unblocked
fractional factorial designs for two-level and three-level factors using
the generalized Minimum Aberration (MA) criterion and related optimization
algorithms. Methodological foundations include the general theory of
minimum aberration as described by Cheng and Tang (2005)
<doi:10.1214/009053604000001228>, and the catalogue of three-level regular
fractional factorial designs developed by Xu (2005)
<doi:10.1007/s00184-005-0408-x>. The main functions dol2() and dol3()
generate blocked two-level and three-level fractional factorial designs,
respectively, using beam search, optimization-based ranking, confounding
assessment, and structured output suitable for complete factorial
situations.

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

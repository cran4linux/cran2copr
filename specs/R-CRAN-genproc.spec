%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  genproc
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Robust, Logged and Reproducible Iteration at Organizational Scale

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-parallel 
Requires:         R-CRAN-progressr 
Requires:         R-stats 
Requires:         R-utils 

%description
Turns one-off iterative R procedures (such as for loops, lapply() or
pmap() from 'purrr') into production-grade workflows by wrapping them with
orthogonal, composable execution layers. Two layers are always active:
structured logging with real traceback and per-case timing; and
reproducibility capture, which records the R version, loaded package
versions, execution environment, the exact iteration mask, and a
stat-based fingerprint of every input file referenced in the mask (with a
diff_inputs() helper to detect silent drift between runs). Parallel
execution (built on the 'future' framework, Bengtsson (2021)
<doi:10.32614/RJ-2021-048>), non-blocking background jobs, and opt-in
progress reporting (via 'progressr') are implemented as optional,
composable layers. Further layers (error replay, content-hash input
fingerprinting, content-based case identifiers) are planned and will
remain composable with the default layers.

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

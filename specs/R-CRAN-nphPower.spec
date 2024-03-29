%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nphPower
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sample Size Calculation under Non-Proportional Hazards

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-survival 
Requires:         R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-zoo 

%description
Performs combination tests and sample size calculation for fixed design
with survival endpoints using combination tests under either proportional
hazards or non-proportional hazards. The combination tests include maximum
weighted log-rank test and projection test. The sample size calculation
procedure is very flexible, allowing for user-defined hazard ratio
function and considering various trial conditions like staggered entry,
drop-out etc. The sample size calculation also applies to various cure
models such as proportional hazards cure model, cure model with (random)
delayed treatments effects. Trial simulation function is also provided to
facilitate the empirical power calculation. The references for projection
test and maximum weighted logrank test include Brendel et al. (2014)
<doi:10.1111/sjos.12059> and Cheng and He (2021) <arXiv:2110.03833>. The
references for sample size calculation under proportional hazard include
Schoenfeld (1981) <doi:10.1093/biomet/68.1.316> and Freedman (1982)
<doi:10.1002/sim.4780010204>. The references for calculation under
non-proportional hazards include Lakatos (1988) <doi:10.2307/2531910> and
Cheng and He (2023) <doi:10.1002/bimj.202100403>.

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

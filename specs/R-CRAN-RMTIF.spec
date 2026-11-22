%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RMTIF
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Restricted Mean Time in Favor of Treatment

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-parallel 

%description
Estimates restricted mean time in favor of treatment from ordered
multistate trajectories, with lower states denoting better outcomes.
Provides complete-path pairwise estimation, projection standard errors,
normal confidence intervals and tests, terminal-aware inverse probability
of censoring weighting, stratified bootstrap inference, and pairwise
regression with sandwich or refitted-bootstrap inference. Includes
parameterized simulation and Monte Carlo summary tools for reversible
processes, continuous-time Markov paths, constant-utility regression, and
comparisons of longitudinal oncology endpoints. The restricted-time
estimand follows Mao (2023) <doi:10.1111/biom.13570>; pairwise regression
is motivated by the proportional win-fractions framework of Mao and Wang
(2021) <doi:10.1111/biom.13382>.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  odr
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Design and Statistical Power for Multilevel Experiments Investigating Main, Mediation, and Moderation Effects

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.0.0
BuildRequires:    R-graphics >= 3.0.0
BuildRequires:    R-base >= 3.0.0
Requires:         R-stats >= 3.0.0
Requires:         R-graphics >= 3.0.0
Requires:         R-base >= 3.0.0

%description
Calculate the optimal sample allocation that produces the highest
statistical power for experimental studies under a budget constraint,
perform power analyses with and without accommodating cost structures of
sampling, and calculate the relative efficiency between two sample
allocations. The references for the proposed methods include: (1) Shen,
Z., & Kelcey, B. (2020). Optimal sample allocation under unequal costs in
cluster-randomized trials. Journal of Educational and Behavioral
Statistics, 45(4): 446-474. <doi:10.3102/1076998620912418>. (2) Shen, Z.,
& Kelcey, B. (2022). Optimal sample allocation for three-level multisite
cluster-randomized trials. Journal of Research on Educational
Effectiveness, 15 (1), 130-150. <doi:10.1080/19345747.2021.1953200>. (3)
Shen, Z., & Kelcey, B. (2022). Optimal sample allocation in multisite
randomized trials. The Journal of Experimental Education.
<doi:10.1080/00220973.2020.1830361>. (4) Champely, S. (2020). pwr: Basic
functions for power analysis (Version 1.3-0) [Software]. Available from
<https://CRAN.R-project.org/package=pwr>.

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

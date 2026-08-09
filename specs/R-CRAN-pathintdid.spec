%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pathintdid
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Path-Integrated Difference-in-Differences

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 

%description
Implements the Path-Integrated Difference-in-Differences ('PI-DiD')
framework of Salavi (2026), which treats the treatment effect as a
trajectory tau(t) = c1(t) - c0(t) and integrates the baseline-differenced
gap over a post-treatment window to obtain a cumulative causal effect and
a path-integrated average treatment effect on the treated, together with
cluster-robust standard errors, confidence intervals, diagnostic plots,
and the pre-treatment parallel-trends, grid-density, and
anticipation-robustness checks of section 5 of the companion paper. This
approach avoids the endpoint-subtraction bias that arises whenever a
transitory policy's effect has fully decayed by the evaluation date, in
which case the conventional static difference-in-differences estimate can
be zero even though the cumulative benefit delivered to treated units was
strictly positive. Formerly distributed as a Stata package under the names
'pidid' and 'pididplot'.

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

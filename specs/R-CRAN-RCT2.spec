%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RCT2
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Designing and Analyzing Two-Stage Randomized Experiments

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-AER 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-quadprog 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-AER 
Requires:         R-stats 
Requires:         R-CRAN-quadprog 

%description
Provides various statistical methods for designing and analyzing two-stage
randomized controlled trials using the methods developed by Imai, Jiang,
and Malani (2021) <doi:10.1080/01621459.2020.1775612> and (2022+)
<doi:10.48550/arXiv.2011.07677>.  The package enables the estimation of
direct and spillover effects, conduct hypotheses tests, and conduct sample
size calculation for two-stage randomized controlled trials.

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

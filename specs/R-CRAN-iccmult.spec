%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  iccmult
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Intracluster Correlation Coefficient (ICC) in Clustered Categorical Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dirmult 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-ICCbin 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-stats 
Requires:         R-CRAN-dirmult 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-ICCbin 
Requires:         R-CRAN-lme4 
Requires:         R-stats 

%description
Assists in generating categorical clustered outcome data, estimating the
Intracluster Correlation Coefficient (ICC) for nominal or ordinal data
with 2+ categories under the resampling and method of moments (MoM)
methods, with confidence intervals.

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

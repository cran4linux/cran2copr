%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SIMICO
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Set-Based Inference for Multiple Interval-Censored Outcomes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-bindata 
BuildRequires:    R-CRAN-fastGHQuad 
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ICSKAT 
Requires:         R-CRAN-bindata 
Requires:         R-CRAN-fastGHQuad 
Requires:         R-CRAN-CompQuadForm 
Requires:         R-stats 
Requires:         R-CRAN-ICSKAT 

%description
Contains tests for association between a set of genetic variants and
multiple correlated outcomes that are interval censored. Interval-censored
data arises when the exact time of the onset of an outcome of interest is
unknown but known to fall between two time points.

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

%global __brp_check_rpaths %{nil}
%global packname  pairwise
%global packver   0.5.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Rasch Model Parameters by Pairwise Algorithm

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.1
Requires:         R-core >= 2.10.1
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-methods 

%description
Performs the explicit calculation -- not estimation! -- of the Rasch item
parameters for dichotomous and polytomous item responses, using a pairwise
comparison approach. Person parameters (WLE) are calculated according to
Warm's weighted likelihood approach.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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

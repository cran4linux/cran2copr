%global __brp_check_rpaths %{nil}
%global packname  psychotree
%global packver   0.16-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.16.0
Release:          1%{?dist}%{?buildtag}
Summary:          Recursive Partitioning Based on Psychometric Models

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-partykit >= 1.2.9
BuildRequires:    R-CRAN-psychotools >= 0.7.1
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Formula 
Requires:         R-CRAN-partykit >= 1.2.9
Requires:         R-CRAN-psychotools >= 0.7.1
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-CRAN-Formula 

%description
Recursive partitioning based on psychometric models, employing the general
MOB algorithm (from package partykit) to obtain Bradley-Terry trees, Rasch
trees, rating scale and partial credit trees, and MPT trees, trees for
1PL, 2PL, 3PL and 4PL models and generalized partial credit models.

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

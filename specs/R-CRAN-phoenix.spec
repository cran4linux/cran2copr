%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  phoenix
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          The Phoenix Pediatric Sepsis and Septic Shock Criteria

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
Implementation of the Phoenix and Phoenix-8 Sepsis Criteria as described
in "Development and Validation of the Phoenix Criteria for Pediatric
Sepsis and Septic Shock" by Sanchez-Pinto, Bennett, DeWitt, Russell et al.
(2024) <doi:10.1001/jama.2024.0196> (Drs. Sanchez-Pinto and Bennett
contributed equally to this manuscript; Dr. DeWitt and Mr. Russell
contributed equally to the manuscript) and "International Consensus
Criteria for Pediatric Sepsis and Septic Shock" by Schlapbach, Watson,
Sorce, Argent, et al. (2024) <doi:10.1001/jama.2024.0179> (Drs Schlapbach,
Watson, Sorce, and Argent contributed equally).

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

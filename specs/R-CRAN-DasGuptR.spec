%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DasGuptR
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Das Gupta Standardisation and Decomposition

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch

%description
Implementation of Das Gupta's standardisation and decomposition of
population rates, as set out "Standardization and decomposition of rates:
A user’s manual", Das Gupta (1993)
<https://www2.census.gov/library/publications/1993/demographics/p23-186.pdf>.
The goal of these methods is to calculate adjusted rates based on
compositional 'factors' and quantify the contribution of each factor to
the difference in crude rates between populations. The package offers
functionality to handle various scenarios for any number of factors and
populations, where said factors can be comprised of vectors across
sub-populations (including cross-classified population breakdowns), and
with the option to specify user-defined rate functions.

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

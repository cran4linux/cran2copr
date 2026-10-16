%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  trialfigs
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Efficacy and Safety Graphics for Clinical Review Packages

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-withr 

%description
Builds submission-style efficacy and safety figures used in clinical
review packages, with one simulator for each therapeutic area. Oncology
figures include Kaplan-Meier curves, RECIST waterfalls, swimmer plots and
spider plots. Cardiovascular, endocrine, immunology, infectious disease
and neuroscience figures include time-to-event curves, mean change from
baseline and responder rates. Shared safety figures include an
adverse-event dot plot, an eDISH liver plot, a laboratory shift plot and
an exposure plot. Reference lines follow RECIST 1.1 and the FDA
drug-induced liver injury guidance. This is not an FDA product and does
not guarantee regulatory acceptance.

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

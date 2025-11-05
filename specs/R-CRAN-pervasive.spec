%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pervasive
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Pervasiveness Functions for Correlational Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-arules 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-arules 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-psych 
Requires:         R-methods 
Requires:         R-stats 

%description
Analysis of pervasiveness of effects in correlational data. The Observed
Proportion (or Percentage) of Concordant Pairs (OPCP) is Kendall's Tau
expressed on a 0 to 1 metric instead of the traditional -1 to 1 metric to
facilitate interpretation. As its name implies, it represents the
proportion of concordant pairs in a sample (with an adjustment for ties).
Pairs are concordant when a participant who has a larger value on a
variable than another participant also has a larger value on a second
variable. The OPCP is therefore an easily interpretable indicator of
monotonicity. The pervasive functions are essentially wrappers for the
'arules' package by Hahsler et al.
(2025)<doi:10.32614/CRAN.package.arules> and serve to count individuals
who actually display the pattern(s) suggested by a regression. For more
details, see the paper "Considering approaches to pervasiveness in the
context of personality psychology" now accepted at the journal Personality
Science.

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

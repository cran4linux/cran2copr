%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PDXpower
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Time to Event Outcome in Experimental Designs of Pre-Clinical Studies

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-frailtypack 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
Requires:         R-CRAN-survival 
Requires:         R-stats 
Requires:         R-parallel 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-frailtypack 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 

%description
Conduct simulation-based customized power calculation for clustered time
to event data in a mixed crossed/nested design, where a number of cell
lines and a number of mice within each cell line are considered to achieve
a desired statistical power, motivated by Eckel-Passow and colleagues
(2021) <doi:10.1093/neuonc/noab137>. This package provides two commonly
used models for powering a design, linear mixed effects and Cox frailty
model. Both models account for within-subject (cell line) correlation
while holding different distributional assumptions about the outcome.
Alternatively, the counterparts of fixed effects model are also available,
which produces similar estimates of statistical power.

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

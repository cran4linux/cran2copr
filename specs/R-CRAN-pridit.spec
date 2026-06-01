%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pridit
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Composite Scoring via Principal Component Analysis of Ridit Scores

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-utils 

%description
Implements 'PRIDIT' (Principal Component Analysis applied to 'RIDITs'), an
unsupervised, nonparametric method for aggregating ordinal, categorical,
and continuous indicators into a single interpretable composite score.
Originally proposed by Brockett et al. (2002)
<doi:10.1111/1539-6975.00027> for insurance fraud detection and extended
to hospital quality measurement by Lieberthal (2008)
<doi:10.1111/j.1475-6773.2007.00821.x> and Lieberthal and Comer (2013)
<doi:10.1111/rmir.12009>. The package provides: (1) low-level functions
ridit(), PRIDITweight(), and PRIDITscore(); (2) a unified pridit() entry
point returning a classed object with print, summary, 'autoplot', and
'coef' methods; (3) pridit_boot() for bootstrap confidence intervals on
scores and weights; (4) a step_pridit() recipe step for out-of-sample
scoring within the 'tidymodels' framework; and (5) pridit_longitudinal()
for panel data, computing cross-period stability of scores and weights.

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

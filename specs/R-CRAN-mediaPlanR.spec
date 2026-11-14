%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mediaPlanR
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Reach and Exposure-Distribution Models for Media Planning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-utils 

%description
Reproducible implementations of reach and exposure-frequency models for
media planning. Provides exact reach and exposure distributions under
random duplication (Sainsbury and Binomial models); the Beta-Binomial
accumulation model and its multi-vehicle version of Metheringham (1964)
<doi:10.1080/00218499.1964.12519751>; the ad hoc duplication and
accumulation formulas of Agostini (1961)
<doi:10.1080/00218499.1961.12519620> and Hofmans (1966)
<doi:10.1177/002224376600300307>; and the multivariate exposure
distribution models of Danaher (1991) <doi:10.1177/002224379102800311>
(canonical expansion), Leckenby and Rice (1986)
<doi:10.1080/00913367.1986.10673014> (Morgensztern sequential
aggregation), Hyo Gyoo Kim (2005, doctoral dissertation, University of
Texas at Austin) (canonical sequential aggregation), Heejin Kim (1994,
doctoral dissertation, University of Texas at Austin) (conditional Beta
distribution), and Cheong (2007, doctoral dissertation, University of
Texas at Austin) and Cheong, Leckenby and Eakin (2011)
<doi:10.2753/JOA0091-3367400101> (multivariate Beta-Binomial). The three
dissertations have no DOI; their complete references are in the help
pages. Also includes an explicitly scoped Negative-Binomial count
approximation, the fitting of the Beta-Binomial model to an observed
reach, and the evaluation of predicted exposure distributions against
observed ones.

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

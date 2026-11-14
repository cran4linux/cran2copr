%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  winnify
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Visual Summaries and Wrappers for Estimating the Win Ratio and Related Measures

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-WINS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sloop 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-WINS 
Requires:         R-methods 
Requires:         R-CRAN-sloop 

%description
Facilitates analysis of Generalised Pairwise Comparisons with Prioritised
Outcomes (e.g. Win Ratio, Win Odds). Includes a wrapper function that
enables rank-based Desirability of Outcome Ranking analyses with any
existing ordinal analysis package (e.g. probabilistic index models
provided by R package `pim') plus automated input processing and a
formula-based interface for estimating win statistics (using R package
`WINS') without needing to restructure or rename the data. In both cases,
supports improved interpretation of prioritised outcomes analyses using
the approach proposed by Johns et al. (2026)
<doi:10.1177/17474930261475853> where the treatment effect is estimated
separately for each outcome plus cumulatively as they are added to the
outcome prioritisation. The contribution of each outcome to the overall
effect size is then visualised with a supplied plotting function.

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

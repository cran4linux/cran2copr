%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  winr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Randomization-Based Covariance Adjustment of Win Statistics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 

%description
A multi-visit clinical trial may collect participant responses on an
ordinal scale and may utilize a stratified design, such as randomization
within centers, to assess treatment efficacy across multiple visits.
Baseline characteristics may be strongly associated with the outcome, and
adjustment for them can improve power. The win ratio (ignores ties) and
the win odds (accounts for ties) can be useful when analyzing these types
of data from randomized controlled trials. This package provides
straightforward functions for adjustment of the win ratio and win odds for
stratification and baseline covariates, facilitating the comparison of
test and control treatments in multi-visit clinical trials. For additional
information concerning the methodologies and applied examples within this
package, please refer to the following publications: 1. Weideman, A.M.K.,
Kowalewski, E.K., & Koch, G.G. (2024). “Randomization-based covariance
adjustment of win ratios and win odds for randomized multi-visit studies
with ordinal outcomes.” Journal of Statistical Research, 58(1), 33–48.
<doi:10.3329/jsr.v58i1.75411>. 2. Kowalewski, E.K., Weideman, A.M.K., &
Koch, G.G. (2023). “SAS macro for randomization-based methods for
covariance and stratified adjustment of win ratios and win odds for
ordinal outcomes.” SESUG 2023 Proceedings, Paper 139-2023.

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

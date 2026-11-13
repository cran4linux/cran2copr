%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  depower
%global packver   2026.11.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2026.11.11
Release:          1%{?dist}%{?buildtag}
Summary:          Power Analysis for Differential Expression Studies

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5.0
Requires:         R-core >= 4.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-CRAN-glmmTMB 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-multidplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 
Requires:         R-CRAN-mvnfast 
Requires:         R-CRAN-glmmTMB 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-multidplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 

%description
Provides a convenient framework to simulate data, run hypothesis tests,
estimate power, and plot the results for differential expression studies.
The simulation-based framework is described in Klamer and Yu (2026)
<doi:10.1177/11769351261431247>. Outcomes may be lognormal, negative
binomial, or bivariate negative binomial. Supported designs are
one-sample, independent two-sample, and dependent two-sample comparisons.
Built-in tests include t-tests, Wald tests, and likelihood ratio tests.
User-defined tests are also accepted. The significance level can be set to
control the per-family error rate or the family-wise error rate. Negative
binomial methods are described in Yu, Fernandez, and Brock (2017)
<doi:10.1186/s12859-017-1648-2> and Yu, Fernandez, and Brock (2020)
<doi:10.1186/s12859-020-3541-7>.

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

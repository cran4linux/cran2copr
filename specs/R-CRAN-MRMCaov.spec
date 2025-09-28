%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MRMCaov
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Reader Multi-Case Analysis of Variance

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-trust 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-trust 

%description
Estimation and comparison of the performances of diagnostic tests in
multi-reader multi-case studies where true case statuses (or ground
truths) are known and one or more readers provide test ratings for
multiple cases.  Reader performance metrics are provided for area under
and expected utility of ROC curves, likelihood ratio of positive or
negative tests, and sensitivity and specificity.  ROC curves can be
estimated empirically or with binormal or binormal likelihood-ratio
models.  Statistical comparisons of diagnostic tests are based on the
ANOVA model of Obuchowski-Rockette and the unified framework of Hillis
(2005) <doi:10.1002/sim.2024>.  The ANOVA can be conducted with data from
a full factorial, nested, or partially paired study design; with random or
fixed readers or cases; and covariances estimated with the DeLong method,
jackknifing, or an unbiased method.  Smith and Hillis (2020)
<doi:10.1117/12.2549075>.

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

%global __brp_check_rpaths %{nil}
%global packname  ra4bayesmeta
%global packver   1.0-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Reference Analysis for Bayesian Meta-Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bayesmeta 
Requires:         R-CRAN-bayesmeta 

%description
Functionality for performing a principled reference analysis in the
Bayesian normal-normal hierarchical model used for Bayesian meta-analysis,
as described in Ott, Plummer and Roos (2021, "How vague is vague? How
informative is informative? Reference analysis for Bayesian
meta-analysis", under minor revision for Statistics in Medicine). Computes
a reference posterior, induced by a minimally informative improper
reference prior for the between-study (heterogeneity) standard deviation.
Determines additional proper anti-conservative (and conservative) prior
benchmarks. Includes functions for reference analyses at both the
posterior and the prior level, which, given the data, quantify the
informativeness of a heterogeneity prior of interest relative to the
minimally informative reference prior and the proper prior benchmarks. The
functions operate on data sets which are compatible with the 'bayesmeta'
package.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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

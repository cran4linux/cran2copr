%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ppsynth
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Partial-Pooling Synthetic Control with Multiple Outcomes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-parallel 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-parallel 

%description
Synthetic control for studies with several outcomes. Each outcome receives
its own donor weights, their dispersion around a common centroid is
penalized, no single penalty is ever selected (the estimator aggregates
over a penalty grid by leave-one-out exponential weighting), and the
resulting mass profile reports how much pooling the data support. One call
returns the per-outcome effects, the weights, the realized pooling, and
whole-pipeline placebo p-values. Implements the estimator of Grier (2026)
"Correlated Weights: Partial Pooling for Synthetic Control with Multiple
Outcomes" <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7149398>,
the common-weights corner of which is the estimator of Sun, Ben-Michael
and Feller (2025) <doi:10.1162/rest_a_01592>. The compiled engine and a
pure-R reference engine are certified against the Python engine behind the
'Stata' command 'ppsynth'.

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

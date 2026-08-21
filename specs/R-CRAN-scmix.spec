%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  scmix
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Model-Based Clustering with Sparse Conditional Mixture Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-stats 

%description
Fits Bayesian sparse conditional (Gaussian) mixture models for model-based
clustering. Each mixture component factorizes into a chain of univariate
polynomial regressions with per-component, per-equation Bayesian variable
selection under a centered Zellner g-prior; the number of clusters is
selected within a single run via an overfitted sparse mixture (Dirichlet
concentration 1/K). The blocked Gibbs sampler draws the selection sets
exactly by enumeration (or by validated single-flip Metropolis-Hastings in
higher dimension), is provably well-posed under a documented proper
fallback prior, and reports a label-invariant consensus partition (Dahl's
least-squares criterion). Companion package to Dong, Liao, and Lee (2026),
"Replacing three nested searches with one sweep: a Bayesian treatment of
sparse conditional mixture clustering". Multiple-imputation functionality
for the same engine is also exposed.

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

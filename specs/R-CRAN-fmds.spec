%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fmds
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Multidimensional Scaling Development Kit

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-stats 

%description
Multidimensional scaling (MDS) functions for various tasks that are beyond
the beta stage and way past the alpha stage. Currently, options are
available for weights, restrictions, classical scaling or principal
coordinate analysis, transformations (linear, power, Box-Cox, spline,
ordinal), outlier mitigation (rdop), out-of-sample estimation (predict),
negative dissimilarities, fast and faster executions with low memory
footprints, penalized restrictions, cross-validation-based penalty
selection, supplementary variable estimation (explain), additive constant
estimation, mixed measurement level distance calculation, restricted
classical scaling, etc. More will come in the future. References. Busing
(2024) "A Simple Population Size Estimator for Local Minima Applied to
Multidimensional Scaling". Manuscript submitted for publication. Busing
(2025) "Node Localization by Multidimensional Scaling with Iterative
Majorization". Manuscript submitted for publication. Busing (2025) "Faster
Multidimensional Scaling". Manuscript in preparation. Barroso and Busing
(2025) "e-RDOP, Relative Density-Based Outlier Probabilities, Extended to
Proximity Mapping". Manuscript submitted for publication.

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

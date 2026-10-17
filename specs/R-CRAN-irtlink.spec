%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  irtlink
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          IRT Linking and Linking Error Estimation Across Time Points and Groups

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-parallel 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 

%description
Estimation of trends in the mean and standard deviation of latent ability
distributions across the time points of educational assessments, and of
ability distribution differences across linked groups, for unidimensional
item response theory (IRT) models (1PL, 2PL, 3PL, partial credit, and
generalized partial credit). Groups connected through common items, with
independent or dependent person samples, are calibrated on an internal
marginal maximum likelihood EM engine, separately, concurrently, with
fixed item parameters, or with regularized calibration. Linking methods
include mean-mean and mean-geometric mean linking, Haberman linking
(Haberman, 2009, <doi:10.1002/j.2333-8504.2009.tb02197.x>) with robust Lp
loss and a pairwise variant (Robitzsch, 2025,
<doi:10.3390/appliedmath5010007>), and the response function methods of
Haebara and Stocking-Lord. Under differential item functioning (DIF), the
linked estimates depend on the selected common items, and the package
estimates this linking error together with the standard error by jackknife
and sandwich estimators, including bias-corrected variants (Robitzsch,
2024, <doi:10.3390/stats7030036>). RMSD and likelihood-ratio DIF
diagnostics with iterative purification are included.

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

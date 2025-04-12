%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cohetsurr
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Assessing Complex Heterogeneity in Surrogacy

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-grf 
Requires:         R-stats 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-grf 

%description
Provides functions to assess complex heterogeneity in the strength of a
surrogate marker with respect to multiple baseline covariates, in either a
randomized treatment setting or observational setting. For a randomized
treatment setting, the functions assess and test for heterogeneity using
both a parametric model and a semiparametric two-step model. More details
for the randomized setting are available in: Knowlton, R., Tian, L., &
Parast, L. (2025). "A General Framework to Assess Complex Heterogeneity in
the Strength of a Surrogate Marker," Statistics in Medicine, 44(5), e70001
<doi:10.1002/sim.70001>. For an observational setting, functions in this
package assess complex heterogeneity in the strength of a surrogate marker
using meta-learners, with options for different base learners. More
details for the observational setting will be available in the future in:
Knowlton, R., Parast, L. (2025) "Assessing Surrogate Heterogeneity in Real
World Data Using Meta-Learners." A tutorial for this package can be found
at <https://www.laylaparast.com/cohetsurr>.

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

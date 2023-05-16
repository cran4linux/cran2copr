%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  boostingDEA
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Boosting Approach to Data Envelopment Analysis

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rglpk 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lpSolveAPI 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MLmetrics 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rglpk 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lpSolveAPI 
Requires:         R-stats 
Requires:         R-CRAN-MLmetrics 
Requires:         R-methods 

%description
Includes functions to estimate production frontiers and make ideal output
predictions in the Data Envelopment Analysis (DEA) context using both
standard models from DEA and Free Disposal Hull (FDH) and boosting
techniques. In particular, EATBoosting (Guillen et al., 2023
<doi:10.1016/j.eswa.2022.119134>) and MARSBoosting. Moreover, the package
includes code for estimating several technical efficiency measures using
different models such as the input and output-oriented radial measures,
the input and output-oriented Russell measures, the Directional Distance
Function (DDF), the Weighted Additive Measure (WAM) and the Slacks-Based
Measure (SBM).

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

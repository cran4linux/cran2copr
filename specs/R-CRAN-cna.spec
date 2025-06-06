%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cna
%global packver   4.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Causal Modeling with Coincidence Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-car 
Requires:         R-CRAN-Rcpp 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-car 

%description
Provides comprehensive functionalities for causal modeling with
Coincidence Analysis (CNA), which is a configurational comparative method
of causal data analysis that was first introduced in Baumgartner (2009)
<doi:10.1177/0049124109339369>, and generalized in Baumgartner & Ambuehl
(2020) <doi:10.1017/psrm.2018.45>. CNA is designed to recover
INUS-causation from data, which is particularly relevant for analyzing
processes featuring conjunctural causation (component causation) and
equifinality (alternative causation). CNA is currently the only method for
INUS-discovery that allows for multiple effects (outcomes/endogenous
factors), meaning it can analyze common-cause and causal chain structures.
Moreover, as of version 4.0, it is the only method of its kind that
provides measures for model evaluation and selection that are custom-made
for the problem of INUS-discovery.

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

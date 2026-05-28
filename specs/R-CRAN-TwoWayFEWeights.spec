%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TwoWayFEWeights
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of the Weights Attached to the Two-Way Fixed Effects Regressions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-fixest 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-haven 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-fixest 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-haven 

%description
Computes the implicit weights attached to two-way fixed effects
regressions, as well as summary measures of these regressions' robustness
to heterogeneous treatment effects. Based on de Chaisemartin and
D'Haultfoeuille (2020) <DOI:10.1257/aer.20181169>.

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

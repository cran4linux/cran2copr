%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  crwbmetareg
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cluster Robust Wild Bootstrap Meta Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-Rfast2 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-Rfast2 
Requires:         R-CRAN-sandwich 
Requires:         R-stats 
Requires:         R-utils 

%description
In meta regression sometimes the studies have multiple effects that are
correlated. For this reason cluster robust standard errors must be
computed. However, since the clusters are unbalanced the wild bootstrap is
suggested. See Oczkowski E. and Doucouliagos H. (2015). "Wine prices and
quality ratings: a meta-regression analysis". American Journal of
Agricultural Economics, 97(1): 103--121. <doi:10.1093/ajae/aau057> and
Cameron A. C., Gelbach J. B. and Miller D. L. (2008). "Bootstrap-based
improvements for inference with clustered errors". The Review of Economics
and Statistics, 90(3): 414--427. <doi:10.1162/rest.90.3.414>.

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

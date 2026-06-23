%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  clusterSEs
%global packver   2.6.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6.6
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate Cluster-Robust p-Values and Confidence Intervals

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-dfidx 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-mlogit 
BuildRequires:    R-CRAN-plm 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-dfidx 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-mlogit 
Requires:         R-CRAN-plm 
Requires:         R-CRAN-sandwich 

%description
Calculate p-values and confidence intervals using cluster-adjusted
t-statistics (based on Ibragimov and Muller (2010)
<DOI:10.1198/jbes.2009.08046>, pairs cluster bootstrapped t-statistics,
and wild cluster bootstrapped t-statistics (the latter two techniques
based on Cameron, Gelbach, and Miller (2008) <DOI:10.1162/rest.90.3.414>.
Procedures are included for use with GLM, plm (pooling or fixed effects),
and mlogit models.

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

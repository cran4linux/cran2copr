%global __brp_check_rpaths %{nil}
%global packname  clusterSEs
%global packver   2.6.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6.5
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate Cluster-Robust p-Values and Confidence Intervals

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mlogit >= 1.1.0
BuildRequires:    R-CRAN-AER 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-plm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-dfidx 
Requires:         R-CRAN-mlogit >= 1.1.0
Requires:         R-CRAN-AER 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-plm 
Requires:         R-stats 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-lmtest 
Requires:         R-utils 
Requires:         R-CRAN-dfidx 

%description
Calculate p-values and confidence intervals using cluster-adjusted
t-statistics (based on Ibragimov and Muller (2010)
<DOI:10.1198/jbes.2009.08046>, pairs cluster bootstrapped t-statistics,
and wild cluster bootstrapped t-statistics (the latter two techniques
based on Cameron, Gelbach, and Miller (2008) <DOI:10.1162/rest.90.3.414>.
Procedures are included for use with GLM, ivreg, plm (pooling or fixed
effects), and mlogit models.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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

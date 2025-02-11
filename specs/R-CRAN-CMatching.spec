%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CMatching
%global packver   2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Matching Algorithms for Causal Inference with Clustered Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.6.0
Requires:         R-core >= 2.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matching 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-multiwayvcov 
BuildRequires:    R-CRAN-lme4 
Requires:         R-CRAN-Matching 
Requires:         R-stats 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-multiwayvcov 
Requires:         R-CRAN-lme4 

%description
Provides functions to perform matching algorithms for causal inference
with clustered data, as described in B. Arpino and M. Cannas (2016)
<doi:10.1002/sim.6880>. Pure within-cluster and preferential
within-cluster matching are implemented. Both algorithms provide causal
estimates with cluster-adjusted estimates of standard errors.

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

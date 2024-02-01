%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MarketMatching
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Market Matching and Causal Impact Inference

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-CausalImpact 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-bsts 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-Boom 
BuildRequires:    R-CRAN-utf8 
BuildRequires:    R-CRAN-dtw 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-utils 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-CausalImpact 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-bsts 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-Boom 
Requires:         R-CRAN-utf8 
Requires:         R-CRAN-dtw 

%description
For a given test market find the best control markets using time series
matching and analyze the impact of an intervention. The intervention could
be a marketing event or some other local business tactic that is being
tested. The workflow implemented in the Market Matching package utilizes
dynamic time warping (the 'dtw' package) to do the matching and the
'CausalImpact' package to analyze the causal impact. In fact, this package
can be considered a "workflow wrapper" for those two packages. In
addition, if you don't have a chosen set of test markets to match, the
Market Matching package can provide suggested test/control market pairs
and pseudo prospective power analysis (measuring causal impact at fake
interventions).

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

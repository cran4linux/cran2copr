%global __brp_check_rpaths %{nil}
%global packname  gmeta
%global packver   2.3-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Meta-Analysis via a Unified Framework of Confidence Distribution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-BiasedUrn 
BuildRequires:    R-CRAN-binom 
Requires:         R-stats 
Requires:         R-CRAN-BiasedUrn 
Requires:         R-CRAN-binom 

%description
An implementation of an all-in-one function for a wide range of
meta-analysis problems. It contains three functions. The gmeta() function
unifies all standard meta-analysis methods and also several newly
developed ones under a framework of combining confidence distributions
(CDs). Specifically, the package can perform classical p-value combination
methods (such as methods of Fisher, Stouffer, Tippett, etc.), fit
meta-analysis fixed-effect and random-effects models, and synthesizes 2x2
tables. Furthermore, it can perform robust meta-analysis, which provides
protection against model-misspecifications, and limits the impact of any
unknown outlying studies. In addition, the package implements two exact
meta-analysis methods from synthesizing 2x2 tables with rare events (e.g.,
zero total event). The np.gmeta() function summarizes information obtained
from multiple studies and makes inference for study-level parameters with
no distributional assumption. Specifically, it can construct confidence
intervals for unknown, fixed study-level parameters via confidence
distribution. Furthermore, it can perform estimation via asymptotic
confidence distribution whether tie or near tie condition exist or not.
The plot.gmeta() function to visualize individual and combined CDs through
extended forest plots is also available. Compared to version 2.2-6,
version 2.3-0 contains a new function np.gmeta().

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

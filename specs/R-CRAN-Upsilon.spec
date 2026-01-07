%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Upsilon
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Another Test of Association for Count Data

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.8
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-Rcpp >= 1.0.8
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-scales 

%description
The Upsilon test assesses association among categorical variables against
the null hypothesis of independence (Luo 2021 MS thesis; ProQuest
Publication No. 28649813). While promoting dominant function patterns, it
demotes non-dominant function patterns. It is robust to low expected
count---continuity correction like Yates's seems unnecessary. Using a
common null population following a uniform distribution, contingency
tables are comparable by statistical significance---not the case for most
association tests defining a varying null population by tensor product of
observed marginals. Although Pearson's chi-squared test, Fisher's exact
test, and Woolf's G-test (related to mutual information) are useful in
some contexts, the Upsilon test appeals to ranking association patterns
not necessarily following same marginal distributions, such as in count
data from DNA sequencing---an important modern scientific domain.

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

%global packname  qch
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Query Composed Hypotheses

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-mclust 
Requires:         R-stats 

%description
Provides functions for the joint analysis of K sets of p-values obtained
for a same list of items. This joint analysis is performed by querying a
composed hypothesis, i.e. an arbitrary complex combination of simple
hypotheses, as described in Mary-Huard et al. (2021) <arXiv:2104.14601>.
The null distribution corresponding to the composed hypothesis of interest
is obtained by fitting non-parametric mixtures models (one for each of the
simple hypothesis of the complex combination). Type I error rate control
is achieved through Bayesian False Discovery Rate control.  The 3 main
functions of the package GetHinfo(), qch.fit() and qch.test() correspond
to the 3 steps for querying a composed hypothesis (composed H0/H1
formulation, inferring the null distribution and testing the null
hypothesis).

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

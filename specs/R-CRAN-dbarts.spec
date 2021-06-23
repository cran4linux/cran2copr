%global __brp_check_rpaths %{nil}
%global packname  dbarts
%global packver   0.9-19
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.19
Release:          1%{?dist}%{?buildtag}
Summary:          Discrete Bayesian Additive Regression Trees Sampler

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-parallel 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-parallel 

%description
Fits Bayesian additive regression trees (BART; Chipman, George, and
McCulloch (2010) <doi:10.1214/09-AOAS285>) while allowing the updating of
predictors or response so that BART can be incorporated as a conditional
model in a Gibbs/Metropolis-Hastings sampler. Also serves as a drop-in
replacement for package 'BayesTree'.

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

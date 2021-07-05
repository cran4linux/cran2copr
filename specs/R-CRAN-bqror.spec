%global __brp_check_rpaths %{nil}
%global packname  bqror
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Quantile Regression for Ordinal Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-GIGrvg 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-NPflow 
BuildRequires:    R-CRAN-invgamma 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-pracma 
Requires:         R-tcltk 
Requires:         R-CRAN-GIGrvg 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-NPflow 
Requires:         R-CRAN-invgamma 

%description
Provides an estimation technique for Bayesian quantile regression in
ordinal models. Two algorithms are considered - one for an ordinal model
with three outcomes and the other for an ordinal model with more than 3
outcomes. It further provides model performance criteria and trace plots
for Markov chain Monte Carlo (MCMC) draws. Rahman, M. A. (2016)
<doi:10.1214/15-BA939>. Greenberg, E. (2012)
<doi:10.1017/CBO9781139058414>. Spiegelhalter, D. J., Best, N. G., Carlin
B. P. and Linde A. (2002) <doi:10.1111/1467-9868.00353>.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hdbayes
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Analysis of Generalized Linear Models with Historical Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-CRAN-instantiate >= 0.1.0
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-posterior 
BuildRequires:    R-CRAN-enrichwith 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-bridgesampling 
Requires:         R-CRAN-instantiate >= 0.1.0
Requires:         R-CRAN-callr 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-formula.tools 
Requires:         R-stats 
Requires:         R-CRAN-posterior 
Requires:         R-CRAN-enrichwith 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-bridgesampling 

%description
User-friendly functions for leveraging (multiple) historical data set(s)
for generalized linear models. Contains functions for sampling from the
posterior distribution of a generalized linear model using the prior
induced by the Bayesian hierarchical model, power prior by Ibrahim and
Chen (2000) <doi:10.1214/ss/1009212673>, normalized power prior by Duan et
al. (2006) <doi:10.1002/env.752>, normalized asymptotic power prior by
Ibrahim et al. (2015) <doi:10.1002/sim.6728>, commensurate prior by Hobbs
et al. (2011) <doi:10.1111/j.1541-0420.2011.01564.x>, robust
meta-analytic-predictive prior by Schmidli et al. (2014)
<doi:10.1111/biom.12242>, and the latent exchangeability prior (LEAP) by
Alt et al. (2023) <arXiv:2303.05223>. The package compiles all the
'CmdStan' models once during installation using the 'instantiate' package.

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

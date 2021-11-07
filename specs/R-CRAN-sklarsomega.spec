%global __brp_check_rpaths %{nil}
%global packname  sklarsomega
%global packver   3.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Measuring Agreement Using Sklar's Omega Coefficient

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-hash 
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mcmcse 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-dfoptim 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-hash 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mcmcse 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-spam 
Requires:         R-CRAN-dfoptim 

%description
Provides tools for applying Sklar's Omega (Hughes, 2018)
<arXiv:1803.02734> methodology to nominal scores, ordinal scores,
percentages, counts, amounts (i.e., non-negative real numbers), and
balances (i.e., any real number). The framework can accommodate any number
of units, any number of coders, and missingness; and can be used to
measure agreement with a gold standard, intra-coder agreement, and/or
inter-coder agreement. Frequentist inference is supported for all levels
of measurement. Bayesian inference is supported for continuous scores
only.

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

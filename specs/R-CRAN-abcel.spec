%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  abcel
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Empirical Likelihood-Based Approximate Bayesian Computation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-emplik 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-corpcor 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-emplik 
Requires:         R-methods 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-corpcor 

%description
Empirical likelihood-based approximate Bayesian Computation.  Approximates
the required posterior using empirical likelihood and estimated
differential entropy.  This is achieved without requiring any
specification of the likelihood or estimating equations that connects the
observations with the underlying parameters. The procedure is known to be
posterior consistent.  More details can be found in Chaudhuri, Ghosh, and
Kim (2024) <doi:10.1002/SAM.11711>.

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

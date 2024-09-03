%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EBcoBART
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Co-Data Learning for Bayesian Additive Regression Trees

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dbarts 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-CRAN-posterior 
BuildRequires:    R-CRAN-univariateML 
BuildRequires:    R-CRAN-extraDistr 
Requires:         R-CRAN-dbarts 
Requires:         R-CRAN-loo 
Requires:         R-CRAN-posterior 
Requires:         R-CRAN-univariateML 
Requires:         R-CRAN-extraDistr 

%description
Estimate prior variable weights for Bayesian Additive Regression Trees
(BART). These weights correspond to the probabilities of the variables
being selected in the splitting rules of the sum-of-trees. Weights are
estimated using empirical Bayes and external information on the
explanatory variables (co-data). BART models are fitted using the 'dbarts'
'R' package. See Goedhart and others (2023)
<doi:10.48550/arXiv.2311.09997> for details.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesOrdDesign
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Group Sequential Design for Ordinal Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ordinal 
BuildRequires:    R-CRAN-schoolmath 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-gsDesign 
BuildRequires:    R-CRAN-superdiag 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-madness 
BuildRequires:    R-CRAN-rjmcmc 
BuildRequires:    R-CRAN-R2jags 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-methods 
Requires:         R-CRAN-ordinal 
Requires:         R-CRAN-schoolmath 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-gsDesign 
Requires:         R-CRAN-superdiag 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-madness 
Requires:         R-CRAN-rjmcmc 
Requires:         R-CRAN-R2jags 
Requires:         R-CRAN-rjags 
Requires:         R-methods 

%description
The proposed group-sequential trial design is based on Bayesian methods
for ordinal endpoints, including three methods, the
proportional-odds-model (PO)-based, non-proportional-odds-model
(NPO)-based, and PO/NPO switch-model-based designs, which makes our
proposed methods generic to be able to deal with various scenarios.
Richard J. Barker, William A. Link (2013)
<doi:10.1080/00031305.2013.791644>. Thomas A. Murray, Ying Yuan, Peter F.
Thall, Joan H. Elizondo, Wayne L.Hofstetter (2018)
<doi:10.1111/biom.12842>. Chengxue Zhong, Haitao Pan, Hongyu Miao (2021)
<arXiv:2108.06568>.

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

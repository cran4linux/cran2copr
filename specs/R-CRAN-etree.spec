%global __brp_check_rpaths %{nil}
%global packname  etree
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Classification and Regression with Structured and Mixed-Type Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.7.0
Requires:         R-core >= 3.7.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fda.usc >= 2.0.0
BuildRequires:    R-CRAN-brainGraph 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-energy 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-NetworkDistance 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-TDA 
BuildRequires:    R-CRAN-usedist 
Requires:         R-CRAN-fda.usc >= 2.0.0
Requires:         R-CRAN-brainGraph 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-energy 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-NetworkDistance 
Requires:         R-parallel 
Requires:         R-CRAN-partykit 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-TDA 
Requires:         R-CRAN-usedist 

%description
Implementation of Energy Trees, a statistical model to perform
classification and regression with structured and mixed-type data. The
model has a similar structure to Conditional Trees, but brings in Energy
Statistics to test independence between variables that are possibly
structured and of different nature. Currently, the package covers
functions and graphs as structured covariates. It builds upon 'partykit'
to provide functionalities for fitting, printing, plotting, and predicting
with Energy Trees. Energy Trees are described in Giubilei et al. (2022)
<arXiv:2207.04430>.

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

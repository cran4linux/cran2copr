%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gsbm
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Parameters in the Generalized SBM

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-softImpute 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-softImpute 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-foreach 

%description
Given an adjacency matrix drawn from a Generalized Stochastic Block Model
with missing observations, this package robustly estimates the
probabilities of connection between nodes and detects outliers nodes, as
describes in Gaucher, Klopp and Robin (2019) <arXiv:1911.13122>.

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

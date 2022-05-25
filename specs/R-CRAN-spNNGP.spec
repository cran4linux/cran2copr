%global __brp_check_rpaths %{nil}
%global packname  spNNGP
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Regression Models for Large Datasets using Nearest Neighbor Gaussian Processes

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-methods 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-RANN 
Requires:         R-methods 

%description
Fits univariate Bayesian spatial regression models for large datasets
using Nearest Neighbor Gaussian Processes (NNGP) detailed in Finley,
Datta, Banerjee (2020) <arXiv:2001.09111>, and Finley, Datta, Cook,
Morton, Andersen, and Banerjee (2019) <doi:10.1080/10618600.2018.1537924>
and Datta, Banerjee, Finley, and Gelfand (2016)
<doi:10.1080/01621459.2015.1044091>.

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

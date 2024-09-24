%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GPTreeO
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Dividing Local Gaussian Processes for Online Learning Regression

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-hash 
BuildRequires:    R-CRAN-DiceKriging 
BuildRequires:    R-CRAN-mlegp 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-hash 
Requires:         R-CRAN-DiceKriging 
Requires:         R-CRAN-mlegp 

%description
We implement and extend the Dividing Local Gaussian Process algorithm by
Lederer et al. (2020) <doi:10.48550/arXiv.2006.09446>. Its main use case
is in online learning where it is used to train a network of local GPs
(referred to as tree) by cleverly partitioning the input space. In
contrast to a single GP, 'GPTreeO' is able to deal with larger amounts of
data. The package includes methods to create the tree and set its
parameter, incorporating data points from a data stream as well as making
joint predictions based on all relevant local GPs.

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

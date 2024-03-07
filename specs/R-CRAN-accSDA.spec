%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  accSDA
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Accelerated Sparse Discriminant Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.45
BuildRequires:    R-grid >= 3.2.2
BuildRequires:    R-CRAN-gridExtra >= 2.2
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
Requires:         R-CRAN-MASS >= 7.3.45
Requires:         R-grid >= 3.2.2
Requires:         R-CRAN-gridExtra >= 2.2
Requires:         R-CRAN-ggplot2 >= 2.1.0

%description
Implementation of sparse linear discriminant analysis, which is a
supervised classification method for multiple classes. Various novel
optimization approaches to this problem are implemented including
alternating direction method of multipliers ('ADMM'), proximal gradient
(PG) and accelerated proximal gradient ('APG') (See Atkins 'et al'.
<arXiv:1705.07194>). Functions for performing cross validation are also
supplied along with basic prediction and plotting functions. Sparse zero
variance discriminant analysis ('SZVD') is also included in the package
(See Ames and Hong, <arXiv:1401.5492>). See the 'github' wiki for a more
extended description.

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

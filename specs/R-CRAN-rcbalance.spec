%global __brp_check_rpaths %{nil}
%global packname  rcbalance
%global packver   1.8.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.6
Release:          1%{?dist}%{?buildtag}
Summary:          Large, Sparse Optimal Matching with Refined Covariate Balance

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-plyr 

%description
Tools for large, sparse optimal matching of treated units and control
units in observational studies.  Provisions are made for refined covariate
balance constraints, which include fine and near-fine balance as special
cases.  Matches are optimal in the sense that they are computed as
solutions to network optimization problems rather than greedy algorithms.
See Pimentel, et al.(2015) <doi:10.1080/01621459.2014.997879> and Pimentel
(2016), Obs. Studies 2(1):4-23.  The optmatch package, which is useful for
running many of the provided functions, may be downloaded from Github at
<https://github.com/markmfredrickson/optmatch> if not available on CRAN.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LHD
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Latin Hypercube Designs (LHDs)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-numbers 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-CRAN-numbers 
Requires:         R-utils 

%description
Contains different algorithms and construction methods for optimal Latin
hypercube designs (LHDs) with flexible sizes. Our package is comprehensive
since it is capable of generating maximin distance LHDs, maximum
projection LHDs, and orthogonal and nearly orthogonal LHDs. Detailed
comparisons and summary of all the algorithms and construction methods in
this package can be found at Hongzhi Wang, Qian Xiao and Abhyuday Mandal
(2021) <doi:10.48550/arXiv.2010.09154>. This package is particularly
useful in the area of Design and Analysis of Experiments (DAE). More
specifically, design of computer experiments.

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

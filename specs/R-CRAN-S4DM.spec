%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  S4DM
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Small Sample Size Species Distribution Modeling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-densratio 
BuildRequires:    R-CRAN-flexclust 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-maxnet 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-np 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-robust 
BuildRequires:    R-CRAN-rvinecopulib 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-densratio 
Requires:         R-CRAN-flexclust 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-maxnet 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-np 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-robust 
Requires:         R-CRAN-rvinecopulib 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Rdpack 

%description
Implements a set of distribution modeling methods that are suited to
species with small sample sizes (e.g., poorly sampled species or rare
species). While these methods can also be used on well-sampled taxa, they
are united by the fact that they can be utilized with relatively few data
points. More details on the currently implemented methodologies can be
found in Drake and Richards (2018) <doi:10.1002/ecs2.2373>, Drake (2015)
<doi:10.1098/rsif.2015.0086>, and Drake (2014) <doi:10.1890/ES13-00202.1>.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  IVPP
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Invariance Partial Pruning Test

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bootnet 
BuildRequires:    R-CRAN-clusterGeneration 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-psychonetrics 
BuildRequires:    R-CRAN-graphicalVAR 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-future 
Requires:         R-CRAN-bootnet 
Requires:         R-CRAN-clusterGeneration 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-psychonetrics 
Requires:         R-CRAN-graphicalVAR 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-future 

%description
An implementation of the Invariance Partial Pruning (IVPP) approach
described in Du, X., Johnson, S. U., Epskamp, S. (2025) The Invariance
Partial Pruning Approach to The Network Comparison in Longitudinal Data.
IVPP is a two-step method that first test for global network structural
difference with invariance test and then inspect specific edge difference
with partial pruning.

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

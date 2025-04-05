%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SimComp
%global packver   3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.6
Release:          1%{?dist}%{?buildtag}
Summary:          Simultaneous Comparisons for Multiple Endpoints

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-mratios 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-mratios 
Requires:         R-graphics 
Requires:         R-stats 

%description
Simultaneous tests and confidence intervals are provided for one-way
experimental designs with one or many normally distributed, primary
response variables (endpoints). Differences (Hasler and Hothorn, 2011
<doi:10.2202/1557-4679.1258>) or ratios (Hasler and Hothorn, 2012
<doi:10.1080/19466315.2011.633868>) of means can be considered. Various
contrasts can be chosen, unbalanced sample sizes are allowed as well as
heterogeneous variances (Hasler and Hothorn, 2008
<doi:10.1002/bimj.200710466>) or covariance matrices (Hasler, 2014
<doi:10.1515/ijb-2012-0015>).

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

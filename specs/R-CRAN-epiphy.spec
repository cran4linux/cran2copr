%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  epiphy
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Plant Disease Epidemics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-transport 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-transport 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-Rcpp 

%description
A toolbox to make it easy to analyze plant disease epidemics. It provides
a common framework for plant disease intensity data recorded over time
and/or space. Implemented statistical methods are currently mainly focused
on spatial pattern analysis (e.g., aggregation indices, Taylor and binary
power laws, distribution fitting, SADIE and 'mapcomp' methods). See
Laurence V. Madden, Gareth Hughes, Franck van den Bosch (2007)
<doi:10.1094/9780890545058> for further information on these methods.
Several data sets that were mainly published in plant disease epidemiology
literature are also included in this package.

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

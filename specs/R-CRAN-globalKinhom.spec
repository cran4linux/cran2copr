%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  globalKinhom
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Inhomogeneous K- And Pair Correlation Functions Using Global Estimators

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-spatstat.geom >= 3.1
BuildRequires:    R-CRAN-spatstat.explore >= 3.0
BuildRequires:    R-CRAN-spatstat.random >= 2.1.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-spatstat.geom >= 3.1
Requires:         R-CRAN-spatstat.explore >= 3.0
Requires:         R-CRAN-spatstat.random >= 2.1.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 

%description
Second-order summary statistics K- and pair-correlation functions describe
interactions in point pattern data. This package provides computations to
estimate those statistics on inhomogeneous point processes, using the
methods of in T Shaw, J Møller, R Waagepetersen, 2020 <arXiv:2004.00527>.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  logbin
%global packver   2.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Relative Risk Regression Using the Log-Binomial Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-turboEM >= 2021
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-glm2 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-itertools2 
BuildRequires:    R-CRAN-iterators 
Requires:         R-CRAN-turboEM >= 2021
Requires:         R-splines 
Requires:         R-CRAN-glm2 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-itertools2 
Requires:         R-CRAN-iterators 

%description
Methods for fitting log-link GLMs and GAMs to binomial data, including
EM-type algorithms with more stable convergence properties than standard
methods.

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

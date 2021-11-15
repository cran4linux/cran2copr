%global __brp_check_rpaths %{nil}
%global packname  GeneNet
%global packver   1.2.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.16
Release:          1%{?dist}%{?buildtag}
Summary:          Modeling and Inferring Gene Networks

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-corpcor >= 1.6.10
BuildRequires:    R-CRAN-fdrtool >= 1.2.17
BuildRequires:    R-CRAN-longitudinal >= 1.1.13
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-corpcor >= 1.6.10
Requires:         R-CRAN-fdrtool >= 1.2.17
Requires:         R-CRAN-longitudinal >= 1.1.13
Requires:         R-stats 
Requires:         R-grDevices 

%description
Analyzes gene expression (time series) data with focus on the inference of
gene networks. In particular, GeneNet implements the methods of Schaefer
and Strimmer (2005a,b,c) and Opgen-Rhein and Strimmer (2006, 2007) for
learning large-scale gene association networks (including assignment of
putative directions).

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

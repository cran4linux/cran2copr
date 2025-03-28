%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ICSShiny
%global packver   0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6
Release:          1%{?dist}%{?buildtag}
Summary:          ICS via a Shiny Application

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ICS 
BuildRequires:    R-CRAN-ICSOutlier 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-ICSNP 
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-CRAN-simsalapar 
BuildRequires:    R-CRAN-DT 
Requires:         R-CRAN-ICS 
Requires:         R-CRAN-ICSOutlier 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-ICSNP 
Requires:         R-CRAN-rrcov 
Requires:         R-CRAN-simsalapar 
Requires:         R-CRAN-DT 

%description
Performs Invariant Coordinate Selection (ICS) (Tyler, Critchley, Duembgen
and Oja (2009) <doi:10.1111/j.1467-9868.2009.00706.x>) and especially ICS
for multivariate outlier detection with application to quality control
(Archimbaud, Nordhausen, Ruiz-Gazen (2018)
<doi:10.1016/j.csda.2018.06.011>) using a shiny app.

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

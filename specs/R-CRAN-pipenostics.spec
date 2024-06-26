%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pipenostics
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Diagnostics, Reliability and Predictive Maintenance of Pipeline Systems

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-iapws 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-iapws 

%description
Functions representing some useful empirical and data-driven models of
heat loss, corrosion diagnostics, reliability and predictive maintenance
of pipeline systems. The package is an option for technical engineering
departments of heat generating and heat transfer companies that use or
plan to use regulatory calculations in their activities. Methods are
described in Timashev et al. (2016) <doi:10.1007/978-3-319-25307-7>,
A.C.Reddy (2017) <doi:10.1016/j.matpr.2017.07.081>, Minenergo (2008)
<https://docs.cntd.ru/document/902148459>, Minenergo (2005)
<https://docs.cntd.ru/document/1200035568>, Xing LU. (2014)
<doi:10.1080/23744731.2016.1258371>.

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

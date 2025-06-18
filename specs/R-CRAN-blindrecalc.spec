%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  blindrecalc
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Blinded Sample Size Recalculation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 

%description
Computation of key characteristics and plots for blinded sample size
recalculation. Continuous as well as binary endpoints are supported in
superiority and non-inferiority trials. See Baumann, Pilz, Kieser (2022)
<doi:10.32614/RJ-2022-001> for a detailed description. The implemented
methods include the approaches by Lu, K. (2019) <doi:10.1002/pst.1737>,
Kieser, M. and Friede, T. (2000)
<doi:10.1002/(SICI)1097-0258(20000415)19:7%%3C901::AID-SIM405%%3E3.0.CO;2-L>,
Friede, T. and Kieser, M. (2004) <doi:10.1002/pst.140>, Friede, T.,
Mitchell, C., Mueller-Veltern, G. (2007) <doi:10.1002/bimj.200610373>, and
Friede, T. and Kieser, M. (2011) <doi:10.3414/ME09-01-0063>.

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

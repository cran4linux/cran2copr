%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  possum
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Surgical Risk Prediction with the POSSUM Score Family

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Computes the Physiological and Operative Severity Score for the
enUmeration of Mortality and morbidity (POSSUM), its Portsmouth
modification (P-POSSUM), and the colorectal (CR-POSSUM), vascular
(V-POSSUM) and ruptured aortic aneurysm (RAAA-POSSUM) variants,
risk-adjustment systems used in surgical audit. Functions map
physiological and operative variables to their component scores and return
the predicted probabilities of morbidity and mortality from the published
logistic equations. The coefficients follow Copeland and others (1991)
<doi:10.1002/bjs.1800780327> for POSSUM, Prytherch and others (1998)
<doi:10.1046/j.1365-2168.1998.00840.x> for P-POSSUM, Tekkis and others
(2004) <doi:10.1002/bjs.4430> for the colorectal variant (CR-POSSUM), and
Neary and others (2003) <doi:10.1002/bjs.4041> for the vascular variant
(V-POSSUM). The package is intended for audit and research; it is not a
validated medical device and must not be used as the sole basis for
clinical decisions.

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

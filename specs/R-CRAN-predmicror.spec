%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  predmicror
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting Predictive Microbiology Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-gslnls 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-gslnls 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides predictive microbiology model functions and convenience wrappers
for fitting primary growth, microbial inactivation, dynamic, omnibus, and
cardinal parameter models to experimental data using nonlinear least
squares and related mixed-effects or time-varying workflows. Includes
helper functions for extracting fitted values, calculating model
diagnostics, and comparing fitted models. Implemented model families
include those described by: Zwietering et al. (1990)
<doi:10.1128/AEM.56.6.1875-1881.1990>, Baranyi and Roberts (1994)
<doi:10.1016/0168-1605(94)90157-0>, Baranyi and Roberts (1995)
<doi:10.1016/0168-1605(94)00121-L>, Buchanan et al. (1997)
<doi:10.1006/fmic.1997.0125>, Richards (1959) <doi:10.1093/jxb/10.2.290>,
Fang et al. (2012) <doi:10.1111/j.1750-3841.2012.02873.x>, Fang et al.
(2013) <doi:10.1016/j.fm.2012.12.005>, Huang (2008)
<doi:10.1111/j.1750-3841.2008.00785.x>, Huang (2009)
<doi:10.1016/j.jfoodeng.2008.07.011>, Huang (2013)
<doi:10.1016/j.foodcont.2012.11.019>, Geeraerd et al. (2005)
<doi:10.1016/j.ijfoodmicro.2004.11.038>, van Boekel (2002)
<doi:10.1016/S0168-1605(01)00742-5>, Peleg (1999)
<doi:10.1016/S0963-9969(99)00081-2>, Mafart et al. (2002)
<doi:10.1016/S0168-1605(01)00624-9>, Albert and Mafart (2005)
<doi:10.1016/j.ijfoodmicro.2004.10.016>, Rosso et al. (1993)
<doi:10.1006/jtbi.1993.1099>, Rosso et al. (1995)
<doi:10.1128/AEM.61.2.610-616.1995>, and Rosso et al. (1996)
<doi:10.4315/0362-028X-59.9.944>.

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

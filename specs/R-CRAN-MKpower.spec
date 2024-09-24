%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MKpower
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Power Analysis and Sample Size Calculation

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MKinfer >= 0.4
BuildRequires:    R-CRAN-matrixTests >= 0.2
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MKdescr 
BuildRequires:    R-CRAN-qqplotr 
BuildRequires:    R-CRAN-coin 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-MKinfer >= 0.4
Requires:         R-CRAN-matrixTests >= 0.2
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MKdescr 
Requires:         R-CRAN-qqplotr 
Requires:         R-CRAN-coin 
Requires:         R-CRAN-mvtnorm 

%description
Power analysis and sample size calculation for Welch and Hsu (Hedderich
and Sachs (2018), ISBN:978-3-662-56657-2) t-tests including Monte-Carlo
simulations of empirical power and type-I-error. Power and sample size
calculation for Wilcoxon rank sum and signed rank tests via Monte-Carlo
simulations. Power and sample size required for the evaluation of a
diagnostic test(-system) (Flahault et al. (2005),
<doi:10.1016/j.jclinepi.2004.12.009>; Dobbin and Simon (2007),
<doi:10.1093/biostatistics/kxj036>) as well as for a single proportion
(Fleiss et al. (2003), ISBN:978-0-471-52629-2; Piegorsch (2004),
<doi:10.1016/j.csda.2003.10.002>; Thulin (2014), <doi:10.1214/14-ejs909>),
comparing two negative binomial rates (Zhu and Lakkis (2014),
<doi:10.1002/sim.5947>), ANCOVA (Shieh (2020),
<doi:10.1007/s11336-019-09692-3>), reference ranges (Jennen-Steinmetz and
Wellek (2005), <doi:10.1002/sim.2177>), multiple primary endpoints (Sozu
et al. (2015), ISBN:978-3-319-22005-5), and AUC (Hanley and McNeil (1982),
<doi:10.1148/radiology.143.1.7063747>).

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

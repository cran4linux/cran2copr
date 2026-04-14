%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qDEA
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Quantile Data Envelopment Analysis

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-doBy 
BuildRequires:    R-CRAN-highs 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-doBy 
Requires:         R-CRAN-highs 
Requires:         R-CRAN-Matrix 
Requires:         R-utils 

%description
R implementation of Quantile Data Envelopment Analysis. The package 'qDEA'
allows a user specified proportion of observations to lie external to a
given Decision Making Units's (DMU's)reference hyperplane. 'qDEA' can be
used to detect and address influential outliers or to implement quantile
benchmarking, as discussed in Atwood and Shaik (2020). Quantile
benchmarking is accomplished by using heuristic procedures to find a DMU's
closest input-output projection point in a specified direction while
allowing a specified proportion of observations to lie external to the
projected point's hyperplane. The 'qDEA' package accommodates standard
(DEA) and quantile DEA estimation, returns to scale
CRS(constant),VRS(variable),DRS(decreasing) or IRS(increasing), the use of
directional vectors, bias correction through subsample bootstrapping and
subsample size selection procedures. The user can also recover each DMU's
reference DMUs and external DMUs if desired. The implemented procedures
are based on discussions in: Atwood and Shaik (2020)
<doi:10.1016/j.ejor.2020.03.054> Atwood and Shaik (2018)
<doi:10.1007/978-3-319-68678-3_4> Walden and Atwood (2023)
<doi:10.1086/724932> Walden and Atwood (2025) <doi:10.1086/736554>.

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

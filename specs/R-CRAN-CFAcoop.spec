%global __brp_check_rpaths %{nil}
%global packname  CFAcoop
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Colony Formation Assay: Taking into Account Cellular Cooperation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc 
Requires:         R-CRAN-Hmisc 

%description
Cellular cooperation compromises the plating efficiency-based analysis of
clonogenic survival data. This tool provides functions that enable a
robust analysis of colony formation assay (CFA) data in presence or
absence of cellular cooperation. The implemented method has been described
in Brix et al. (2020). (Brix, N., Samaga, D., Hennel, R. et al. "The
clonogenic assay: robustness of plating efficiency-based analysis is
strongly compromised by cellular cooperation." Radiat Oncol 15, 248
(2020). <doi:10.1186/s13014-020-01697-y>) Power regression for parameter
estimation, calculation of survival fractions, uncertainty analysis and
plotting functions are provided.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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

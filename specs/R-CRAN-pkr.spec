%global __brp_check_rpaths %{nil}
%global packname  pkr
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Pharmacokinetics in R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.0
Requires:         R-core >= 2.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-foreign 
BuildRequires:    R-CRAN-binr 
BuildRequires:    R-CRAN-forestplot 
BuildRequires:    R-CRAN-rtf 
Requires:         R-CRAN-foreign 
Requires:         R-CRAN-binr 
Requires:         R-CRAN-forestplot 
Requires:         R-CRAN-rtf 

%description
Conduct a noncompartmental analysis as closely as possible to the most
widely used commercial software. Some features are 1) CDISC SDTM terms 2)
Automatic slope selection with the same criterion of WinNonlin(R) 3)
Supporting both 'linear-up linear-down' and 'linear-up log-down' method 4)
Interval(partial) AUCs with 'linear' or 'log' interpolation method *
Reference: Gabrielsson J, Weiner D. Pharmacokinetic and Pharmacodynamic
Data Analysis - Concepts and Applications. 5th ed. 2016.
(ISBN:9198299107).

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

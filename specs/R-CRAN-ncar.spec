%global packname  ncar
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Noncompartmental Analysis for Pharmacokinetic Report

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-NonCompart >= 0.3.3
BuildRequires:    R-CRAN-rtf 
Requires:         R-CRAN-NonCompart >= 0.3.3
Requires:         R-CRAN-rtf 

%description
Conduct a noncompartmental analysis with industrial strength. Some
features are 1) CDISC SDTM terms 2) Automatic or manual slope selection 3)
Supporting both 'linear-up linear-down' and 'linear-up log-down' method 4)
Interval(partial) AUCs with 'linear' or 'log' interpolation method 5)
Produce pdf, rtf, text report files. * Reference: Gabrielsson J, Weiner D.
Pharmacokinetic and Pharmacodynamic Data Analysis - Concepts and
Applications. 5th ed. 2016. (ISBN:9198299107).

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

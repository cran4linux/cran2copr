%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bondAnalyst
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Methods for Fixed-Income Valuation, Risk and Return

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 

%description
Bond Pricing and Fixed-Income Valuation of Selected Securities included
here serve as a quick reference of Quantitative Methods for undergraduate
courses on Fixed-Income and CFA Level I Readings on Fixed-Income
Valuation, Risk and Return. CFA Institute ("CFA Program Curriculum 2020
Level I Volumes 1-6. (Vol. 5, pp. 107-151, pp. 237-299)", 2019, ISBN:
9781119593577). Barbara S. Petitt ("Fixed Income Analysis", 2019, ISBN:
9781119628132). Frank J. Fabozzi ("Handbook of Finance: Financial Markets
and Instruments", 2008, ISBN: 9780470078143). Frank J. Fabozzi ("Fixed
Income Analysis", 2007, ISBN: 9780470052211).

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

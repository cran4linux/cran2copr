%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ragtop
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Pricing Equity Derivatives with Extensions of Black-Scholes

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-methods >= 3.2.2
BuildRequires:    R-CRAN-limSolve >= 2.0.1
BuildRequires:    R-CRAN-futile.logger >= 1.4.1
Requires:         R-methods >= 3.2.2
Requires:         R-CRAN-limSolve >= 2.0.1
Requires:         R-CRAN-futile.logger >= 1.4.1

%description
Algorithms to price American and European equity options, convertible
bonds and a variety of other financial derivatives. It uses an extension
of the usual Black-Scholes model in which jump to default may occur at a
probability specified by a power-law link between stock price and hazard
rate as found in the paper by Takahashi, Kobayashi, and Nakagawa (2001)
<doi:10.3905/jfi.2001.319302>.  We use ideas and techniques from Andersen
and Buffum (2002) <doi:10.2139/ssrn.355308> and Linetsky (2006)
<doi:10.1111/j.1467-9965.2006.00271.x>.

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

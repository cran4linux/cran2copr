%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  elitism
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Equipment for Logarithmic and Linear Time Stepwise Multiple Hypothesis Testing

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.0.0
BuildRequires:    R-stats >= 4.0.0
Requires:         R-CRAN-MASS >= 7.0.0
Requires:         R-stats >= 4.0.0

%description
Recently many new p-value based multiple test procedures have been
proposed, and these new methods are more powerful than the widely used
Hochberg procedure. These procedures strongly control the familywise error
rate (FWER). This is a comprehensive collection of p-value based
FWER-control stepwise multiple test procedures, including six procedure
families and thirty multiple test procedures. In this collection, the
conservative Hochberg procedure, linear time Hommel procedures, asymptotic
Rom procedure, Gou-Tamhane-Xi-Rom procedures, and Quick procedures are all
developed in recent five years since 2014. The package name "elitism" is
an acronym of "e"quipment for "l"ogarithmic and l"i"near "ti"me "s"tepwise
"m"ultiple hypothesis testing. See Gou, J. (2022), "Quick multiple test
procedures and p-value adjustments", Statistics in Biopharmaceutical
Research 14(4), 636-650.

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

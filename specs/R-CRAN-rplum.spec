%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rplum
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Age-Depth Modelling of Cores Dated by Pb-210

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rbacon >= 3.5.2
BuildRequires:    R-CRAN-rintcal >= 1.1.3
BuildRequires:    R-CRAN-rice >= 1.1.1
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-rbacon >= 3.5.2
Requires:         R-CRAN-rintcal >= 1.1.3
Requires:         R-CRAN-rice >= 1.1.1
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
An approach to age-depth modelling that uses Bayesian statistics to
reconstruct accumulation histories for 210Pb-dated deposits using prior
information. It can combine 210Pb, radiocarbon, and other dates in the
chronologies. See Aquino et al. (2018) <doi:10.1007/s13253-018-0328-7>.
Note that parts of the code underlying 'rplum' are derived from the
'rbacon' package by the same authors, and there remains a degree of
overlap between the two packages.

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

%global __brp_check_rpaths %{nil}
%global packname  BTYD
%global packver   2.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Implementing BTYD Models with the Log Sum Exp Patch

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-hypergeo 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-hypergeo 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Matrix 

%description
Functions for data preparation, parameter estimation, scoring, and
plotting for the BG/BB (Fader, Hardie, and Shang 2010
<doi:10.1287/mksc.1100.0580>), BG/NBD (Fader, Hardie, and Lee 2005
<doi:10.1287/mksc.1040.0098>) and Pareto/NBD and Gamma/Gamma (Fader,
Hardie, and Lee 2005 <doi:10.1509/jmkr.2005.42.4.415>) models.

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

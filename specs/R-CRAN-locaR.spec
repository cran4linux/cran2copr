%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  locaR
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Set of Tools for Sound Localization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-seewave 
BuildRequires:    R-CRAN-tuneR 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-oce 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-SynchWave 
Requires:         R-CRAN-seewave 
Requires:         R-CRAN-tuneR 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-oce 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-SynchWave 

%description
A set of functions and tools to conduct acoustic source localization, as
well as organize and check localization data and results. The localization
functions implement the modified steered response power algorithm
described by Cobos et al. (2010) <doi:10.1109/LSP.2010.2091502>.

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

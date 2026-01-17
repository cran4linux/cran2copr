%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NMAR
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation under not Missing at Random Nonresponse

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-Formula 
Requires:         R-stats 
Requires:         R-CRAN-nleqslv 
Requires:         R-utils 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-Formula 

%description
Methods to estimate finite-population parameters under nonresponse that is
not missing at random (NMAR, nonignorable). Incorporates auxiliary
information and user-specified response models, and supports independent
samples and complex survey designs via objects from the 'survey' package.
Provides diagnostics and optional variance estimates. For methodological
background see Qin, Leung and Shao (2002) <doi:10.1198/016214502753479338>
and Riddles, Kim and Im (2016) <doi:10.1093/jssam/smv047>.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  surveyverse
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Easily Install and Load Survey Analysis Packages

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-srvyr 
BuildRequires:    R-CRAN-svrep 
BuildRequires:    R-CRAN-svyVGAM 
BuildRequires:    R-CRAN-svylme 
BuildRequires:    R-stats 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-srvyr 
Requires:         R-CRAN-svrep 
Requires:         R-CRAN-svyVGAM 
Requires:         R-CRAN-svylme 
Requires:         R-stats 

%description
Makes it easy to install and load a collection of packages for survey
analysis that build upon the foundational 'survey' package of Lumley
(2004) <doi:10.18637/jss.v009.i08>. Schneider (2025)
<https://isi-iass.org/home/wp-content/uploads/Survey_Statistician_2025_January_N91_06.pdf>
describes the three core packages in this collection.

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

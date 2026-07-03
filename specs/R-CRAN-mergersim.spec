%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mergersim
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Merger Simulation and Calibration

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-stats 
Requires:         R-CRAN-BB 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-rootSolve 
Requires:         R-stats 

%description
Analyze mergers between firms. Models of competition include
differentiated Bertrand price-setting, Nash bargaining, and second score
auctions, as implemented in Panhans and Taragin (2023)
<doi:10.1016/j.ijindorg.2023.102986>. Calibrates demand systems including
standard logit, nested logit, and generalized nested logit as implemented
in Panhans and Wiemer (2026) <doi:10.1093/joclec/nhaf037>.

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

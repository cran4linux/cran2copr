%global __brp_check_rpaths %{nil}
%global packname  winRatioAnalysis
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimates the Win-Ratio as a Function of Time

License:          GNU Affero General Public License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-pssm 
BuildRequires:    R-CRAN-MLEcens 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-JM 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-pssm 
Requires:         R-CRAN-MLEcens 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-JM 
Requires:         R-CRAN-mvtnorm 

%description
Fits a model to data separately for each treatment group and then
calculates the win-Ratio as a function of follow-up time.

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

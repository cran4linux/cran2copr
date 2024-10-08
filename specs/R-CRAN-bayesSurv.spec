%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bayesSurv
%global packver   3.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.8
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Survival Regression with Flexible Error and Random Effects Distributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-smoothSurv 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-smoothSurv 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Contains Bayesian implementations of the Mixed-Effects Accelerated Failure
Time (MEAFT) models for censored data. Those can be not only
right-censored but also interval-censored, doubly-interval-censored or
misclassified interval-censored. The methods implemented in the package
have been published in Komárek and Lesaffre (2006, Stat. Modelling)
<doi:10.1191/1471082X06st107oa>, Komárek, Lesaffre and Legrand (2007,
Stat. in Medicine) <doi:10.1002/sim.3083>, Komárek and Lesaffre (2007,
Stat. Sinica)
<https://www3.stat.sinica.edu.tw/statistica/oldpdf/A17n27.pdf>, Komárek
and Lesaffre (2008, JASA) <doi:10.1198/016214507000000563>,
García-Zattera, Jara and Komárek (2016, Biometrics)
<doi:10.1111/biom.12424>.

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

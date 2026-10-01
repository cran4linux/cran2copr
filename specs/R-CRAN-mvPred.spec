%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mvPred
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Methods for Handling Missing Values in Linear Modeling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-regtools 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-Amelia 
BuildRequires:    R-CRAN-missForest 
BuildRequires:    R-CRAN-toweranNA 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-qeML 
Requires:         R-CRAN-regtools 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-Amelia 
Requires:         R-CRAN-missForest 
Requires:         R-CRAN-toweranNA 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-qeML 

%description
Provides user-friendly methods for handling missing data in regression
modeling, including available-case linear regression, multiple imputation,
random-forest imputation, and the Tower method. Implemented approaches
include chained-equation imputation described by van Buuren and
Groothuis-Oudshoorn (2011) <doi:10.18637/jss.v045.i03>, multiple
imputation described by Honaker, King and Blackwell (2011)
<doi:10.18637/jss.v045.i07>, random-forest imputation described by
Stekhoven and Buehlmann (2012) <doi:10.1093/bioinformatics/btr597>, and
the Tower method described by Matloff and Mohanty (2023)
<https://CRAN.R-project.org/package=toweranNA>.

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

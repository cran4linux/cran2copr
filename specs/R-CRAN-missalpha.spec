%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  missalpha
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Find Range of Cronbach Alpha with a Dataset Including Missing Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-GA 
BuildRequires:    R-CRAN-DEoptim 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-stats 
Requires:         R-CRAN-GA 
Requires:         R-CRAN-DEoptim 
Requires:         R-CRAN-nloptr 
Requires:         R-stats 

%description
Provides functions to calculate the minimum and maximum possible values of
Cronbach's alpha when item-level missing data are present. Cronbach's
alpha (Cronbach, 1951 <doi:10.1007/BF02310555>) is one of the most widely
used measures of internal consistency in the social, behavioral, and
medical sciences (Bland & Altman, 1997 <doi:10.1136/bmj.314.7080.572>;
Tavakol & Dennick, 2011 <doi:10.5116/ijme.4dfb.8dfd>). However,
conventional implementations assume complete data, and listwise deletion
is often applied when missingness occurs, which can lead to biased or
overly optimistic reliability estimates (Enders, 2003
<doi:10.1037/1082-989X.8.3.322>). This package implements computational
strategies including enumeration, Monte Carlo sampling, and optimization
algorithms (e.g., Genetic Algorithm, Differential Evolution, Sequential
Least Squares Programming) to obtain sharp lower and upper bounds of
Cronbach's alpha under arbitrary missing data patterns. The approach is
motivated by Manski's partial identification framework and pessimistic
bounding ideas from optimization literature.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RFlocalfdr
%global packver   0.8.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.5
Release:          1%{?dist}%{?buildtag}
Summary:          Significance Level for Random Forest Impurity Importance Scores

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-RFlocalfdr.data 
BuildRequires:    R-CRAN-vita 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-RFlocalfdr.data 
Requires:         R-CRAN-vita 

%description
Sets a significance level for Random Forest MDI (Mean Decrease in
Impurity, Gini or sum of squares) variable importance scores, using an
empirical Bayes approach. See Dunne et al. (2022)
<doi:10.1101/2022.04.06.487300>.

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

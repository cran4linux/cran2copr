%global __brp_check_rpaths %{nil}
%global packname  LDLcalc
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate and Predict the Low Density Lipoprotein Values

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-caretEnsemble 
BuildRequires:    R-CRAN-lares 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-resample 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-earth 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-Cubist 
BuildRequires:    R-CRAN-randomForest 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-caretEnsemble 
Requires:         R-CRAN-lares 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-resample 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-earth 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-Cubist 
Requires:         R-CRAN-randomForest 

%description
A wide variety of ways to calculate (through equations) or predict (using
9 Machine learning methods as well as a stack algorithm combination of
them all) the Low Density Lipoprotein values of patients based on the
values of three other metrics as Total Cholesterol , Triglyceride and High
Density Lipoprotein.

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

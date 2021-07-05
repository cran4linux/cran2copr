%global __brp_check_rpaths %{nil}
%global packname  tableone
%global packver   0.13.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.13.0
Release:          1%{?dist}%{?buildtag}
Summary:          Create 'Table 1' to Describe Baseline Characteristics with or without Propensity Score Weights

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-gmodels 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-labelled 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-gmodels 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-labelled 

%description
Creates 'Table 1', i.e., description of baseline patient characteristics,
which is essential in every medical research. Supports both continuous and
categorical variables, as well as p-values and standardized mean
differences. Weighted data are supported via the 'survey' package.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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

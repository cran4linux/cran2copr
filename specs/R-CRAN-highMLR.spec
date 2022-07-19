%global __brp_check_rpaths %{nil}
%global packname  highMLR
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Feature Selection for High Dimensional Survival Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mlr3 
BuildRequires:    R-CRAN-mlr3learners 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-coxme 
BuildRequires:    R-CRAN-missForest 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-mlr3 
Requires:         R-CRAN-mlr3learners 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-utils 
Requires:         R-CRAN-coxme 
Requires:         R-CRAN-missForest 
Requires:         R-CRAN-R6 

%description
Perform high dimensional Feature Selection in the presence of survival
outcome. Based on Feature Selection method and different survival
analysis, it will obtain the best markers with optimal threshold levels
according to their effect on disease progression and produce the most
consistent level according to those threshold values. The functions'
methodology is based on by Sonabend et al (2021)
<doi:10.1093/bioinformatics/btab039> and Bhattacharjee et al (2021)
<arXiv:2012.02102>.

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

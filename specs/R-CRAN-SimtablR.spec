%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SimtablR
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Easy Publication-Ready Tables and Regression Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-sandwich 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
Streamlines the creation of descriptive frequency tables ('Table 1'),
diagnostic test accuracy evaluations (sensitivity, specificity, predictive
values), and multi-outcome regression summaries. Features automatic
tables, prevalence and odds ratio calculations, and seamless integration
with 'flextable' for exporting results to 'Microsoft Word' and
'PowerPoint'.

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

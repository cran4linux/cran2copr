%global __brp_check_rpaths %{nil}
%global packname  comorbidity
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Computing Comorbidity Scores

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-utils 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-data.table 
Requires:         R-stats 
Requires:         R-CRAN-stringi 
Requires:         R-utils 

%description
Computing comorbidity indices and scores such as the weighted Charlson
score (Charlson, 1987 <doi:10.1016/0021-9681(87)90171-8>) and the
Elixhauser comorbidity score (Elixhauser, 1998
<doi:10.1097/00005650-199801000-00004>) using ICD-9-CM or ICD-10 codes
(Quan, 2005 <doi:10.1097/01.mlr.0000182534.19832.83>). Australian and
Swedish modifications of the Charlson Comorbidity Index are available as
well (Sundararajan, 2004 <doi:10.1016/j.jclinepi.2004.03.012> and
Ludvigsson, 2021 <doi:10.2147/CLEP.S282475>).

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

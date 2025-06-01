%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kidney.epi
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Kidney-Related Functions for Clinical and Epidemiological Research

License:          LGPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-purrr 

%description
Contains kidney care oriented functions. Current version contains
functions for calculation of: - Estimated glomerular filtration rate by
CKD-EPI (2021 and 2009), MDRD, CKiD, FAS, EKFC, etc. - Kidney Donor Risk
Index and Kidney Donor Profile Index for kidney transplant donors. -
Citation: Bikbov B. kidney.epi: Kidney-Related Functions for Clinical and
Epidemiological Research. Scientific-Tools.Org,
<https://Scientific-Tools.Org>.  <doi:10.32614/CRAN.package.kidney.epi>.

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

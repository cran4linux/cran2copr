%global __brp_check_rpaths %{nil}
%global packname  optBiomarker
%global packver   1.0-28
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.28
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of Optimal Number of Biomarkers for Two-Group Microarray Based Classifications at a Given Error Tolerance Level for Various Classification Rules

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-rpanel 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-ipred 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-rpanel 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-ipred 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-Matrix 

%description
Estimates optimal number of biomarkers for two-group classification based
on microarray data.

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

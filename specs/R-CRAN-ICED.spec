%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ICED
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          IntraClass Effect Decomposition

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-stringr 

%description
Estimate test-retest reliability for complex sampling strategies and
extract variances using IntraClass Effect Decomposition. Developed by
Brandmaier et al. (2018) "Assessing reliability in neuroimaging research
through intra-class effect decomposition (ICED)" <doi:10.7554/eLife.35718>
Also includes functions to simulate data based on sampling strategy.
Unofficial version release name: "Good work squirrels".

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

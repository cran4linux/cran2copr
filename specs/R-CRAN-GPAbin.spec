%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GPAbin
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Unifying Multiple Biplot Visualisations into a Single Display

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ca 
BuildRequires:    R-CRAN-jomo 
BuildRequires:    R-CRAN-mi 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-missMDA 
BuildRequires:    R-CRAN-mitools 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-ca 
Requires:         R-CRAN-jomo 
Requires:         R-CRAN-mi 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-missMDA 
Requires:         R-CRAN-mitools 
Requires:         R-CRAN-stringr 

%description
Aligning multiple visualisations by utilising generalised orthogonal
Procrustes analysis (GPA) before combining coordinates into a single
biplot display as described in Nienkemper-Swanepoel, le Roux and Lubbe
(2023)<doi:10.1080/03610918.2021.1914089>. This is mainly suitable to
combine visualisations constructed from multiple imputations, however, it
can be generalised to combine variations of visualisations from the same
datasets (i.e. resamples).

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

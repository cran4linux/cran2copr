%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  IIS
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Datasets to Accompany Wolfe and Schneider - Intuitive Introductory Statistics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-asbio 
BuildRequires:    R-CRAN-BSDA 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-NSM3 
BuildRequires:    R-CRAN-Rfit 
Requires:         R-CRAN-asbio 
Requires:         R-CRAN-BSDA 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-NSM3 
Requires:         R-CRAN-Rfit 

%description
These datasets and functions accompany Wolfe and Schneider (2017) -
Intuitive Introductory Statistics (ISBN: 978-3-319-56070-0)
<doi:10.1007/978-3-319-56072-4>. They are used in the examples throughout
the text and in the end-of-chapter exercises. The datasets are meant to
cover a broad range of topics in order to appeal to the diverse set of
interests and backgrounds typically present in an introductory Statistics
class.

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

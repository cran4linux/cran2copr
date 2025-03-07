%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TDLM
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Systematic Comparison of Trip Distribution Laws and Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-readr >= 2.0.0
BuildRequires:    R-CRAN-rmarkdown >= 2.0
BuildRequires:    R-CRAN-Rdpack >= 1.0.0
BuildRequires:    R-CRAN-sf >= 1.0.0
BuildRequires:    R-CRAN-Ecume 
BuildRequires:    R-CRAN-mathjaxr 
Requires:         R-CRAN-readr >= 2.0.0
Requires:         R-CRAN-rmarkdown >= 2.0
Requires:         R-CRAN-Rdpack >= 1.0.0
Requires:         R-CRAN-sf >= 1.0.0
Requires:         R-CRAN-Ecume 
Requires:         R-CRAN-mathjaxr 

%description
The main purpose of this package is to propose a rigorous framework to
fairly compare trip distribution laws and models as described in Lenormand
et al. (2016) <doi:10.1016/j.jtrangeo.2015.12.008>.

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

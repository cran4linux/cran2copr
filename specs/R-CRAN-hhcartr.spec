%global __brp_check_rpaths %{nil}
%global packname  hhcartr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          HHCART(G) - A Reflected Feature Space for CART

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-hash 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-DiagrammeR 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-DiagrammeRsvg 
BuildRequires:    R-CRAN-captioner 
BuildRequires:    R-CRAN-rsvg 
BuildRequires:    R-CRAN-bookdown 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-hash 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-DiagrammeR 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-DiagrammeRsvg 
Requires:         R-CRAN-captioner 
Requires:         R-CRAN-rsvg 
Requires:         R-CRAN-bookdown 

%description
An implementation of the HHCART-G algorithm as described in the paper -
Wickramarachchi C, Robertson B, Reale M, Price C, Brown J (2019). 'A
reflected feature space for CART.' Australian & New Zealand Journal of
Statistics, 61, 380–391. <doi:10.1111/anzs.12275>.

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

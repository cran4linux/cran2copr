%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SetMethods
%global packver   4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Functions for Set-Theoretic Multi-Method Research and Advanced QCA

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-QCA 
BuildRequires:    R-CRAN-admisc 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-stargazer 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-CRAN-fmsb 
BuildRequires:    R-CRAN-betareg 
Requires:         R-CRAN-QCA 
Requires:         R-CRAN-admisc 
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-stargazer 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-CRAN-fmsb 
Requires:         R-CRAN-betareg 

%description
Functions for performing set-theoretic multi-method research, QCA for
clustered data, theory evaluation, Enhanced Standard Analysis, indirect
calibration, radar visualisations. Additionally it includes data to
replicate the examples in the books by Oana, I.E, C. Q. Schneider, and E.
Thomann. Qualitative Comparative Analysis (QCA) using R: A Beginner's
Guide. Cambridge University Press and C. Q. Schneider and C. Wagemann "Set
Theoretic Methods for the Social Sciences", Cambridge University Press.

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

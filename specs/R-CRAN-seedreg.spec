%global packname  seedreg
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Regression Analysis for Seed Germination as a Function of Temperature

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-drc 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-hnp 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-multcompView 
Requires:         R-CRAN-drc 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-car 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-hnp 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-multcompView 

%description
Regression analysis using common models in seed temperature studies, such
as the Gaussian model (Martins, JF, Barroso, AAM, & Alves, PLCA (2017)
<doi:10.1590/s0100-83582017350100039>), quadratic (Nunes, AL, Sossmeier,
S, Gotz, AP, & Bispo, NB (2018) <doi:10.17265/2161-6264/2018.06.002>) and
others with potential for use, such as those implemented in the 'drc'
package (Ritz, C, Baty, F, Streibig, JC, & Gerhard, D (2015).
<doi:10.1371/journal.pone.0146021>), in the estimation of the ideal and
cardinal temperature for the occurrence of plant seed germination. The
functions return graphs with the equations automatically.

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

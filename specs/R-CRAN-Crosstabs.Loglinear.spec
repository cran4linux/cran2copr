%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Crosstabs.Loglinear
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Cross Tabulation and Loglinear Analyses of Categorical Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides 'SPSS'- and 'SAS'-like output for cross tabulations of two
categorical variables (CROSSTABS) and for hierarchical loglinear analyses
of two or more categorical variables (LOGLINEAR). The methods are
described in Agresti (2013, ISBN:978-0-470-46363-5), Ajzen & Walker (2021,
ISBN:9780429330308), Field (2018, ISBN:9781526440273), Norusis (2012,
ISBN:978-0-321-74843-0), Nussbaum (2015, ISBN:978-1-84872-603-1), Stevens
(2009, ISBN:978-0-8058-5903-4), Tabachnik & Fidell (2019,
ISBN:9780134790541), and von Eye & Mun (2013, ISBN:978-1-118-14640-8).

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

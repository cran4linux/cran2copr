%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BiMaUmisc
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          BiMaU Miscellaneous

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival >= 3.8.6
BuildRequires:    R-CRAN-exams 
BuildRequires:    R-CRAN-latex2exp 
BuildRequires:    R-CRAN-plotfunctions 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-survival >= 3.8.6
Requires:         R-CRAN-exams 
Requires:         R-CRAN-latex2exp 
Requires:         R-CRAN-plotfunctions 
Requires:         R-graphics 
Requires:         R-utils 

%description
Contains a function to plot publication-ready survival curves with the
Kaplan-Meier method (1958) <doi:10.2307/2281868> and a function to format
p-values, which are useful for repetitive analyses. BiMaU stands for the
Biostatistics and Mathematics Research Unit at the Sant Joan de Déu -
Pediatric Cancer Center Barcelona <https://github.com/BiMaU-PCCB>.

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

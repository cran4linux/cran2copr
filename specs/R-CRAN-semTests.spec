%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  semTests
%global packver   0.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Goodness-of-Fit Testing for Structural Equation Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan >= 0.6.16
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
Requires:         R-CRAN-lavaan >= 0.6.16
Requires:         R-CRAN-CompQuadForm 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 

%description
Supports eigenvalue block-averaging p-values (Foldnes, Grønneberg, 2018)
<doi:10.1080/10705511.2017.1373021>, penalized eigenvalue block-averaging
p-values (Foldnes, Moss, Grønneberg, 2024)
<doi:10.1080/10705511.2024.2372028>, penalized regression p-values
(Foldnes, Moss, Grønneberg, 2024) <doi:10.1080/10705511.2024.2372028>, as
well as traditional p-values such as Satorra-Bentler. All p-values can be
calculated using unbiased or biased gamma estimates (Du, Bentler, 2022)
<doi:10.1080/10705511.2022.2063870> and two choices of chi square
statistics.

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

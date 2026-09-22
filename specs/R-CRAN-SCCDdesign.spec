%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SCCDdesign
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Construction of Screening Designs for Mixed Level Continuous and Categorical Factors

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-AlgDesign 
BuildRequires:    R-CRAN-leaps 
BuildRequires:    R-stats 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-AlgDesign 
Requires:         R-CRAN-leaps 
Requires:         R-stats 

%description
Constructs screening designs for experiments involving continuous and
categorical factors with multiple levels. The package implements methods
for constructing mixed-level screening designs, involving factors with
more than two levels. It also evaluates the statistical performance of
screening designs throughdev power to identify active effects and Type I
error rates. The package implements three methods proposed by Jones, B.,
Lekivetz, R., Majumdar, D. and Nachtsheim, C. (2025)
<doi:10.1080/00401706.2024.2362149> for generating efficient screening
designs involving three-level continuous and two-level categorical factors
for even run sizes. It also includes Paley Type I and Type II
constructions for conference matrices and pseudo conference matrices
obtained using the coordinate exchange algorithm by Jones, B. and
Nachtsheim, C. J. (2011) <doi:10.1080/00224065.2011.11917841> which are
used in the development of these screening designs.

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

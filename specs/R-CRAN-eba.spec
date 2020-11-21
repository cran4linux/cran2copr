%global packname  eba
%global packver   1.10-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.10.0
Release:          1%{?dist}%{?buildtag}
Summary:          Elimination-by-Aspects Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-psychotools 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-psychotools 

%description
Fitting and testing multi-attribute probabilistic choice models,
especially the Bradley-Terry-Luce (BTL) model (Bradley & Terry, 1952
<doi:10.1093/biomet/39.3-4.324>; Luce, 1959), elimination-by-aspects (EBA)
models (Tversky, 1972 <doi:10.1037/h0032955>), and preference tree
(Pretree) models (Tversky & Sattath, 1979
<doi:10.1037/0033-295X.86.6.542>).

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

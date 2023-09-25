%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  checkdown
%global packver   0.0.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.10
Release:          1%{?dist}%{?buildtag}
Summary:          Check-Fields and Check-Boxes for 'rmarkdown'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-glue 

%description
Creates auto-grading check-fields and check-boxes for 'rmarkdown' or
'quarto' HTML. It can be used in class, when teacher share materials and
tasks, so students can solve some problems and check their work. In
contrast to the 'learnr' package, the 'checkdown' package works
serverlessly without 'shiny'.

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

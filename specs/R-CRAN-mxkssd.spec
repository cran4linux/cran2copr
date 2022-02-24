%global __brp_check_rpaths %{nil}
%global packname  mxkssd
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient Mixed-Level k-Circulant Supersaturated Designs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0
BuildArch:        noarch

%description
Generates efficient balanced mixed-level k-circulant supersaturated
designs by interchanging the elements of the generator vector. Attempts to
generate a supersaturated design that has EfNOD efficiency more than user
specified efficiency level (mef). Displays the progress of generation of
an efficient mixed-level k-circulant design through a progress bar. The
progress of 100 per cent means that one full round of interchange is
completed. More than one full round (typically 4-5 rounds) of interchange
may be required for larger designs. For more details, please see Mandal,
B.N., Gupta V. K. and Parsad, R. (2011). Construction of Efficient
Mixed-Level k-Circulant Supersaturated Designs, Journal of Statistical
Theory and Practice, 5:4, 627-648, <doi:10.1080/15598608.2011.10483735>.

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

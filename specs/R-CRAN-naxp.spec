%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  naxp
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Encoded ASCII Expressions

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-cpp11 

%description
Converts alphanumeric codes such as postcodes to whole numbers and back
again, following the 'naxp' standard <https://naxp.org/spec/>. A naxp
('encoded ASCII expression') is a pattern, defined using a similar syntax
to regular expressions, that maps each text it accepts to a number from 1
to a fixed maximum, and any other text to 0. The same pattern maps text to
numbers identically across all 'naxp' libraries in all languages on all
platforms (subject only to the availability of types able to store large
enough integers). Standard naxps are defined for common code systems and
are built into all 'naxp' libraries. Two naxps can be compared to
determine, among other things, whether stored values keep their meaning
when one replaces the other. Wraps the 'naxp' 'C++' library
<https://naxp.org/api/#cpp>.

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

%global packname  SwimmeR
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Data Import, Cleaning, and Conversions for Swimming Results

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-pdftools 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-readr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-pdftools 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-readr 

%description
The goal for of the 'SwimmeR' package is to provide means of acquiring,
and then analyzing, data from swimming (and diving) competitions.  To that
end 'SwimmeR' allows results to be read in from .html sources, like
'Hy-Tek' real time results pages, '.pdf' files, 'ISL' results, and (on a
development basis) '.hy3' files.  Once read in, 'SwimmeR' can convert
swimming times (performances) between the computationally useful format of
seconds reported to the '100ths' place (e.g. 95.37), and the conventional
reporting format (1:35.37) used in the swimming community.  'SwimmeR' can
also score meets in a variety of formats with user defined point values,
convert times between courses ('LCM', 'SCM', 'SCY') and draw single
elimination brackets, as well as providing a suite of tools for working
cleaning swimming data.  This is a developmental package, not yet mature.

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

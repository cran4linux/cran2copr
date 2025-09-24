%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rtables.officer
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Exporting Tools for 'rtables'

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 2.1.0
BuildRequires:    R-CRAN-stringi >= 1.6
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-flextable >= 0.9.10
BuildRequires:    R-CRAN-officer >= 0.7.0
BuildRequires:    R-CRAN-rtables >= 0.6.12
BuildRequires:    R-CRAN-formatters >= 0.5.11
BuildRequires:    R-CRAN-rlistings >= 0.2.11
BuildRequires:    R-CRAN-lifecycle >= 0.2.0
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-checkmate >= 2.1.0
Requires:         R-CRAN-stringi >= 1.6
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-flextable >= 0.9.10
Requires:         R-CRAN-officer >= 0.7.0
Requires:         R-CRAN-rtables >= 0.6.12
Requires:         R-CRAN-formatters >= 0.5.11
Requires:         R-CRAN-rlistings >= 0.2.11
Requires:         R-CRAN-lifecycle >= 0.2.0
Requires:         R-methods 
Requires:         R-stats 

%description
Designed to create and display complex tables with R, the 'rtables' R
package allows cells in an 'rtables' object to contain any
high-dimensional data structure, which can then be displayed with
cell-specific formatting instructions. Additionally, the 'rtables.officer'
package supports export formats related to the Microsoft Office software
suite, including Microsoft Word ('docx') and Microsoft PowerPoint
('pptx').

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

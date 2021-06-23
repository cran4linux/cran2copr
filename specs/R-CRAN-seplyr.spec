%global __brp_check_rpaths %{nil}
%global packname  seplyr
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Improved Standard Evaluation Interfaces for Common Data Manipulation Tasks

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-wrapr >= 2.0.7
BuildRequires:    R-CRAN-dplyr >= 0.8.5
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-wrapr >= 2.0.7
Requires:         R-CRAN-dplyr >= 0.8.5
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 

%description
The 'seplyr' (standard evaluation plying) package supplies improved
standard evaluation adapter methods for important common 'dplyr' data
manipulation tasks. In addition the 'seplyr' package supplies several new
"key operations bound together" methods.  These include
'group_summarize()' (which combines grouping, arranging and calculation in
an atomic unit), 'add_group_summaries()' (which joins grouped summaries
into a 'data.frame' in a well documented manner), 'add_group_indices()'
(which adds per-group identifiers to a 'data.frame' without depending on
row-order), 'partition_mutate_qt()' (which optimizes mutate sequences),
and 'if_else_device()' (which simulates per-row if-else blocks in
expression sequences).

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

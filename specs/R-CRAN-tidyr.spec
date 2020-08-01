%global packname  tidyr
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Tidy Messy Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-tibble >= 2.1.1
BuildRequires:    R-CRAN-tidyselect >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 0.8.2
BuildRequires:    R-CRAN-vctrs >= 0.3.0
BuildRequires:    R-CRAN-ellipsis >= 0.1.0
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-cpp11 
Requires:         R-CRAN-tibble >= 2.1.1
Requires:         R-CRAN-tidyselect >= 1.1.0
Requires:         R-CRAN-dplyr >= 0.8.2
Requires:         R-CRAN-vctrs >= 0.3.0
Requires:         R-CRAN-ellipsis >= 0.1.0
Requires:         R-CRAN-glue 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-utils 
Requires:         R-CRAN-lifecycle 

%description
Tools to help to create tidy data, where each column is a variable, each
row is an observation, and each cell contains a single value. 'tidyr'
contains tools for changing the shape (pivoting) and hierarchy (nesting
and 'unnesting') of a dataset, turning deeply nested lists into
rectangular data frames ('rectangling'), and extracting values out of
string columns. It also includes tools for working with missing values
(both implicit and explicit).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}

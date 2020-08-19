%global packname  dplyr
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Grammar of Data Manipulation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-glue >= 1.3.2
BuildRequires:    R-CRAN-tidyselect >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 0.4.7
BuildRequires:    R-CRAN-vctrs >= 0.3.2
BuildRequires:    R-CRAN-lifecycle >= 0.2.0
BuildRequires:    R-CRAN-ellipsis 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-utils 
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-glue >= 1.3.2
Requires:         R-CRAN-tidyselect >= 1.1.0
Requires:         R-CRAN-rlang >= 0.4.7
Requires:         R-CRAN-vctrs >= 0.3.2
Requires:         R-CRAN-lifecycle >= 0.2.0
Requires:         R-CRAN-ellipsis 
Requires:         R-CRAN-generics 
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-utils 

%description
A fast, consistent tool for working with data frame like objects, both in
memory and out of memory.

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

%global __brp_check_rpaths %{nil}
%global packname  markmyassignment
%global packver   0.8.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.3
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Marking of R Assignments

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-testthat >= 2.0.0
BuildRequires:    R-CRAN-httr >= 1.0.0
BuildRequires:    R-CRAN-checkmate >= 1.0.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-codetools 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-testthat >= 2.0.0
Requires:         R-CRAN-httr >= 1.0.0
Requires:         R-CRAN-checkmate >= 1.0.0
Requires:         R-methods 
Requires:         R-CRAN-yaml 
Requires:         R-codetools 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-rlang 

%description
Automatic marking of R assignments for students and teachers based on
'testthat' test suites.

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

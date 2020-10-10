%global packname  exams.mylearn
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Question Generation in the 'MyLearn' XML Format

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-exams >= 2.3.4
BuildRequires:    R-CRAN-stringi >= 1.4.6
BuildRequires:    R-CRAN-glue >= 1.4.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-xml2 >= 1.2.5
Requires:         R-CRAN-exams >= 2.3.4
Requires:         R-CRAN-stringi >= 1.4.6
Requires:         R-CRAN-glue >= 1.4.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-xml2 >= 1.2.5

%description
Randomized multiple-select and single-select question generation for the
'MyLearn' teaching and learning platform. Question templates in the form
of the R/exams package (see <http://www.r-exams.org/>) are transformed
into XML format required by 'MyLearn'.

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

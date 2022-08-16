%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mdsr
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Complement to 'Modern Data Science with R'

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-babynames 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-dbplyr 
BuildRequires:    R-CRAN-downloader 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-RMariaDB 
BuildRequires:    R-CRAN-skimr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-webshot 
Requires:         R-CRAN-babynames 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-dbplyr 
Requires:         R-CRAN-downloader 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-RMariaDB 
Requires:         R-CRAN-skimr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-webshot 

%description
A complement to *Modern Data Science with R*, both the first and second
editions (ISBN: 978-0367191498, publisher URL:
<https://www.routledge.com/Modern-Data-Science-with-R/Baumer-Kaplan-Horton/p/book/9780367191498>).
This package contains data and code to complete exercises and reproduce
examples from the text. It also facilitates connections to the SQL
database server used in the book. Both editions of the book are supported
by this package.

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

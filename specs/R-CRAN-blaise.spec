%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  blaise
%global packver   1.3.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.10
Release:          1%{?dist}%{?buildtag}
Summary:          Read and Write FWF Files in the 'Blaise' Format

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils >= 3.4.1
BuildRequires:    R-tools >= 3.4.1
BuildRequires:    R-methods >= 3.4.1
BuildRequires:    R-stats >= 3.4.1
BuildRequires:    R-CRAN-tibble >= 1.3.3
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-CRAN-readr >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 0.7.2
Requires:         R-utils >= 3.4.1
Requires:         R-tools >= 3.4.1
Requires:         R-methods >= 3.4.1
Requires:         R-stats >= 3.4.1
Requires:         R-CRAN-tibble >= 1.3.3
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-CRAN-readr >= 1.1.1
Requires:         R-CRAN-dplyr >= 0.7.2

%description
Can be used to read and write a fwf with an accompanying 'Blaise'
datamodel. Blaise is the software suite built by Statistics Netherlands
(CBS). It is essentially a way to write and collect surveys and perform
statistical analysis on the data. It stores its data in fixed width format
with an accompanying metadata file, this is the Blaise format. The package
automatically interprets this metadata and reads the file into an R
dataframe. When supplying a datamodel for writing, the dataframe will be
automatically converted to that format and checked for compatibility.
Supports dataframes, tibbles and LaF objects. For more information about
'Blaise', see <https://blaise.com/products/general-information>.

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

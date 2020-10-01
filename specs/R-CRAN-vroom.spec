%global packname  vroom
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Read and Write Rectangular Text Data Quickly

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-tibble >= 2.0.0
BuildRequires:    R-CRAN-progress >= 1.2.1
BuildRequires:    R-CRAN-rlang >= 0.4.2
BuildRequires:    R-CRAN-cpp11 >= 0.2.0
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-hms 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-tibble >= 2.0.0
Requires:         R-CRAN-rlang >= 0.4.2
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-hms 
Requires:         R-CRAN-lifecycle 
Requires:         R-stats 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-withr 

%description
The goal of 'vroom' is to read and write data (like 'csv', 'tsv' and
'fwf') quickly. When reading it uses a quick initial indexing step, then
reads the values lazily , so only the data you actually use needs to be
read.  The writer formats the data in parallel and writes to disk
asynchronously from formatting.

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

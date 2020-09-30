%global packname  prt
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Tabular Data Backed by Partitioned 'fst' Files

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-fst 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-pillar 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-fansi 
BuildRequires:    R-CRAN-backports 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-fst 
Requires:         R-CRAN-data.table 
Requires:         R-utils 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-pillar 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-fansi 
Requires:         R-CRAN-backports 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-knitr 

%description
Intended for larger-than-memory tabular data, 'prt' objects provide an
interface to read row and/or column subsets into memory as data.table
objects. Data queries, constructed as 'R' expressions, are evaluated using
the non-standard evaluation framework provided by 'rlang' and file-backing
is powered by the fast and efficient 'fst' package.

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

%global __brp_check_rpaths %{nil}
%global packname  fplyr
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          2%{?dist}%{?buildtag}
Summary:          Apply Functions to Blocks of Files

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-parallel >= 3.5.1
BuildRequires:    R-CRAN-data.table >= 1.1.4
BuildRequires:    R-CRAN-iotools >= 0.2.5
Requires:         R-parallel >= 3.5.1
Requires:         R-CRAN-data.table >= 1.1.4
Requires:         R-CRAN-iotools >= 0.2.5

%description
Read and process a large delimited file block by block. A block consists
of all the contiguous rows that have the same value in the first field.
The result can be returned as a list or a data.table, or even directly
printed to an output file.

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

%files
%{rlibdir}/%{packname}

%global packname  finch
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}
Summary:          Parse Darwin Core Files

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-EML >= 2.0.0
BuildRequires:    R-CRAN-data.table >= 1.10.0
BuildRequires:    R-CRAN-xml2 >= 1.0.0
BuildRequires:    R-CRAN-hoardr >= 0.2.0
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-EML >= 2.0.0
Requires:         R-CRAN-data.table >= 1.10.0
Requires:         R-CRAN-xml2 >= 1.0.0
Requires:         R-CRAN-hoardr >= 0.2.0
Requires:         R-CRAN-digest 

%description
Parse and create Darwin Core (<http://rs.tdwg.org/dwc/>) Simple and
Archives. Functionality includes reading and parsing all the files in a
Darwin Core Archive, including the datasets and metadata; read and parse
simple Darwin Core files; and validation of Darwin Core Archives.

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

%global packname  us.census.geoheader
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          2%{?dist}%{?buildtag}
Summary:          US 2010 Census SF2 Geographic Header Summary Levels 010-050

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-tibble 

%description
A simple interface to the Geographic Header information from the "2010 US
Census Summary File 2".  The entire Summary File 2 is described at
<https://catalog.data.gov/dataset/census-2000-summary-file-2-sf2>, but
note that this package only provides access to parts of the geographic
header ('geoheader') of the file.  In particular, only the first 101
columns of the geoheader are included and, more importantly, only rows
with summary levels (SUMLEVs) 010 through 050 (nation down through county
level) are included.  In addition to access to (part of) the geoheader,
the package also provides a decode function that takes a column name and
value and, for certain columns, returns "the meaning" of that column
(i.e., a "SUMLEV" value of 40 means "State"); without a value, the decode
function attempts to describe the column itself.

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

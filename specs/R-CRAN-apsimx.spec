%global packname  apsimx
%global packver   1.946
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.946
Release:          1%{?dist}
Summary:          Inspect, Read, Edit and Run 'APSIM' "Next Generation" and'APSIM' Classic

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-RSQLite 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-xml2 

%description
The functions in this package inspect, read, edit and run files for
'APSIM' "Next Generation" ('JSON') and 'APSIM' "Classic" ('XML'). The
files with an 'apsim' extension correspond to 'APSIM' Classic (7.x) -
Windows only - and the ones with an 'apsimx' extension correspond to
'APSIM' "Next Generation". For more information about 'APSIM' see
(<https://www.apsim.info/>) and for 'APSIM' next generation
(<https://apsimnextgeneration.netlify.com/>).

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

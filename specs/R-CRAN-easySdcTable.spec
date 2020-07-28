%global packname  easySdcTable
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}
Summary:          Easy Interface to the Statistical Disclosure Control Package'sdcTable'

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-SSBtools 
BuildRequires:    R-CRAN-sdcTable 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-methods 
Requires:         R-CRAN-SSBtools 
Requires:         R-CRAN-sdcTable 
Requires:         R-CRAN-shiny 
Requires:         R-methods 

%description
The main function, ProtectTable(), performs table suppression according to
a frequency rule with a data set as the only required input. Within this
function, protectTable(), protectLinkedTables() or runArgusBatchFile() in
package 'sdcTable' is called. Lists of level-hierarchy (parameter
'dimList') and other required input to these functions are created
automatically. The function, PTgui(), starts a graphical user interface
based on the shiny package.

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

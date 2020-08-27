%global packname  R.utils
%global packver   2.10.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.10.1
Release:          1%{?dist}%{?buildtag}
Summary:          Various Programming Utilities

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R.methodsS3 >= 1.8.0
BuildRequires:    R-CRAN-R.oo >= 1.23.0
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
Requires:         R-CRAN-R.methodsS3 >= 1.8.0
Requires:         R-CRAN-R.oo >= 1.23.0
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-tools 

%description
Utility functions useful when programming and developing R packages.

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

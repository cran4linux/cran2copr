%global __brp_check_rpaths %{nil}
%global packname  XiMpLe
%global packver   0.10-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.3
Release:          1%{?dist}%{?buildtag}
Summary:          A Simple XML Tree Parser and Generator

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.9.0
Requires:         R-core >= 2.9.0
BuildArch:        noarch
BuildRequires:    R-methods 
Requires:         R-methods 

%description
Provides a simple XML tree parser/generator. It includes functions to read
XML files into R objects, get information out of and into nodes, and write
R objects back to XML code. It's not as powerful as the 'XML' package and
doesn't aim to be, but for simple XML handling it could be useful. It was
originally developed for the R GUI and IDE 'RKWard'
<https://rkward.kde.org>, to make plugin development easier.

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

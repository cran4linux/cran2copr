%global packname  DescToolsAddIns
%global packver   1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Functions to be Used as Shortcuts in 'RStudio'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DescTools >= 0.99.30
BuildRequires:    R-CRAN-rstudioapi >= 0.1
BuildRequires:    R-base 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-manipulate 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-foreign 
Requires:         R-CRAN-DescTools >= 0.99.30
Requires:         R-CRAN-rstudioapi >= 0.1
Requires:         R-base 
Requires:         R-stats 
Requires:         R-CRAN-manipulate 
Requires:         R-CRAN-writexl 
Requires:         R-foreign 

%description
'RStudio' as of recently offers the option to define addins and assign
shortcuts to them. This package contains addins for a few most frequently
used functions in a data scientist's (at least mine) daily work (like
str(), example(), plot(), head(), view(), Desc()). Most of these functions
will use the current selection in the editor window and send the specific
command to the console while instantly executing it. Assigning shortcuts
to these addins will save you quite a few keystrokes.

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

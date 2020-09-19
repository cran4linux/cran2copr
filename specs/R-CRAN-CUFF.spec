%global packname  CUFF
%global packver   1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Charles's Utility Function using Formula

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-xlsx 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-nlme 
Requires:         R-CRAN-xlsx 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-lmerTest 
Requires:         R-nlme 

%description
Utility functions that provides wrapper to descriptive base functions like
cor, mean and table.  It makes use of the formula interface to pass
variables to functions.  It also provides operators to concatenate (%+%),
to repeat (%n%) and manage character vectors for nice display.

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

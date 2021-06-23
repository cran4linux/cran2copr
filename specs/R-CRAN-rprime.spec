%global __brp_check_rpaths %{nil}
%global packname  rprime
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Functions for Working with 'Eprime' Text Files

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr >= 1.0.0
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-stringr >= 1.0.0
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-stringi 
Requires:         R-tools 
Requires:         R-utils 

%description
'Eprime' is a set of programs for administering psychological experiments
by computer. This package provides functions for loading, parsing,
filtering and exporting data in the text files produced by 'Eprime'
experiments.

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

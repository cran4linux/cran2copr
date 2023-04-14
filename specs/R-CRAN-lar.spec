%global __brp_check_rpaths %{nil}
%global packname  lar
%global packver   0.1-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          History of labour relations package

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-treemap 
BuildRequires:    R-CRAN-xlsx 
Requires:         R-CRAN-data.table 
Requires:         R-grid 
Requires:         R-CRAN-treemap 
Requires:         R-CRAN-xlsx 

%description
This package is intended for researchers studying historical labour
relations (see http://www.historyoflabourrelations.org). The package
allows for easy access of excel files in the standard defined by the
Global Collaboratory on the History of Labour Relations. The package also
allows for visualisation of labour relations according to the
Collaboratory's format.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}

%global __brp_check_rpaths %{nil}
%global packname  ConfigParser
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Package to Parse an INI File, Including Variable Interpolation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ini 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-ini 
Requires:         R-CRAN-R6 

%description
Enhances the 'ini' package by adding the ability to interpolate variables.
The INI configuration file is read into an R6 ConfigParser object (loosely
inspired by Pythons ConfigParser module) and the keys can be read, where
'%(....)s' instances are interpolated by other included options or outside
variables.

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

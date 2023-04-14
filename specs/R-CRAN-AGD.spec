%global __brp_check_rpaths %{nil}
%global packname  AGD
%global packver   0.39
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.39
Release:          3%{?dist}%{?buildtag}
Summary:          Analysis of Growth Data

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gamlss 
BuildRequires:    R-CRAN-gamlss.dist 
Requires:         R-CRAN-gamlss 
Requires:         R-CRAN-gamlss.dist 

%description
Tools for the analysis of growth data: to extract an LMS table from a
gamlss object, to calculate the standard deviation scores and its inverse,
and to superpose two wormplots from different models. The package contains
a some varieties of reference tables, especially for The Netherlands.

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

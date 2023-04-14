%global __brp_check_rpaths %{nil}
%global packname  mldr
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          3%{?dist}%{?buildtag}
Summary:          Exploratory Data Analysis and Manipulation of Multi-Label DataSets

License:          LGPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 0.11
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-circlize 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-shiny >= 0.11
Requires:         R-CRAN-XML 
Requires:         R-CRAN-circlize 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-methods 

%description
Exploratory data analysis and manipulation functions for multi- label data
sets along with an interactive Shiny application to ease their use.

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

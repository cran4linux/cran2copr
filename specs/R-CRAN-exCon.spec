%global __brp_check_rpaths %{nil}
%global packname  exCon
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          3%{?dist}%{?buildtag}
Summary:          Interactive Exploration of Contour Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-CRAN-jsonlite 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Interactive tools to explore topographic-like data sets.  Such data sets
take the form of a matrix in which the rows and columns provide
location/frequency information, and the matrix elements contain
altitude/response information.  Such data is found in cartography, 2D
spectroscopy and chemometrics.  The functions in this package create
interactive web pages showing the contoured data, possibly with slices
from the original matrix parallel to each dimension. The interactive
behavior is created using the 'D3.js' 'JavaScript' library by Mike
Bostock.

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

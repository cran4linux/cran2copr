%global __brp_check_rpaths %{nil}
%global packname  colorscience
%global packver   1.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          3%{?dist}%{?buildtag}
Summary:          Color Science Methods and Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-sp 

%description
Methods and data for color science - color conversions by observer,
illuminant, and gamma. Color matching functions and chromaticity diagrams.
Color indices, color differences, and spectral data conversion/analysis.

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

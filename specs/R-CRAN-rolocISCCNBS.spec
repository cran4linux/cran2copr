%global __brp_check_rpaths %{nil}
%global packname  rolocISCCNBS
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}%{?buildtag}
Summary:          A Colour List and Colour Metric Based on the ISCC-NBS System ofColor Designation

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-roloc 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-colorspace 
Requires:         R-CRAN-roloc 
Requires:         R-methods 
Requires:         R-CRAN-colorspace 

%description
A colour list and colour metric based on the ISCC-NBS System of Color
Designation for use with the 'roloc' package for converting colour
specifications to colour names.

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

%global packname  munsellinterpol
%global packver   2.5-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.1
Release:          1%{?dist}
Summary:          Interpolate Munsell Renotation Data from Hue/Chroma to CIE/RGB

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-spacesRGB 
BuildRequires:    R-CRAN-spacesXYZ 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-spacesRGB 
Requires:         R-CRAN-spacesXYZ 

%description
Methods for interpolating data in the Munsell color system following the
ASTM D-1535 standard. Hues and chromas with decimal values can be
interpolated and converted to/from the Munsell color system and CIE xyY,
CIE XYZ, CIE Lab, CIE Luv, or RGB.  Includes ISCC-NBS color block lookup.
Based on the work by Paul Centore, "The Munsell and Kubelka-Munk Toolbox".

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX

%global packname  swatches
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}
Summary:          Read, Inspect, and Manipulate Color Swatch Files

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-pack 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-pack 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-xml2 
Requires:         R-tools 
Requires:         R-CRAN-colorspace 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 

%description
There are numerous places to create and download color palettes. These are
usually shared in 'Adobe' swatch file formats of some kind. There is also
often the need to use standard palettes developed within an organization
to ensure that aesthetics are carried over into all projects and output.
Now there is a way to read these swatch files in R and avoid transcribing
or converting color values by hand or or with other programs. This package
provides functions to read and inspect 'Adobe Color' ('ACO'), 'Adobe
Swatch Exchange' ('ASE'), 'GIMP Palette' ('GPL'), 'OpenOffice' palette
('SOC') files and 'KDE Palette' ('colors') files. Detailed descriptions of
'Adobe Color' and 'Swatch Exchange' file formats as well as other swatch
file formats can be found at
<http://www.selapa.net/swatches/colors/fileformats.php>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/palettes
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

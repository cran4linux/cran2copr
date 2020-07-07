%global packname  exifr
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          4%{?dist}
Summary:          EXIF Image Data in R

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    perl(Image::ExifTool)
Requires:         perl(Image::ExifTool)
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rappdirs 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-jsonlite 
Requires:         R-utils 
Requires:         R-CRAN-rappdirs 

%description
Reads EXIF data using ExifTool
<http://www.sno.phy.queensu.ca/~phil/exiftool/> and returns results as a
data frame. ExifTool is a platform-independent Perl library plus a
command-line application for reading, writing and editing meta information
in a wide variety of files. ExifTool supports many different metadata
formats including EXIF, GPS, IPTC, XMP, JFIF, GeoTIFF, ICC Profile,
Photoshop IRB, FlashPix, AFCP and ID3, as well as the maker notes of many
digital cameras by Canon, Casio, FLIR, FujiFilm, GE, HP, JVC/Victor,
Kodak, Leaf, Minolta/Konica-Minolta, Motorola, Nikon, Nintendo,
Olympus/Epson, Panasonic/Leica, Pentax/Asahi, Phase One, Reconyx, Ricoh,
Samsung, Sanyo, Sigma/Foveon and Sony.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/images
%{rlibdir}/%{packname}/INDEX

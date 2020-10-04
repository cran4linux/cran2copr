%global packname  imgpalr
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Create Color Palettes from Images

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-downloader 
BuildRequires:    R-CRAN-farver 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-jpeg 
Requires:         R-CRAN-downloader 
Requires:         R-CRAN-farver 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-jpeg 

%description
Provides ability to create color palettes from image files. It offers
control over the type of color palette to derive from an image
(qualitative, sequential or divergent) and other palette properties.
Quantiles of an image color distribution can be trimmed. Near-black or
near-white colors can be trimmed in RGB color space independent of
trimming brightness or saturation distributions in HSV color space.
Creating sequential palettes also offers control over the order of HSV
color dimensions to sort by. This package differs from other related
packages like 'RImagePalette' in approaches to quantizing and extracting
colors in images to assemble color palettes and the level of user control
over palettes construction.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/blue-yellow.bmp
%doc %{rlibdir}/%{packname}/blue-yellow.gif
%doc %{rlibdir}/%{packname}/blue-yellow.jpg
%doc %{rlibdir}/%{packname}/blue-yellow.png
%doc %{rlibdir}/%{packname}/colors.jpg
%doc %{rlibdir}/%{packname}/purples.jpg
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX

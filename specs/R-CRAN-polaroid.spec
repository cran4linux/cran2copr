%global packname  polaroid
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          3%{?dist}
Summary:          Create Hex Stickers with 'shiny'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-argonDash 
BuildRequires:    R-CRAN-argonR 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-hexSticker 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyWidgets 
Requires:         R-CRAN-argonDash 
Requires:         R-CRAN-argonR 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-hexSticker 
Requires:         R-CRAN-png 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyWidgets 

%description
Create hexagonal shape sticker image. 'polaroid' can be used in user's web
browser. 'polaroid' can be used in 'shinyapps.io'. In both way, user can
download created 'hexSticker' as 'PNG' image. 'polaroid' is built based on
'argonDash', 'colourpicker' and 'hexSticker' R package.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/polaroid
%doc %{rlibdir}/%{packname}/polaroid.png
%{rlibdir}/%{packname}/INDEX

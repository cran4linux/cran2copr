%global packname  showtext
%global packver   0.8-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.1
Release:          2%{?dist}
Summary:          Using Fonts More Easily in R Graphs

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    zlib-devel
BuildRequires:    libpng-devel
BuildRequires:    freetype-devel
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-showtextdb >= 2.0
BuildRequires:    R-CRAN-sysfonts >= 0.7.1
BuildRequires:    R-grDevices 
Requires:         R-CRAN-showtextdb >= 2.0
Requires:         R-CRAN-sysfonts >= 0.7.1
Requires:         R-grDevices 

%description
Making it easy to use various types of fonts ('TrueType', 'OpenType', Type
1, web fonts, etc.) in R graphs, and supporting most output formats of R
graphics including PNG, PDF and SVG. Text glyphs will be converted into
polygons or raster images, hence after the plot has been created, it no
longer relies on the font files. No external software such as
'Ghostscript' is needed to use this package.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/AUTHORS
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

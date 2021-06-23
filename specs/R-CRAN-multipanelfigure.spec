%global __brp_check_rpaths %{nil}
%global packname  multipanelfigure
%global packver   2.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Infrastructure to Assemble Multi-Panel Figures (from Grobs)

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-magick >= 1.9
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringi >= 1.2.3
BuildRequires:    R-CRAN-gridGraphics >= 0.3.0
BuildRequires:    R-CRAN-gtable >= 0.2.0
BuildRequires:    R-CRAN-assertive.base >= 0.0.7
BuildRequires:    R-CRAN-assertive.properties >= 0.0.4
BuildRequires:    R-CRAN-assertive.types >= 0.0.3
BuildRequires:    R-CRAN-assertive.files >= 0.0.2
BuildRequires:    R-CRAN-assertive.numbers >= 0.0.2
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-magick >= 1.9
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringi >= 1.2.3
Requires:         R-CRAN-gridGraphics >= 0.3.0
Requires:         R-CRAN-gtable >= 0.2.0
Requires:         R-CRAN-assertive.base >= 0.0.7
Requires:         R-CRAN-assertive.properties >= 0.0.4
Requires:         R-CRAN-assertive.types >= 0.0.3
Requires:         R-CRAN-assertive.files >= 0.0.2
Requires:         R-CRAN-assertive.numbers >= 0.0.2
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-utils 

%description
Tools to create a layout for figures made of multiple panels, and to fill
the panels with base, 'lattice', 'ggplot2' and 'ComplexHeatmap' plots,
grobs, as well as content from all image formats supported by
'ImageMagick' (accessed through 'magick').

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX

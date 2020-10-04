%global packname  colorBlindness
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          3%{?dist}%{?buildtag}
Summary:          Safe Color Set for Color Blindness

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-gridGraphics 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-grid 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-colorspace 
Requires:         R-graphics 
Requires:         R-CRAN-gridGraphics 
Requires:         R-CRAN-gtable 
Requires:         R-grid 

%description
Provide the safe color set for color blindness, the simulator of
protanopia, deuteranopia. The color sets are collected from: Wong, B.
(2011) <doi:10.1038/nmeth.1618>, <http://mkweb.bcgsc.ca/biovis2012/>, and
<http://geog.uoregon.edu/datagraphics/color_scales.htm>. The simulations
of the appearance of the colors to color-deficient viewers were based on
algorithms in Vienot, F., Brettel, H. and Mollon, J.D. (1999)
<doi:10.1002/(SICI)1520-6378(199908)24:4%3C243::AID-COL5%3E3.0.CO;2-3>.
The cvdPlot() function to generate 'ggplot' grobs of simulations were
modified from <https://github.com/clauswilke/colorblindr>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX

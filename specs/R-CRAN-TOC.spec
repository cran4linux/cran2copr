%global packname  TOC
%global packver   0.0-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}
Summary:          Total Operating Characteristic Curve and ROC Curve

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-bit 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-bit 
Requires:         R-CRAN-rgdal 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Construction of the Total Operating Characteristic (TOC) Curve and the
Receiver (aka Relative) Operating Characteristic (ROC) Curve for spatial
and non-spatial data. The TOC method is a modification of the ROC method
which measures the ability of an index variable to diagnose either
presence or absence of a characteristic. The diagnosis depends on whether
the value of an index variable is above a threshold. Each threshold
generates a two-by-two contingency table, which contains four entries:
hits (H), misses (M), false alarms (FA), and correct rejections (CR).
While ROC shows for each threshold only two ratios, H/(H + M) and FA/(FA +
CR), TOC reveals the size of every entry in the contingency table for each
threshold (Pontius Jr., R.G., Si, K. 2014.
<doi:10.1080/13658816.2013.862623>).

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
%doc %{rlibdir}/%{packname}/external
%{rlibdir}/%{packname}/INDEX

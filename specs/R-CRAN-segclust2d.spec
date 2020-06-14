%global packname  segclust2d
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          2%{?dist}
Summary:          Bivariate Segmentation/Clustering Methods and Tools

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-reshape2 >= 1.4.1
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ggplot2 >= 2.1.0
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-reshape2 >= 1.4.1
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-zoo 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-scales 

%description
Provides two methods for segmentation and joint segmentation/clustering of
bivariate time-series. Originally intended for ecological segmentation
(home-range and behavioural modes) but easily applied on other series, the
package also provides tools for analysing outputs from R packages
'moveHMM' and 'marcher'. The segmentation method is a bivariate extension
of Lavielle's method available in 'adehabitatLT' (Lavielle, 1999
<doi:10.1016/S0304-4149(99)00023-X> and 2005
<doi:10.1016/j.sigpro.2005.01.012>). This method rely on dynamic
programming for efficient segmentation. The segmentation/clustering method
alternates steps of dynamic programming with an Expectation-Maximization
algorithm. This is an extension of Picard et al (2007)
<doi:10.1111/j.1541-0420.2006.00729.x> method (formerly available in
'cghseg' package) to the bivariate case. The method is fully described in
Patin et al (2018) <doi:10.1101/444794>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

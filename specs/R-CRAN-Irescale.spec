%global packname  Irescale
%global packver   2.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Calculate and Rectify Moran's I

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-fBasics 
BuildRequires:    R-CRAN-imager 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-e1071 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-fBasics 
Requires:         R-CRAN-imager 
Requires:         R-CRAN-reshape2 

%description
Provides a scaling method to obtain a standardized Moran's I measure.
Moran's I is a measure for the spatial autocorrelation of a data set, it
gives a measure of similarity between data and its surrounding. The range
of this value must be [-1,1], but this does not happen in practice. This
package scale the Moran's I value and map it into the theoretical range of
[-1,1]. Once the Moran's I value is rescaled, it facilitates the
comparison between projects, for instance, a researcher can calculate
Moran's I in a city in China, with a sample size of n1 and area of
interest a1. Another researcher runs a similar experiment in a city in
Mexico with different sample size, n2, and an area of interest a2. Due to
the differences between the conditions, it is not possible to compare
Moran's I in a straightforward way. In this version of the package, the
spatial autocorrelation Moran's I is calculated as proposed in Chen(2013)
<arXiv:1606.03658>.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/testdata
%{rlibdir}/%{packname}/INDEX

%global packname  densityClust
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          3%{?dist}
Summary:          Clustering by Fast Search and Find of Density Peaks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-grDevices 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-RColorBrewer 

%description
An improved implementation (based on k-nearest neighbors) of the density
peak clustering algorithm, originally described by Alex Rodriguez and
Alessandro Laio (Science, 2014 vol. 344). It can handle large datasets (>
100, 000 samples) very efficiently. It was initially implemented by Thomas
Lin Pedersen, with inputs from Sean Hughes and later improved by Xiaojie
Qiu to handle large datasets with kNNs.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

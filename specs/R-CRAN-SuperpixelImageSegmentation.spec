%global packname  SuperpixelImageSegmentation
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Superpixel Image Segmentation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.10
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-OpenImageR 
BuildRequires:    R-grDevices 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-ClusterR 
Requires:         R-CRAN-Rcpp >= 0.12.10
Requires:         R-CRAN-R6 
Requires:         R-CRAN-OpenImageR 
Requires:         R-grDevices 
Requires:         R-lattice 

%description
Image Segmentation using Superpixels, Affinity Propagation and Kmeans
Clustering. The R code is based primarily on the article "Image
Segmentation using SLIC Superpixels and Affinity Propagation Clustering,
Bao Zhou, International Journal of Science and Research (IJSR), 2013"
<https://pdfs.semanticscholar.org/6533/654973054b742e725fd433265700c07b48a2.pdf>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/images
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

%global packname  ClusterR
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          Gaussian Mixture Models, K-Means, Mini-Batch-Kmeans, K-Medoidsand Affinity Propagation Clustering

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.5
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-Rcpp >= 0.12.5
Requires:         R-CRAN-gtools 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-gmp 
Requires:         R-CRAN-ggplot2 

%description
Gaussian mixture models, k-means, mini-batch-kmeans, k-medoids and
affinity propagation clustering with the option to plot, validate, predict
(new data) and estimate the optimal number of clusters. The package takes
advantage of 'RcppArmadillo' to speed up the computationally intensive
parts of the functions. For more information, see (i) "Clustering in an
Object-Oriented Environment" by Anja Struyf, Mia Hubert, Peter Rousseeuw
(1997), Journal of Statistical Software, <doi:10.18637/jss.v001.i04>; (ii)
"Web-scale k-means clustering" by D. Sculley (2010), ACM Digital Library,
<doi:10.1145/1772690.1772862>; (iii) "Armadillo: a template-based C++
library for linear algebra" by Sanderson et al (2016), The Journal of Open
Source Software, <doi:10.21105/joss.00026>; (iv) "Clustering by Passing
Messages Between Data Points" by Brendan J. Frey and Delbert Dueck,
Science 16 Feb 2007: Vol. 315, Issue 5814, pp. 972-976,
<doi:10.1126/science.1136800>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

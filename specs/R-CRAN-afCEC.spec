%global packname  afCEC
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Active Function Cross-Entropy Clustering

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-graphics 
Requires:         R-CRAN-rgl 

%description
Active function cross-entropy clustering partitions the n-dimensional data
into the clusters by finding the parameters of the mixed generalized
multivariate normal distribution, that optimally approximates the
scattering of the data in the n-dimensional space, whose density function
is of the form:
p_1*N(mi_1,^sigma_1,sigma_1,f_1)+...+p_k*N(mi_k,^sigma_k,sigma_k,f_k). The
above-mentioned generalization is performed by introducing so called
"f-adapted Gaussian densities" (i.e. the ordinary Gaussian densities
adapted by the "active function"). Additionally, the active function
cross-entropy clustering performs the automatic reduction of the
unnecessary clusters. For more information please refer to P. Spurek, J.
Tabor, K.Byrski, "Active function Cross-Entropy Clustering" (2017)
<doi:10.1016/j.eswa.2016.12.011>.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

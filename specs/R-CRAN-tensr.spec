%global packname  tensr
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          2%{?dist}
Summary:          Covariance Inference and Decompositions for Tensor Datasets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
Requires:         R-CRAN-assertthat 

%description
A collection of functions for Kronecker structured covariance estimation
and testing under the array normal model. For estimation, maximum
likelihood and Bayesian equivariant estimation procedures are implemented.
For testing, a likelihood ratio testing procedure is available. This
package also contains additional functions for manipulating and
decomposing tensor data sets. This work was partially supported by NSF
grant DMS-1505136. Details of the methods are described in Gerard and Hoff
(2015) <doi:10.1016/j.jmva.2015.01.020> and Gerard and Hoff (2016)
<doi:10.1016/j.laa.2016.04.033>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

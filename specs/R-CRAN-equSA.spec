%global packname  equSA
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          2%{?dist}
Summary:          Learning High-Dimensional Graphical Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-huge 
BuildRequires:    R-CRAN-XMRF 
BuildRequires:    R-CRAN-ZIM 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-speedglm 
BuildRequires:    R-CRAN-SIS 
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-bnlearn 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-huge 
Requires:         R-CRAN-XMRF 
Requires:         R-CRAN-ZIM 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-speedglm 
Requires:         R-CRAN-SIS 
Requires:         R-CRAN-ncvreg 
Requires:         R-survival 
Requires:         R-CRAN-bnlearn 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 

%description
Provides an equivalent measure of partial correlation coefficients for
high-dimensional Gaussian Graphical Models to learn and visualize the
underlying relationships between variables from single or multiple
datasets. You can refer to Liang, F., Song, Q. and Qiu, P. (2015)
<doi:10.1080/01621459.2015.1012391> for more detail. Based on this method,
the package also provides the method for constructing networks for Next
Generation Sequencing Data, jointly estimating multiple Gaussian Graphical
Models, constructing single graphical model for heterogeneous dataset,
inferring graphical models from high-dimensional missing data and
estimating moral graph for Bayesian network.

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

%global __brp_check_rpaths %{nil}
%global packname  simule
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          A Constrained L1 Minimization Approach for Estimating MultipleSparse Gaussian or Nonparanormal Graphical Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-pcaPP 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-pcaPP 
Requires:         R-CRAN-igraph 

%description
This is an R implementation of a constrained l1 minimization approach for
estimating multiple Sparse Gaussian or Nonparanormal Graphical Models
(SIMULE). The SIMULE algorithm can be used to estimate multiple related
precision matrices. For instance, it can identify context-specific gene
networks from multi-context gene expression datasets. By performing
data-driven network inference from high-dimensional and heterogenous data
sets, this tool can help users effectively translate aggregated data into
knowledge that take the form of graphs among entities. Please run
demo(simuleDemo) to learn the basic functions provided by this package.
For further details, please read the original paper: Beilun Wang,
Ritambhara Singh, Yanjun Qi (2017) <DOI:10.1007/s10994-017-5635-7>.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX

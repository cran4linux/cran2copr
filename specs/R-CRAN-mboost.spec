%global packname  mboost
%global packver   2.9-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.9.2
Release:          1%{?dist}
Summary:          Model-Based Boosting

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-partykit >= 1.2.1
BuildRequires:    R-CRAN-stabs >= 0.5.0
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
BuildRequires:    R-Matrix 
BuildRequires:    R-survival 
BuildRequires:    R-splines 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-nnls 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-partykit >= 1.2.1
Requires:         R-CRAN-stabs >= 0.5.0
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-parallel 
Requires:         R-Matrix 
Requires:         R-survival 
Requires:         R-splines 
Requires:         R-lattice 
Requires:         R-CRAN-nnls 
Requires:         R-CRAN-quadprog 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Functional gradient descent algorithm (boosting) for optimizing general
risk functions utilizing component-wise (penalised) least squares
estimates or regression trees as base-learners for fitting generalized
linear, additive and interaction models to potentially high-dimensional
data.

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
%doc %{rlibdir}/%{packname}/birds_Biometrics.R
%doc %{rlibdir}/%{packname}/cache
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/india_additive.R
%doc %{rlibdir}/%{packname}/india_analysis.R
%doc %{rlibdir}/%{packname}/india_blackboost.R
%doc %{rlibdir}/%{packname}/india_helpfunc.R
%doc %{rlibdir}/%{packname}/india_plots.R
%doc %{rlibdir}/%{packname}/india_preproc.R
%doc %{rlibdir}/%{packname}/India_quantiles.R
%doc %{rlibdir}/%{packname}/india_rqss_lambdaOptFunc.R
%doc %{rlibdir}/%{packname}/india_rqss.R
%doc %{rlibdir}/%{packname}/india_rqssResults.R
%doc %{rlibdir}/%{packname}/india_stumps.R
%doc %{rlibdir}/%{packname}/india_summary.R
%doc %{rlibdir}/%{packname}/india_vcm.R
%doc %{rlibdir}/%{packname}/mboost_Bioinf.R
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/readAML_Bullinger.R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

%global packname  TVsMiss
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Variable Selection for Missing Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-Rcpp 

%description
Use a regularization likelihood method to achieve variable selection
purpose. Likelihood can be worked with penalty lasso, smoothly clipped
absolute deviations (SCAD), and minimax concave penalty (MCP). Tuning
parameter selection techniques include cross validation (CV), Bayesian
information criterion (BIC) (low and high), stability of variable
selection (sVS), stability of BIC (sBIC), and stability of estimation
(sEST). More details see Jiwei Zhao, Yang Yang, and Yang Ning (2018)
<arXiv:1703.06379> "Penalized pairwise pseudo likelihood for variable
selection with nonignorable missing data." Statistica Sinica.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

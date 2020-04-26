%global packname  ROCnReg
%global packver   1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          ROC Curve Inference with and without Covariates

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-np 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-nor1mix 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-lattice 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-pbivnorm 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-splines 
Requires:         R-CRAN-np 
Requires:         R-Matrix 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-nor1mix 
Requires:         R-CRAN-spatstat 
Requires:         R-lattice 
Requires:         R-MASS 
Requires:         R-CRAN-pbivnorm 

%description
Estimates the pooled (unadjusted) Receiver Operating Characteristic (ROC)
curve, the covariate-adjusted ROC (AROC) curve, and the
covariate-specific/conditional ROC (cROC) curve by different methods, both
Bayesian and frequentist. Also, it provides functions to obtain ROC-based
optimal cutpoints utilizing several criteria. Based on Erkanli, A. et al.
(2006) <doi:10.1002/sim.2496>; Faraggi, D. (2003)
<doi:10.1111/1467-9884.00350>; Gu, J. et al. (2008)
<doi:10.1002/sim.3366>; Inacio de Carvalho, V. et al. (2013)
<doi:10.1214/13-BA825>; Inacio de Carvalho, V., and Rodriguez-Alvarez,
M.X. (2018) <arXiv:1806.00473>; Janes, H., and Pepe, M.S. (2009)
<doi:10.1093/biomet/asp002>; Pepe, M.S. (1998)
<https://www.jstor.org/stable/2534001?seq=1>; Rodriguez-Alvarez, M.X. et
al. (2011a) <doi:10.1016/j.csda.2010.07.018>; Rodriguez-Alvarez, M.X. et
al. (2011a) <doi:10.1007/s11222-010-9184-1>. Please see Rodriguez-Alvarez,
M.X. and Inacio, V. (20208) <arXiv:2003.13111> for more details.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX

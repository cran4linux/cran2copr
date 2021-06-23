%global __brp_check_rpaths %{nil}
%global packname  LCAvarsel
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Variable Selection for Latent Class Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-poLCA >= 1.4.1
BuildRequires:    R-nnet 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-GA 
BuildRequires:    R-CRAN-memoise 
Requires:         R-CRAN-poLCA >= 1.4.1
Requires:         R-nnet 
Requires:         R-MASS 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-GA 
Requires:         R-CRAN-memoise 

%description
Variable selection for latent class analysis for model-based clustering of
multivariate categorical data. The package implements a general framework
for selecting the subset of variables with relevant clustering information
and discard those that are redundant and/or not informative. The variable
selection method is based on the approach of Fop et al. (2017)
<doi:10.1214/17-AOAS1061> and Dean and Raftery (2010)
<doi:10.1007/s10463-009-0258-9>. Different algorithms are available to
perform the selection: stepwise, swap-stepwise and evolutionary stochastic
search. Concomitant covariates used to predict the class membership
probabilities can also be included in the latent class analysis model. The
selection procedure can be run in parallel on multiple cores machines.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX

%global packname  mase
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Model-Assisted Survey Estimators

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rpms 
BuildRequires:    R-boot 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-glmnet 
Requires:         R-Matrix 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rpms 
Requires:         R-boot 
Requires:         R-stats 
Requires:         R-CRAN-Rdpack 

%description
A set of model-assisted survey estimators and corresponding variance
estimators for single stage, unequal probability, without replacement
sampling designs.  All of the estimators can be written as a generalized
regression estimator with the Horvitz-Thompson, ratio, post-stratified,
and regression estimators summarized by Sarndal et al. (1992,
ISBN:978-0-387-40620-6). Two of the estimators employ a statistical
learning model as the assisting model: the elastic net regression
estimator, which is an extension of the lasso regression estimator given
by McConville et al. (2017) <doi:10.1093/jssam/smw041>, and the regression
tree estimator described in McConville and Toth (2017) <arXiv:1712.05708>.
The variance estimators which approximate the joint inclusion
probabilities can be found in Berger and Tille (2009)
<doi:10.1016/S0169-7161(08)00002-3> and the bootstrap variance estimator
is presented in Mashreghi et al. (2016) <doi:10.1214/16-SS113>.

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
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX

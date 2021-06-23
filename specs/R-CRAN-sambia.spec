%global __brp_check_rpaths %{nil}
%global packname  sambia
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          A Collection of Techniques Correcting for Sample Selection Bias

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-smotefamily 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-FNN 
Requires:         R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-smotefamily 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-FNN 

%description
A collection of various techniques correcting statistical models for
sample selection bias is provided. In particular, the resampling-based
methods "stochastic inverse-probability oversampling" and "parametric
inverse-probability bagging" are placed at the disposal which generate
synthetic observations for correcting classifiers for biased samples
resulting from stratified random sampling. For further information, see
the article Krautenbacher, Theis, and Fuchs (2017)
<doi:10.1155/2017/7847531>. The methods may be used for further purposes
where weighting and generation of new observations is needed.

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
%{rlibdir}/%{packname}/INDEX

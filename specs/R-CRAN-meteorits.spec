%global __brp_check_rpaths %{nil}
%global packname  meteorits
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Mixture-of-Experts Modeling for Complex Non-Normal Distributions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-pracma 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-MASS 
Requires:         R-CRAN-Rcpp 

%description
Provides a unified mixture-of-experts (ME) modeling and estimation
framework with several original and flexible ME models to model, cluster
and classify heterogeneous data in many complex situations where the data
are distributed according to non-normal, possibly skewed distributions,
and when they might be corrupted by atypical observations.
Mixtures-of-Experts models for complex and non-normal distributions
('meteorits') are originally introduced and written in 'Matlab' by Faicel
Chamroukhi. The references are mainly the following ones. The references
are mainly the following ones. Chamroukhi F., Same A., Govaert, G. and
Aknin P. (2009) <doi:10.1016/j.neunet.2009.06.040>. Chamroukhi F. (2010)
<https://chamroukhi.com/FChamroukhi-PhD.pdf>. Chamroukhi F. (2015)
<arXiv:1506.06707>. Chamroukhi F. (2015)
<https://chamroukhi.com/FChamroukhi-HDR.pdf>. Chamroukhi F. (2016)
<doi:10.1109/IJCNN.2016.7727580>. Chamroukhi F. (2016)
<doi:10.1016/j.neunet.2016.03.002>. Chamroukhi F. (2017)
<doi:10.1016/j.neucom.2017.05.044>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}

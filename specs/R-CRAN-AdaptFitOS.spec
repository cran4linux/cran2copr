%global packname  AdaptFitOS
%global packver   0.67
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.67
Release:          3%{?dist}
Summary:          Adaptive Semiparametric Additive Regression with SimultaneousConfidence Bands and Specification Tests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-nlme 
BuildRequires:    R-MASS 
BuildRequires:    R-splines 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-SemiPar 
Requires:         R-nlme 
Requires:         R-MASS 
Requires:         R-splines 
Requires:         R-mgcv 
Requires:         R-CRAN-SemiPar 

%description
Fits semiparametric additive regression models with spatially adaptive
penalized splines and computes simultaneous confidence bands and
associated specification (lack-of-fit) tests. Simultaneous confidence
bands cover the entire curve with a prescribed level of confidence and
allow us to assess the estimation uncertainty for the whole curve. In
contrast to pointwise confidence bands, they permit statements about the
statistical significance of certain features (e.g. bumps) in the
underlying curve.The method allows for handling of spatially heterogeneous
functions and their derivatives as well as heteroscedasticity in the data.
See Wiesenfarth et al (2012) <doi:10.1080/01621459.2012.682809>.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

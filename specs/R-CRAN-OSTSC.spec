%global packname  OSTSC
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          2%{?dist}
Summary:          Over Sampling for Time Series Classification

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-fields 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-foreach 

%description
Oversampling of imbalanced univariate time series classification data
using integrated ESPO and ADASYN methods. Enhanced Structure Preserving
Oversampling (ESPO) is used to generate a large percentage of the
synthetic minority samples from univariate labeled time series under the
modeling assumption that the predictors are Gaussian. ESPO estimates the
covariance structure of the minority-class samples and applies a spectral
filer to reduce noise. Adaptive Synthetic (ADASYN) sampling approach is a
nearest neighbor interpolation approach which is subsequently applied to
the ESPO samples. This code is ported from a 'MATLAB' implementation by
Cao et al. <doi:10.1109/TKDE.2013.37> and adapted for use with Recurrent
Neural Networks implemented in 'TensorFlow'.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

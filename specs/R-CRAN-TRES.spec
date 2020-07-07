%global packname  TRES
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}
Summary:          Tensor Regression with Envelope Structure and Three GenericEnvelope Estimation Approaches

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ManifoldOptim 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-rTensor 
BuildRequires:    R-stats 
Requires:         R-CRAN-ManifoldOptim 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-rTensor 
Requires:         R-stats 

%description
Provides three estimators for tensor response regression (TRR) and tensor
predictor regression (TPR) models with tensor envelope structure. The
three types of estimation approaches are generic and can be applied to any
envelope estimation problems. The full Grassmannian (FG) optimization is
often associated with likelihood-based estimation but requires heavy
computation and good initialization; the one-directional optimization
approaches (1D and ECD algorithms) are faster, stable and does not require
carefully chosen initial values; the SIMPLS-type is motivated by the
partial least squares regression and is computationally the least
expensive. For details of TRR, see Li L, Zhang X (2017)
<doi:10.1080/01621459.2016.1193022>. For details of TPR, see Zhang X, Li L
(2017) <doi:10.1080/00401706.2016.1272495>. For details of 1D algorithm,
see Cook RD, Zhang X (2016) <doi:10.1080/10618600.2015.1029577>. For
details of ECD algorithm, see Cook RD, Zhang X (2018)
<doi:10.5705/ss.202016.0037>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX

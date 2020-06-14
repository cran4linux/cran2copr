%global packname  StatPerMeCo
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Statistical Performance Measures to Evaluate Covariance MatrixEstimates

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Statistical performance measures used in the econometric literature to
evaluate conditional covariance/correlation matrix estimates (MSE, MAE,
Euclidean distance, Frobenius distance, Stein distance, asymmetric loss
function, eigenvalue loss function and the loss function defined in Eq.
(4.6) of Engle et al. (2016) <doi:10.2139/ssrn.2814555>). Additionally,
compute Eq. (3.1) and (4.2) of Li et al. (2016)
<doi:10.1080/07350015.2015.1092975> to compare the factor loading matrix.
The statistical performance measures implemented have been previously used
in, for instance, Laurent et al. (2012) <doi:10.1002/jae.1248>, Amendola
et al. (2015) <doi:10.1002/for.2322> and Becker et al. (2015)
<doi:10.1016/j.ijforecast.2013.11.007>.

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

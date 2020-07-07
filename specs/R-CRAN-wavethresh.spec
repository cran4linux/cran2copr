%global packname  wavethresh
%global packver   4.6.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.6.8
Release:          3%{?dist}
Summary:          Wavelets Statistics and Transforms

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-MASS 
Requires:         R-MASS 

%description
Performs 1, 2 and 3D real and complex-valued wavelet transforms,
nondecimated transforms, wavelet packet transforms, nondecimated wavelet
packet transforms, multiple wavelet transforms, complex-valued wavelet
transforms, wavelet shrinkage for various kinds of data, locally
stationary wavelet time series, nonstationary multiscale transfer function
modeling, density estimation.

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
%doc %{rlibdir}/%{packname}/CHANGES
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

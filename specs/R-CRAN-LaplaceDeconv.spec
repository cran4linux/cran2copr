%global packname  LaplaceDeconv
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          Laplace Deconvolution with Noisy Discrete Non-Equally SpacedObservations on a Finite Time Interval

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-polynom 
BuildRequires:    R-CRAN-orthopolynom 
Requires:         R-parallel 
Requires:         R-CRAN-polynom 
Requires:         R-CRAN-orthopolynom 

%description
Solves the problem of Laplace deconvolution with noisy discrete
non-equally spaced observations on a finite time interval based on
expansions of the convolution kernel, the unknown function and the
observed signal over Laguerre functions basis. It implements the
methodology proposed in the paper "Laplace deconvolution on the basis of
time domain data and its application to Dynamic Contrast Enhanced imaging"
by F. Comte, C-A. Cuenod, M. Pensky and Y. Rozenholc in ArXiv
(http://arxiv.org/abs/1405.7107).

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX

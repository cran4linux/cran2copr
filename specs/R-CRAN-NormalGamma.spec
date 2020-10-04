%global packname  NormalGamma
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Normal-gamma convolution model

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-histogram 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-histogram 

%description
The functions proposed in this package compute the density of the sum of a
Gaussian and a gamma random variables, estimate the parameters and correct
the noise effect in a gamma-signal and Gaussian-noise model. This package
has been used to implement the background correction method for Illumina
microarray data presented in Plancade S., Rozenholc Y. and Lund E.
"Generalization of the normal-exponential model : exploration of a more
accurate parameterization for the signal distribution on Illumina
BeadArrays", BMC Bioinfo 2012, 13(329).

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
%{rlibdir}/%{packname}/INDEX

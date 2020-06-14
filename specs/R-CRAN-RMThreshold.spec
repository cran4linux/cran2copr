%global packname  RMThreshold
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          2%{?dist}
Summary:          Signal-Noise Separation in Random Matrices by using EigenvalueSpectrum Analysis

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-png 
Requires:         R-Matrix 
Requires:         R-CRAN-png 

%description
An algorithm which can be used to determine an objective threshold for
signal-noise separation in large random matrices (correlation matrices,
mutual information matrices, network adjacency matrices) is provided. The
package makes use of the results of Random Matrix Theory (RMT). The
algorithm increments a suppositional threshold monotonically, thereby
recording the eigenvalue spacing distribution of the matrix. According to
RMT, that distribution undergoes a characteristic change when the
threshold properly separates signal from noise. By using the algorithm,
the modular structure of a matrix - or of the corresponding network - can
be unraveled.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

%global packname  keras
%global packver   2.2.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.5.0
Release:          1%{?dist}
Summary:          R Interface to 'Keras'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-tensorflow >= 2.0.0
BuildRequires:    R-CRAN-reticulate >= 1.10
BuildRequires:    R-CRAN-tfruns >= 1.0
BuildRequires:    R-CRAN-generics >= 0.0.1
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-zeallot 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-tensorflow >= 2.0.0
Requires:         R-CRAN-reticulate >= 1.10
Requires:         R-CRAN-tfruns >= 1.0
Requires:         R-CRAN-generics >= 0.0.1
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-zeallot 
Requires:         R-methods 
Requires:         R-CRAN-R6 

%description
Interface to 'Keras' <https://keras.io>, a high-level neural networks
'API'. 'Keras' was developed with a focus on enabling fast
experimentation, supports both convolution based networks and recurrent
networks (as well as combinations of the two), and runs seamlessly on both
'CPU' and 'GPU' devices.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/python
%{rlibdir}/%{packname}/INDEX

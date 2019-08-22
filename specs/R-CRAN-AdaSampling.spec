%global packname  AdaSampling
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Adaptive Sampling for Positive Unlabeled and Label NoiseLearning

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caret >= 6.0.78
BuildRequires:    R-class >= 7.3.14
BuildRequires:    R-CRAN-e1071 >= 1.6.8
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
Requires:         R-CRAN-caret >= 6.0.78
Requires:         R-class >= 7.3.14
Requires:         R-CRAN-e1071 >= 1.6.8
Requires:         R-stats 
Requires:         R-MASS 

%description
Implements the adaptive sampling procedure, a framework for both positive
unlabeled learning and learning with class label noise. Yang, P., Ormerod,
J., Liu, W., Ma, C., Zomaya, A., Yang, J. (2018)
<doi:10.1109/TCYB.2018.2816984>.

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

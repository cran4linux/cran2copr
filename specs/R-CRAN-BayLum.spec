%global packname  BayLum
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Chronological Bayesian Models Integrating Optically StimulatedLuminescence and Radiocarbon Age Dating

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags >= 4.6
BuildRequires:    R-CRAN-Luminescence >= 0.8.2
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-hexbin 
BuildRequires:    R-KernSmooth 
BuildRequires:    R-CRAN-ArchaeoPhases 
Requires:         R-CRAN-rjags >= 4.6
Requires:         R-CRAN-Luminescence >= 0.8.2
Requires:         R-utils 
Requires:         R-CRAN-coda 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-hexbin 
Requires:         R-KernSmooth 
Requires:         R-CRAN-ArchaeoPhases 

%description
Bayesian analysis of luminescence data and C-14 age estimates. Bayesian
models are based on the following publications: Combes, B. & Philippe, A.
(2017) <doi:10.1016/j.quageo.2017.02.003> and Combes et al (2015)
<doi:10.1016/j.quageo.2015.04.001>. This includes, amongst others, data
import, export, application of age models and palaeodose model.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX

%global packname  randomizationInference
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}
Summary:          Flexible Randomization-Based Inference

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-permute >= 0.7.8
BuildRequires:    R-CRAN-matrixStats 
Requires:         R-CRAN-permute >= 0.7.8
Requires:         R-CRAN-matrixStats 

%description
Allows the user to conduct randomization-based inference for a wide
variety of experimental scenarios. The package leverages a potential
outcomes framework to output randomization-based p-values and null
intervals for test statistics geared toward any estimands of interest,
according to the specified null and alternative hypotheses. Users can
define custom randomization schemes so that the randomization
distributions are accurate for their experimental settings. The package
also creates visualizations of randomization distributions and can test
multiple test statistics simultaneously.

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

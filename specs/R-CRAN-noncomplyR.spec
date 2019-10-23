%global packname  noncomplyR
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Bayesian Analysis of Randomized Experiments with Non-Compliance

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MCMCpack >= 1.4.0
BuildRequires:    R-stats 
Requires:         R-CRAN-MCMCpack >= 1.4.0
Requires:         R-stats 

%description
Functions for Bayesian analysis of data from randomized experiments with
non-compliance. The functions are based on the models described in Imbens
and Rubin (1997) <doi:10.1214/aos/1034276631>. Currently only two types of
outcome models are supported: binary outcomes and normally distributed
outcomes. Models can be fit with and without the exclusion restriction
and/or the strong access monotonicity assumption. Models are fit using the
data augmentation algorithm as described in Tanner and Wong (1987)
<doi:10.2307/2289457>.

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

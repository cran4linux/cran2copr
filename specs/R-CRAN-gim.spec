%global packname  gim
%global packver   0.28.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.28.0
Release:          1%{?dist}
Summary:          Generalized Integration Model

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-numDeriv 

%description
Implements the generalized integration model, which integrates
individual-level data and summary statistics under a generalized linear
model framework. It supports continuous and binary outcomes to be modeled
by the linear and logistic regression models. For binary outcome, data can
be sampled in prospective cohort studies or case-control studies.

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

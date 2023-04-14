%global __brp_check_rpaths %{nil}
%global packname  InvariantCausalPrediction
%global packver   0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8
Release:          3%{?dist}%{?buildtag}
Summary:          Invariant Causal Prediction

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-mboost 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-mboost 

%description
Confidence intervals for causal effects, using data collected in different
experimental or environmental conditions. Hidden variables can be included
in the model with a more experimental version.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}

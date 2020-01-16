%global packname  PAMA
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Rank Aggregation with Partition Mallows Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-PerMallows 
BuildRequires:    R-CRAN-mc2d 
BuildRequires:    R-stats 
Requires:         R-CRAN-PerMallows 
Requires:         R-CRAN-mc2d 
Requires:         R-stats 

%description
Rank aggregation aims to achieve a better ranking list given multiple
observations. 'PAMA' implements Partition-Mallows model for rank
aggregation. Both Bayesian inference and Maximum likelihood estimation
(MLE) are provided. It can handle partial list as well. When covariates
information is available, this package can make inference by incorporating
the covariate information. More information can be found in the paper
"Integrated Partition-Mallows Model and Its Inference for Rank
Aggregation". The paper is not yet published.

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
%{rlibdir}/%{packname}/INDEX

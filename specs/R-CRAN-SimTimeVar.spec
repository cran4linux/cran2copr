%global packname  SimTimeVar
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}
Summary:          Simulate Longitudinal Dataset with Time-Varying CorrelatedCovariates

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ICC 
BuildRequires:    R-CRAN-miscTools 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ICC 
Requires:         R-CRAN-miscTools 
Requires:         R-CRAN-car 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-psych 
Requires:         R-stats 
Requires:         R-utils 

%description
Flexibly simulates a dataset with time-varying covariates with
user-specified exchangeable correlation structures across and within
clusters. Covariates can be normal or binary and can be static within a
cluster or time-varying. Time-varying normal variables can optionally have
linear trajectories within each cluster. See ?make_one_dataset for the
main wrapper function. See Montez-Rath et al. <arXiv:1709.10074> for
methodological details.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}

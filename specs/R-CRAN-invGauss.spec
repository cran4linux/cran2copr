%global __brp_check_rpaths %{nil}
%global packname  invGauss
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Threshold regression that fits the (randomized drift) inverseGaussian distribution to survival data.

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-optimx 
Requires:         R-survival 
Requires:         R-CRAN-optimx 

%description
invGauss fits the (randomized drift) inverse Gaussian distribution to
survival data. The model is described in Aalen OO, Borgan O, Gjessing HK.
Survival and Event History Analysis. A Process Point of View. Springer,
2008. It is based on describing time to event as the barrier hitting time
of a Wiener process, where drift towards the barrier has been randomized
with a Gaussian distribution. The model allows covariates to influence
starting values of the Wiener process and/or average drift towards a
barrier, with a user-defined choice of link functions.

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

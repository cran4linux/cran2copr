%global packname  clusterSEs
%global packver   2.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6.2
Release:          1%{?dist}
Summary:          Calculate Cluster-Robust p-Values and Confidence Intervals

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-AER 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-plm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-mlogit 
BuildRequires:    R-utils 
Requires:         R-CRAN-AER 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-plm 
Requires:         R-stats 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-mlogit 
Requires:         R-utils 

%description
Calculate p-values and confidence intervals using cluster-adjusted
t-statistics (based on Ibragimov and Muller (2010)
<DOI:10.1198/jbes.2009.08046>, pairs cluster bootstrapped t-statistics,
and wild cluster bootstrapped t-statistics (the latter two techniques
based on Cameron, Gelbach, and Miller (2008) <DOI:10.1162/rest.90.3.414>.
Procedures are included for use with GLM, ivreg, plm (pooling or fixed
effects), and mlogit models.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX

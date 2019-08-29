%global packname  forestinventory
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Design-Based Global and Small-Area Estimations for MultiphaseForest Inventories

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr >= 1.8.3
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-plyr >= 1.8.3
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 

%description
Extensive global and small-area estimation procedures for multiphase
forest inventories under the design-based Monte-Carlo approach are
provided. The implementation includes estimators for simple and cluster
sampling published by Daniel Mandallaz in 2007
(<DOI:10.1201/9781584889779>), 2013 (<DOI:10.1139/cjfr-2012-0381>,
<DOI:10.1139/cjfr-2013-0181>, <DOI:10.1139/cjfr-2013-0449>,
<DOI:10.3929/ethz-a-009990020>) and 2016 (<DOI:10.3929/ethz-a-010579388>).
It provides point estimates, their external- and design-based variances as
well as confidence intervals. The procedures have also been optimized for
the use of remote sensing data as auxiliary information.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

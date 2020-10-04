%global packname  dfmeta
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Meta-Analysis of Phase I Dose-Finding Early Clinical Trials

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-lme4 
Requires:         R-stats4 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-data.table 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 

%description
Meta-analysis approaches for Phase I dose finding early phases clinical
trials in order to better suit requirements in terms of maximum tolerated
dose (MTD) and maximal dose regimen (MDR). This package has currently
three different approaches: (a) an approach proposed by Zohar et al, 2011,
<doi:10.1002/sim.4121> (denoted as ZKO), (b) the Variance Weighted pooling
analysis (called VarWT) and (c) the Random Effects Model Based (REMB)
algorithm, where user can input his/her own model based approach or use
the existing random effect logistic regression model (named as glimem)
through the 'dfmeta' package.

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

%global packname  metaBLUE
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          BLUE for Combining Location and Scale Information in aMeta-Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-Matrix 
Requires:         R-stats 
Requires:         R-Matrix 

%description
The sample mean and standard deviation are two commonly used statistics in
meta-analyses, but some trials use other summary statistics such as the
median and quartiles to report the results. Therefore, researchers need to
transform those information back to the sample mean and standard
deviation. This package implemented sample mean estimators by Luo et al.
(2016) <arXiv:1505.05687>, sample standard deviation estimators by Wan et
al. (2014) <arXiv:1407.8038>, and the best linear unbiased estimators
(BLUEs) of location and scale parameters by Yang et al. (2018, submitted)
based on sample quantiles derived summaries in a meta-analysis.

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

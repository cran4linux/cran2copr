%global packname  permuco
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Permutation Tests for Regression, (Repeated Measures)ANOVA/ANCOVA and Comparison of Signals

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-permute 
BuildRequires:    R-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-permute 
Requires:         R-Matrix 
Requires:         R-stats 
Requires:         R-graphics 

%description
Functions to compute p-values based on permutation tests. Regression,
ANOVA and ANCOVA, omnibus F-tests, marginal unilateral and bilateral
t-tests are available. Several methods to handle nuisance variables are
implemented (Kherad-Pajouh, S., & Renaud, O. (2010)
<doi:10.1016/j.csda.2010.02.015> ; Kherad-Pajouh, S., & Renaud, O. (2014)
<doi:10.1007/s00362-014-0617-3> ; Winkler, A. M., Ridgway, G. R., Webster,
M. A., Smith, S. M., & Nichols, T. E. (2014)
<doi:10.1016/j.neuroimage.2014.01.060>). An extension for the comparison
of signals issued from experimental conditions (e.g. EEG/ERP signals) is
provided. Several corrections for multiple testing are possible, including
the cluster-mass statistic (Maris, E., & Oostenveld, R. (2007)
<doi:10.1016/j.jneumeth.2007.03.024>) and the threshold-free cluster
enhancement (Smith, S. M., & Nichols, T. E. (2009)
<doi:10.1016/j.neuroimage.2008.03.061>).

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

%global __brp_check_rpaths %{nil}
%global packname  APFr
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Multiple Testing Approach using Average Power Function (APF) andBayes FDR Robust Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.5.2
BuildRequires:    R-graphics >= 3.5.2
Requires:         R-stats >= 3.5.2
Requires:         R-graphics >= 3.5.2

%description
Implements a multiple testing approach to the choice of a threshold gamma
on the p-values using the Average Power Function (APF) and Bayes False
Discovery Rate (FDR) robust estimation. Function apf_fdr() estimates both
quantities from either raw data or p-values. Function apf_plot() produces
smooth graphs and tables of the relevant results. Details of the methods
can be found in Quatto P, Margaritella N, et al. (2019)
<doi:10.1177/0962280219844288>.

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

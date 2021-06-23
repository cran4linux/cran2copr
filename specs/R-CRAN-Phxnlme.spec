%global __brp_check_rpaths %{nil}
%global packname  Phxnlme
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Run Phoenix NLME and Perform Post-Processing

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-manipulate 
BuildRequires:    R-grid 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-manipulate 
Requires:         R-grid 
Requires:         R-lattice 
Requires:         R-CRAN-testthat 

%description
Calls 'Phoenix NLME' (non-linear mixed effects), a population modeling and
simulation software, for pharmacokinetics and pharmacodynamics analyses
and conducts post-processing of the results. This includes creation of
various diagnostic plots, bootstrap and visual predictive checks. See
<http://
www.certara.com/software/pkpd-modeling-and-simulation/phoenix-nlme/> for
more information about 'Phoenix NLME'.

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

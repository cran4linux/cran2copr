%global packname  MetaUtility
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Utility Functions for Conducting and Interpreting Meta-Analyses

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-metafor 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-dplyr 

%description
Contains functions to estimate the proportion of effects stronger than a
threshold of scientific importance (function prop_stronger), to
nonparametrically characterize the distribution of effects in a
meta-analysis (calib_ests, pct_pval), to make effect size conversions
(r_to_d, r_to_z, z_to_r), to compute and format inference in a
meta-analysis (format_CI, format_stat, tau_CI), to scrape results from
existing meta-analyses for re-analysis (scrape_meta, parse_CI_string).

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

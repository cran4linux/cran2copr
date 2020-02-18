%global packname  httk
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}
Summary:          High-Throughput Toxicokinetics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-methods 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-truncnorm 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-methods 

%description
Functions and data tables for simulation and statistical analysis of
chemical toxicokinetics ("TK") as in Pearce et al. (2017)
<doi:10.18637/jss.v079.i04>. Chemical-specific in vitro data have been
obtained from relatively high throughput experiments. Both
physiologically-based ("PBTK") and empirical (e.g., one compartment) "TK"
models can be parameterized for several hundred chemicals and multiple
species. These models are solved efficiently, often using compiled
(C-based) code. A Monte Carlo sampler is included for simulating
biological variability (Ring et al., 2017
<doi:10.1016/j.envint.2017.06.004>) and measurement limitations.
Calibrated methods are included for predicting tissue:plasma partition
coefficients and volume of distribution (Pearce et al., 2017
<doi:10.1007/s10928-017-9548-7>). These functions and data provide a set
of tools for in vitro-in vivo extrapolation ("IVIVE") of high throughput
screening data (e.g., Tox21, ToxCast) to real-world exposures via reverse
dosimetry (also known as "RTK") (Wetmore et al., 2015
<doi:10.1093/toxsci/kfv171>).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/libs

%global packname  RLumCarlo
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          2%{?dist}
Summary:          Monte-Carlo Methods for Simulating Luminescence Phenomena

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-foreach >= 1.5.0
BuildRequires:    R-CRAN-abind >= 1.4.5
BuildRequires:    R-CRAN-khroma >= 1.3.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.4
BuildRequires:    R-CRAN-doParallel >= 1.0.15
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.850.1.0
BuildRequires:    R-CRAN-scatterplot3d >= 0.3
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
Requires:         R-CRAN-foreach >= 1.5.0
Requires:         R-CRAN-abind >= 1.4.5
Requires:         R-CRAN-khroma >= 1.3.0
Requires:         R-CRAN-Rcpp >= 1.0.4
Requires:         R-CRAN-doParallel >= 1.0.15
Requires:         R-CRAN-scatterplot3d >= 0.3
Requires:         R-utils 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-stats 

%description
A collection of functions to simulate luminescence production in
dosimetric materials using Monte Carlo methods. Implemented are models for
delocalised transitions (e.g., Chen and McKeever (1997)
<doi:10.1142/2781>), localised transitions (e.g., Pagonis et al. (2019)
<doi:10.1016/j.jlumin.2018.11.024>) and tunnelling transitions (Jain et
al. (2012) <doi:10.1088/0953-8984/24/38/385402> and Pagonis et al. (2019)
<doi:10.1016/j.jlumin.2018.11.024>). Supported stimulation methods are
thermal luminescence (TL), continuous-wave optically stimulated
luminescence (CW-OSL), linearly-modulated optically stimulated
luminescence (LM-OSL), linearly-modulated infrared stimulated luminescence
(LM-IRSL), and isothermal luminescence (ITL or ISO-TL).

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

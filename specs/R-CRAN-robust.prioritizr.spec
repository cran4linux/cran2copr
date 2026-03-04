%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  robust.prioritizr
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Systematic Conservation Prioritization

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-prioritizr >= 8.1.0
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-R6 >= 2.5.1
BuildRequires:    R-CRAN-tibble >= 2.0.0
BuildRequires:    R-CRAN-terra >= 1.8.54
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-sf >= 1.0.12
BuildRequires:    R-CRAN-units >= 0.8.7
BuildRequires:    R-CRAN-assertthat >= 0.2.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.10.7.3.0
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
Requires:         R-CRAN-prioritizr >= 8.1.0
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-R6 >= 2.5.1
Requires:         R-CRAN-tibble >= 2.0.0
Requires:         R-CRAN-terra >= 1.8.54
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-sf >= 1.0.12
Requires:         R-CRAN-units >= 0.8.7
Requires:         R-CRAN-assertthat >= 0.2.0
Requires:         R-utils 
Requires:         R-parallel 

%description
Systematic conservation prioritization with robust optimization
techniques. This is important because conservation prioritizations
typically only consider the most likely outcome associated with a
conservation action (e.g., establishing a protected area will safeguard a
threatened species population) and fail to consider other outcomes and
their consequences for meeting conservation objectives. By extending the
'prioritizr' package, this package can be used to generate conservation
prioritizations that account of uncertainty in the climate change scenario
projections, species distribution models, ecosystem service models, and
measurement errors. In particular, prioritizations can be generated to be
fully robust to uncertainty by minimizing (or maximizing) objectives under
the worst possible outcome. Since reducing the associated with achieving
conservation objectives may sacrifice other objectives (e.g., minimizing
protected area implementation costs), prioritizations can also be
generated to be partially robust based on a specified confidence level
parameter. Partially robust prioritizations can be generated based on the
chance constrained programming problem (Charnes & Cooper 1959,
<doi:10.1287/mnsc.6.1.73>) and the conditional value-at-risk problem
(Rockafellar & Uryasev 2000, <doi:10.21314/JOR.2000.038>).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}

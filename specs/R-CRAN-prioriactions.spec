%global __brp_check_rpaths %{nil}
%global packname  prioriactions
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Action Conservation Planning

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-assertthat >= 0.2.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.10.1.0.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-proto 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-Rsymphony 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-assertthat >= 0.2.0
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-proto 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-Rsymphony 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rlang 

%description
This uses a mixed integer mathematical programming (MIP) approach for
building and solving multi-action planning problems, where the goal is to
find an optimal combination of management actions that abate threats, in
an efficient way while accounting for spatial aspects. Thus, optimizing
the connectivity and conservation effectiveness of the prioritized units
and of the deployed actions. The package is capable of handling different
commercial (gurobi) and non-commercial (symphony) MIP solvers. Gurobi
optimization solver can be installed using comprehensive instructions in
the gurobi installation vignette of the prioritizr package (available in
<https://prioritizr.net/articles/gurobi_installation_guide.html>). Methods
used in the package refers to Salgado-Rojas et al. (2020)
<doi:10.1016/j.ecolmodel.2019.108901>, Beyer et al. (2016)
<doi:10.1016/j.ecolmodel.2016.02.005>, Cattarino et al. (2015)
<doi:10.1371/journal.pone.0128027> and Watts et al. (2009)
<doi:10.1016/j.envsoft.2009.06.005>. See the prioriactions website for
more information, documentations and examples.

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

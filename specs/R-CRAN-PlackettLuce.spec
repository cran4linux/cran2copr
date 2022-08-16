%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PlackettLuce
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Plackett-Luce Models for Rankings

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-CVXR 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-CRAN-psychotools 
BuildRequires:    R-CRAN-psychotree 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-qvcalc 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-stats 
Requires:         R-CRAN-CVXR 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-matrixStats 
Requires:         R-methods 
Requires:         R-CRAN-partykit 
Requires:         R-CRAN-psychotools 
Requires:         R-CRAN-psychotree 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-qvcalc 
Requires:         R-CRAN-sandwich 
Requires:         R-stats 

%description
Functions to prepare rankings data and fit the Plackett-Luce model jointly
attributed to Plackett (1975) <doi:10.2307/2346567> and Luce (1959,
ISBN:0486441369). The standard Plackett-Luce model is generalized to
accommodate ties of any order in the ranking. Partial rankings, in which
only a subset of items are ranked in each ranking, are also accommodated
in the implementation. Disconnected/weakly connected networks implied by
the rankings may be handled by adding pseudo-rankings with a hypothetical
item. Optionally, a multivariate normal prior may be set on the log-worth
parameters and ranker reliabilities may be incorporated as proposed by
Raman and Joachims (2014) <doi:10.1145/2623330.2623654>. Maximum a
posteriori estimation is used when priors are set. Methods are provided to
estimate standard errors or quasi-standard errors for inference as well as
to fit Plackett-Luce trees. See the package website or vignette for
further details.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rSRD
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Sum of Ranking Differences Statistical Test

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ggrepel 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-stringr 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ggrepel 

%description
We provide an implementation for Sum of Ranking Differences (SRD), a novel
statistical test introduced by Héberger (2010)
<doi:10.1016/j.trac.2009.09.009>. The test allows the comparison of
different solutions through a reference by first performing a rank
transformation on the input, then calculating and comparing the distances
between the solutions and the reference - the latter is measured in the L1
norm. The reference can be an external benchmark (e.g. an established gold
standard) or can be aggregated from the data. The calculated distances,
called SRD scores, are validated in two ways, see Héberger and
Kollár-Hunek (2011) <doi:10.1002/cem.1320>. A randomization test (also
called permutation test) compares the SRD scores of the solutions to the
SRD scores of randomly generated rankings. The second validation option is
cross-validation that checks whether the rankings generated from the
solutions come from the same distribution or not. For a detailed analysis
about the cross-validation process see Sziklai, Baranyi and Héberger
(2021) <arXiv:2105.11939>. The package offers a wide array of features
related to SRD including the computation of the SRD scores, validation
options, input preprocessing and plotting tools.

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

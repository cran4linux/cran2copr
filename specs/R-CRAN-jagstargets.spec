%global __brp_check_rpaths %{nil}
%global packname  jagstargets
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Targets for JAGS Workflows

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags >= 4.10
BuildRequires:    R-CRAN-tibble >= 3.0.1
BuildRequires:    R-CRAN-withr >= 2.1.2
BuildRequires:    R-CRAN-posterior >= 1.0.1
BuildRequires:    R-CRAN-fst >= 0.9.2
BuildRequires:    R-CRAN-digest >= 0.6.25
BuildRequires:    R-CRAN-R2jags >= 0.6.1
BuildRequires:    R-CRAN-targets >= 0.6.0
BuildRequires:    R-CRAN-rlang >= 0.4.10
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-qs >= 0.23.2
BuildRequires:    R-CRAN-coda >= 0.19.4
BuildRequires:    R-CRAN-tarchetypes >= 0.0.1
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-rjags >= 4.10
Requires:         R-CRAN-tibble >= 3.0.1
Requires:         R-CRAN-withr >= 2.1.2
Requires:         R-CRAN-posterior >= 1.0.1
Requires:         R-CRAN-fst >= 0.9.2
Requires:         R-CRAN-digest >= 0.6.25
Requires:         R-CRAN-R2jags >= 0.6.1
Requires:         R-CRAN-targets >= 0.6.0
Requires:         R-CRAN-rlang >= 0.4.10
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-qs >= 0.23.2
Requires:         R-CRAN-coda >= 0.19.4
Requires:         R-CRAN-tarchetypes >= 0.0.1
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Bayesian data analysis usually incurs long runtimes and cumbersome custom
code. A pipeline toolkit tailored to Bayesian statisticians, the
'jagstargets' R package is leverages 'targets' and 'R2jags' to ease this
burden. 'jagstargets' makes it super easy to set up scalable JAGS
pipelines that automatically parallelize the computation and skip
expensive steps when the results are already up to date. Minimal custom
code is required, and there is no need to manually configure branching, so
usage is much easier than 'targets' alone. For the underlying methodology,
please refer to the documentation of 'targets' <doi:10.21105/joss.02959>
and 'JAGS' (Plummer 2003)
<https://www.r-project.org/conferences/DSC-2003/Proceedings/Plummer.pdf>.

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

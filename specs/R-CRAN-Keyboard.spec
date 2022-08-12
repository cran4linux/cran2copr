%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Keyboard
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Designs for Early Phase Clinical Trials

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Iso 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 
Requires:         R-CRAN-Iso 
Requires:         R-CRAN-ggplot2 

%description
We developed a package 'Keyboard' for designing single-agent,
drug-combination, or phase I/II dose-finding clinical trials. The
'Keyboard' designs are novel early phase trial designs that can be
implemented simply and transparently, similar to the 3+3 design, but yield
excellent performance, comparable to those of more-complicated,
model-based designs (Yan F, Mandrekar SJ, Yuan Y (2017)
<doi:10.1158/1078-0432.CCR-17-0220>, Li DH, Whitmore JB, Guo W, Ji Y.
(2017) <doi:10.1158/1078-0432.CCR-16-1125>, Liu S, Johnson VE (2016)
<doi:10.1093/biostatistics/kxv040>, Zhou Y, Lee JJ, Yuan Y (2019)
<doi:10.1002/sim.8475>, Pan H, Lin R, Yuan Y (2020)
<doi:10.1016/j.cct.2020.105972>). The 'Keyboard' package provides tools
for designing, conducting, and analyzing single-agent, drug-combination,
and phase I/II dose-finding clinical trials. For more details about how to
use this packge, please refer to Li C, Sun H, Cheng C, Tang L, and Pan H.
(2022) "A software tool for both the maximum tolerated dose and the
optimal biological dose finding trials in early phase designs". Manuscript
submitted for publication.

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

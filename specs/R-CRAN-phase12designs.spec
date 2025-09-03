%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  phase12designs
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Comprehensive Tools for Running Model-Assisted Phase I/II Trial Simulations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-trialr 
BuildRequires:    R-CRAN-Iso 
Requires:         R-CRAN-trialr 
Requires:         R-CRAN-Iso 

%description
Provides a comprehensive set of tools to simulate, evaluate, and compare
model-assisted designs for early-phase (Phase I/II) clinical trials,
including: - BOIN12 (Bayesian optimal interval phase 1/11 trial design;
Lin et al. (2020) <doi:10.1200/PO.20.00257>), - BOIN-ET (Takeda, K.,
Taguri, M., & Morita, S. (2018) <doi:10.1002/pst.1864>), - EffTox (Thall,
P. F., & Cook, J. D. (2004) <doi:10.1111/j.0006-341X.2004.00218.x>), -
Ji3+3 (Joint i3+3 design; Lin, X., & Ji, Y. (2020)
<doi:10.1080/10543406.2020.1818250>), - PRINTE (probability intervals of
toxicity and efficacy design; Lin, X., & Ji, Y. (2021)
<doi:10.1177/0962280220977009>), - STEIN (simple toxicity and efficacy
interval design; Lin, R., & Yin, G. (2017) <doi:10.1002/sim.7428>), - TEPI
(toxicity and efficacy probability interval design; Li, D. H., Whitmore,
J. B., Guo, W., & Ji, Y. (2017) <doi:10.1158/1078-0432.CCR-16-1125>), -
uTPI (utility-based toxicity Probability interval design; Shi, H., Lin,
R., & Lin, X. (2024) <doi:10.1002/sim.8922>). Includes flexible simulation
parameters that allow researchers to efficiently compute operating
characteristics under various fixed and random trial scenarios and export
the results.

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

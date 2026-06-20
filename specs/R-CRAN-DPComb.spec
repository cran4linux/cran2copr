%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DPComb
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Discrete p-Value Combination Tests

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MCMCpack 
Requires:         R-CRAN-MCMCpack 

%description
Provides tools for performing p-value combination tests with discrete
input p-values. These tests combine significance evidence derived from
independent discrete statistics to test a global null hypothesis, which is
defined by the specified null distribution(s) of these discrete
statistics. The testing procedure involves two main steps: (1) Wasserstein
Adjustment: Each component of the combination statistic is replaced by an
adjusted Z statistic. This adjustment, based on the minimum Wasserstein
distance, preserves the discrete nature of the original statistics while
better aligning them with their counterparts under continuity. (2)
Calculation of the Significance of the Combination Statistic: A continuous
distribution that optimally matches the discrete distribution of the
combination statistic is obtained, and the testing p-value for the global
null hypothesis is computed. The first step is analogous to Lancaster's
approach but is generalized based on Wasserstein optimization. The second
step allows for asymptotic control of Type I error with higher statistical
power. The package implements several p-value combination methods,
including Fisher’s, Pearson’s, George’s, Stouffer’s, and Edgington’s
methods. The individual tests to be combined can be right-sided,
left-sided, or two-sided, and can be based on binomial, Poisson,
hypergeometric, noncentral hypergeometric, negative binomial, or geometric
distributions, or a mixture of them. The underlying methodology and its
foundations are described in the following references: Contador, Gonzalo
and Wu, Zheyang (2025). A minimum Wasserstein distance approach to
Fisher's combination of independent, discrete p-values. Scandinavian
Journal of Statistics, 52(3), 1281-1300. <doi:10.1111/sjos.12787>
Contador, Gonzalo and Wu, Zheyang (2026). Optimal Adjustment and
Combination of Independent Discrete p-Values. Under revision at the
Journal of Computational and Graphical Statistics.
<doi:10.48550/arXiv.2508.02647> Lancaster, HO (1949). The combination of
probabilities arising from data in discrete distributions. Biometrika,
36(3/4), 370-382. <doi:10.1093/biomet/36.3-4.370>.

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

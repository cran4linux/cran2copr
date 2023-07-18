%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  puniform
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Meta-Analysis Methods Correcting for Publication Bias

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ADGofTest >= 0.3
BuildRequires:    R-CRAN-Rcpp >= 0.12.15
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ADGofTest >= 0.3
Requires:         R-CRAN-Rcpp >= 0.12.15
Requires:         R-stats 
Requires:         R-CRAN-metafor 

%description
Provides meta-analysis methods that correct for publication bias and
outcome reporting bias. Four methods and a visual tool are currently
included in the package. The p-uniform method as described in van Assen,
van Aert, and Wicherts (2015) <doi:10.1037/met0000025> can be used for
estimating the average effect size, testing the null hypothesis of no
effect, and testing for publication bias using only the statistically
significant effect sizes of primary studies. The second method in the
package is the p-uniform* method as described in van Aert and van Assen
(2023) <doi:10.31222/osf.io/zqjr9>. This method is an extension of the
p-uniform method that allows for estimation of the average effect size and
the between-study variance in a meta-analysis, and uses both the
statistically significant and nonsignificant effect sizes. The third
method in the package is the hybrid method as described in van Aert and
van Assen (2017) <doi:10.3758/s13428-017-0967-6>. The hybrid method is a
meta-analysis method for combining an original study and replication and
while taking into account statistical significance of the original study.
The p-uniform and hybrid method are based on the statistical theory that
the distribution of p-values is uniform conditional on the population
effect size. The fourth method in the package is the Snapshot Bayesian
Hybrid Meta-Analysis Method as described in van Aert and van Assen (2018)
<doi:10.1371/journal.pone.0175302>. This method computes posterior
probabilities for four true effect sizes (no, small, medium, and large)
based on an original study and replication while taking into account
publication bias in the original study. The method can also be used for
computing the required sample size of the replication akin to power
analysis in null hypothesis significance testing. The meta-plot is a
visual tool for meta-analysis that provides information on the primary
studies in the meta-analysis, the results of the meta-analysis, and
characteristics of the research on the effect under study (van Assen et
al., 2023). Helper functions to apply the Correcting for Outcome Reporting
Bias (CORB) method to correct for outcome reporting bias in a
meta-analysis (van Aert & Wicherts, 2023).

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

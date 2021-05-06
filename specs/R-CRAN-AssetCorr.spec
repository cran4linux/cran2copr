%global packname  AssetCorr
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating Asset Correlations from Default Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-VineCopula 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-mvQuad 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-qpdf 
Requires:         R-CRAN-VineCopula 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-mvQuad 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-qpdf 

%description
Functions for the estimation of intra- and inter-cohort correlations in
the Vasicek credit portfolio model. For intra-cohort correlations, the
package covers the two method of moments estimators of Gordy (2000)
<doi:10.1016/S0378-4266(99)00054-0>, the method of moments estimator of
Lucas (1995) <https://jfi.pm-research.com/content/4/4/76> and a Binomial
approximation extension of this approach. Moreover, the maximum likelihood
estimators of Gordy and Heitfield (2010)
<http://elsa.berkeley.edu/~mcfadden/e242_f03/heitfield.pdf> and Duellmann
and Gehde-Trapp (2004) <http://hdl.handle.net/10419/19729> are
implemented. For inter-cohort correlations, the method of moments
estimator of Bluhm and Overbeck (2003)
<doi:10.1007/978-3-642-59365-9_2>/Bams et al. (2016)
<https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2676595> is provided
and the maximum likelihood estimators comprise the approaches of Gordy and
Heitfield (2010)/Kalkbrener and Onwunta (2010) <ISBN: 978-1906348250> and
Pfeuffer et al. (2020). Bootstrap and Jackknife procedures for bias
correction are included as well as the method of moments estimator of Frei
and Wunsch (2018) <doi:10.21314/JCR.2017.231> for auto-correlated time
series.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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

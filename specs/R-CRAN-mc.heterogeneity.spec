%global packname  mc.heterogeneity
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Monte Carlo Based Heterogeneity Test for Meta-Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-boot.heterogeneity 
Requires:         R-stats 
Requires:         R-CRAN-metafor 
Requires:         R-utils 
Requires:         R-CRAN-boot.heterogeneity 

%description
Implements a Monte Carlo Based Heterogeneity Test for standardized mean
differences (d), Fisher-transformed Pearson's correlations (r), and
natural-logarithm-transformed odds ratio (OR) in Meta-Analysis Studies.
Depending on the presence of moderators, this Monte Carlo Based Test can
be implemented in the random or mixed-effects model. This package uses
rma() function from the R package 'metafor' to obtain parameter estimates
and likelihood, so installation of R package 'metafor' is required. This
approach refers to the studies of Hedges (1981)
<doi:10.3102/10769986006002107>, Hedges & Olkin (1985,
ISBN:978-0123363800), Silagy, Lancaster, Stead, Mant, & Fowler (2004)
<doi:10.1002/14651858.CD000146.pub2>, Viechtbauer (2010)
<doi:10.18637/jss.v036.i03>, and Zuckerman (1994, ISBN:978-0521432009).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}

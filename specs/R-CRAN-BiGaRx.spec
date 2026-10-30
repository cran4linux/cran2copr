%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BiGaRx
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Unified Classical and Canonical Biplots

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Classical and canonical biplots computed from a single singular value
decomposition (SVD) engine. Includes the two biplots of Gabriel (1971)
<doi:10.1093/biomet/58.3.453>: the GH-biplot, named after its row markers
G and column markers H, which preserves the column metric (covariances and
correlations between variables), and the JK-biplot, named after its row
markers J and column markers K, which preserves the row metric (distances
between individuals). Also includes the HJ-biplot of Galindo (1986)
<https://upcommons.upc.edu/entities/publication/e17797dd-e20b-4fe5-b34a-f4cde41695ed>,
which combines the row markers J and the column markers H so that rows and
columns are both represented with maximum quality. Options include
configurable preprocessing, supplementary rows and columns, quality of
representation, contributions, goodness of fit, bootstrap confidence
intervals following Nieto, Galindo, Leiva and Vicente-Galindo (2014)
<doi:10.15446/rce.v37n2spe.47944>, and imputation of missing values by
iterative low-rank approximation following Gabriel and Zamir (1979)
<doi:10.1080/00401706.1979.10489819>. The canonical biplot, also known as
the multivariate analysis of variance (MANOVA) biplot, follows Amaro,
Vicente-Villardon and Galindo (2004)
<https://www.redalyc.org/pdf/339/33908807.pdf>. It is available for
one-way designs and for two-way designs with total, row, column and
interaction biplots. It comes with multivariate tests, pairwise
comparisons with Hotelling's T-squared statistic, log-ratio
transformations for compositional data and confidence regions for the
group means. The regions are circles or the ellipses of Krzanowski (1989)
<doi:10.1093/biomet/76.1.107>, computed consistently in the scale of the
within-groups covariance matrix. Plots use base graphics or 'ggplot2'.

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

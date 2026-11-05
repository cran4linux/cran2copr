%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CANE
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Comprehensive Groups of Experiments Analysis for Numerous Environments

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-utils 

%description
Pooled analysis of a series of designed experiments repeated over
locations, seasons or years, where treatment-by-environment interaction is
of primary interest. One design-specific function call performs
environment-wise analysis of variance, formal testing of homogeneity of
error variances, an optional variance-stabilising transformation, pooled
analysis of variance with the correct error stratum for every effect, and
multiple comparison of means. Five classical designs are supported:
completely randomised ('PooledCRD()'), randomised block ('PooledRBD()'),
Latin square ('PooledLSD()'), split plot ('PooledSPD()') and strip plot
('PooledStPD()'). Homogeneity of error variances is assessed by Bartlett's
test computed on the environment-wise error mean squares as in Bartlett
(1937) <doi:10.1098/rspa.1937.0109>, and by the median-centred
Brown-Forsythe form of Levene's test <doi:10.1080/01621459.1974.10482955>,
which is robust to non-normality. When variances are heterogeneous,
Aitken's transformation (division of each observation by the square root
of the error mean square of its own environment) may be applied, and
treatment means are reported on both the transformed and the original
scale. For split plot and strip plot designs every effect is tested
against its proper error term, and mean separation uses the error mean
square and degrees of freedom of the corresponding stratum. The
statistical theory is given in Cochran and Cox (1957, ISBN:9780471162032),
Gomez and Gomez (1984, ISBN:9780471870928), Dean et al. (2017)
<doi:10.1007/978-3-319-52250-0> and Ruiz et al. (2024)
<doi:10.1007/978-3-031-65575-3>.

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

%global __brp_check_rpaths %{nil}
%global packname  getspres
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          SPRE Statistics for Exploring Heterogeneity in Meta-Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotrix >= 3.5.12
BuildRequires:    R-CRAN-colorRamps >= 2.3
BuildRequires:    R-CRAN-metafor >= 1.9.6
BuildRequires:    R-CRAN-colorspace >= 1.2.6
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-dplyr >= 0.4.1
Requires:         R-CRAN-plotrix >= 3.5.12
Requires:         R-CRAN-colorRamps >= 2.3
Requires:         R-CRAN-metafor >= 1.9.6
Requires:         R-CRAN-colorspace >= 1.2.6
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-dplyr >= 0.4.1

%description
An implementation of SPRE (standardised predicted random-effects)
statistics in R to explore heterogeneity in genetic association meta-
analyses, as described by Magosi et al. (2019)
<doi:10.1093/bioinformatics/btz590>. SPRE statistics are precision
weighted residuals that indicate the direction and extent with which
individual study-effects in a meta-analysis deviate from the average
genetic effect. Overly influential positive outliers have the potential to
inflate average genetic effects in a meta-analysis whilst negative
outliers might lower or change the direction of effect. See the 'getspres'
website for documentation and examples
<https://magosil86.github.io/getspres/>.

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

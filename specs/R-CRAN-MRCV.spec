%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MRCV
%global packver   0.4-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Methods for Analyzing Multiple Response Categorical Variables (MRCVs)

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tables 
Requires:         R-CRAN-tables 

%description
Provides functions for analyzing the association between one single
response categorical variable (SRCV) and one multiple response categorical
variable (MRCV), or between two or three MRCVs.  A modified Pearson
chi-square statistic can be used to test for marginal independence for the
one or two MRCV case, or a more general loglinear modeling approach can be
used to examine various other structures of association for the two or
three MRCV case.  Bootstrap- and asymptotic-based standardized residuals
and model-predicted odds ratios are available, in addition to other
descriptive information. Statisical methods implemented are described in
Bilder et al. (2000) <doi:10.1080/03610910008813665>, Bilder and Loughin
(2004) <doi:10.1111/j.0006-341X.2004.00147.x>, Bilder and Loughin (2007)
<doi:10.1080/03610920600974419>, and Koziol and Bilder (2014)
<https://journal.r-project.org/articles/RJ-2014-014/>.

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
